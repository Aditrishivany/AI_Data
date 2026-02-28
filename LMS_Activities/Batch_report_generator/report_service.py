import pandas as pd
import os
import json
from student_report import StudentReport

class ReportService:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def load_csv(self, filename):
        path = os.path.join(self.input_dir, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(filename)
        return pd.read_csv(path)

    def clean_df(self, df):
        df = df.drop_duplicates()
        df = df.fillna(0)
        return df

    def generate_reports(self):
        # Load CSVs
        students = self.clean_df(self.load_csv("students.csv"))
        attendance = self.clean_df(self.load_csv("attendance.csv"))
        marks = self.clean_df(self.load_csv("marks.csv"))

        # Debug
        print("DEBUG → Students columns:", students.columns)
        print("DEBUG → Attendance columns:", attendance.columns)
        print("DEBUG → Marks columns:", marks.columns)

        # Normalize all columns to lowercase
        for df in [students, attendance, marks]:
            df.columns = df.columns.str.strip().str.lower()

        # Ensure consistent student ID column name
        students.rename(columns={
            "studentid": "studentid",
            "id": "studentid",
            "rollnumber": "studentid",
            "rollno": "studentid"
        }, inplace=True)

        attendance.rename(columns={
            "studentid": "studentid",
            "attendance": "present"
        }, inplace=True)

        marks.rename(columns={
            "studentid": "studentid",
            "score": "marks"
        }, inplace=True)

        # Calculate attendance percentage
        attendance_summary = attendance.groupby("studentid")["present"].mean() * 100
        attendance_summary = attendance_summary.reset_index().rename(
            columns={"present": "attendancepercent"}
        )

        # Calculate average marks
        marks_summary = marks.groupby("studentid")["marks"].mean().reset_index()
        marks_summary.rename(columns={"marks": "avgmarks"}, inplace=True)

        # Merge all data
        merged = students.merge(attendance_summary, on="studentid", how="left")
        merged = merged.merge(marks_summary, on="studentid", how="left")
        merged.fillna(0, inplace=True)

        # Generate student reports
        reports = []
        for _, row in merged.iterrows():
            r = StudentReport(
                row.studentid,
                row.name,
                row.attendancepercent,
                row.avgmarks
            )
            reports.append(r.to_dict())

        report_df = pd.DataFrame(reports)

        # Ensure output folder exists
        os.makedirs(self.output_dir, exist_ok=True)

        # Save CSV
        report_df.to_csv(os.path.join(self.output_dir, "report.csv"), index=False)

        # Save JSON Summary
        summary = {
            "totalStudents": int(len(report_df)),
            "avgAttendance": float(report_df["attendancepercent"].mean()),
            "avgMarks": float(report_df["avgmarks"].mean()),
            "passCount": int((report_df["status"] == "PASS").sum()),
            "failCount": int((report_df["status"] == "FAIL").sum()),
            "top3Students": [
                {
                    "studentid": str(row["studentid"]),
                    "name": row["name"],
                    "avgmarks": float(row["avgmarks"])
                }
                for _, row in report_df.nlargest(3, "avgmarks").iterrows()
            ]
        }

        with open(os.path.join(self.output_dir, "summary.json"), "w") as f:
            json.dump(summary, f, indent=4)