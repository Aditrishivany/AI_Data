class StudentReport:
    def __init__(self, studentid, name, attendancepercent, avgmarks):
        self.studentid = studentid
        self.name = name
        self.attendancepercent = attendancepercent
        self.avgmarks = avgmarks
        self.status = "PASS" if avgmarks >= 40 else "FAIL"

    def to_dict(self):
        return {
            "studentid": self.studentid,
            "name": self.name,
            "attendancepercent": self.attendancepercent,
            "avgmarks": self.avgmarks,
            "status": self.status
        }