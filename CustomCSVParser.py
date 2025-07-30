import csv
def read_csv(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

            if not data:
                print("CSV file is empty.")
                return

            # Show available columns
            print("\nAvailable columns:")
            for col in data[0].keys():
                print("-", col)

            # Ask user for column to average
            column = input("\nEnter the column name to calculate average: ").strip()

            if column not in data[0]:
                print(f"Column '{column}' not found.")
                return

            # Extract and convert values to float
            values = []
            for row in data:
                try:
                    value = float(row[column])
                    values.append(value)
                except ValueError:
                    print(f"Warning: Skipping non-numeric value '{row[column]}' in row.")

            if not values:
                print("No valid numeric data found in the column.")
                return

            # Calculate average
            average = sum(values) / len(values)
            print(f"\nAverage of column '{column}' = {average:.2f}")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = input("Enter the CSV file name (e.g., data.csv): ")
read_csv(filename)
