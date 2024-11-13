import pandas as pd

def load_data(file_path):
    """Loads data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("File not found.")
        return None

def process_data(data):
    """Processes data by removing any missing values and calculating summary statistics."""
    if data is not None:
        data.dropna(inplace=True)
        summary = data.describe()
        print("Data processed successfully.")
        return summary
    else:
        print("No data to process.")
        return None

def generate_report(summary):
    """Generates a report from the summary statistics."""
    if summary is not None:
        with open("report.txt", "w") as file:
            file.write("Data Summary Report\n")
            file.write(summary.to_string())
        print("Report generated successfully as 'report.txt'.")

# Main script
file_path = "data.csv"
data = load_data(file_path)
summary = process_data(data)
generate_report(summary)
