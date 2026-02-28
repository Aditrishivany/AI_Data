import argparse
from report_service import ReportService

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    try:
        service = ReportService(args.input, args.output)
        service.generate_reports()
        print("✔ Reports generated successfully!")

    except FileNotFoundError as e:
        print(f"ERROR: Missing file → {e}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")

if __name__ == "__main__":
    main()