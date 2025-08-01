# Base class
class Report:
    def __init__(self, title):
        self.title = title

    def generate(self):
        raise NotImplementedError("Subclasses must implement this method")

# PDF report subclass
class PDFReport(Report):
    def generate(self):
        print(f"Generating PDF report: {self.title}.pdf")

# Excel report subclass
class ExcelReport(Report):
    def generate(self):
        print(f"Generating Excel report: {self.title}.xlsx")

# HTML report subclass
class HTMLReport(Report):
    def generate(self):
        print(f"Generating HTML report: {self.title}.html")

# ReportManager that handles all reports
class ReportManager:
    def __init__(self):
        self.reports = []

    def add_report(self, report):
        if isinstance(report, Report):
            self.reports.append(report)
        else:
            raise TypeError("Only Report objects can be added.")

    def generate_all(self):
        print("Generating all reports:")
        for report in self.reports:
            report.generate()

# Example usage
manager = ReportManager()
manager.add_report(PDFReport("Sales Report"))
manager.add_report(ExcelReport("Inventory Report"))
manager.add_report(HTMLReport("Website Analytics"))

manager.generate_all()
