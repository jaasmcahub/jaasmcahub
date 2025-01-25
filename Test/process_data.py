import csv

def generate_result_csv():
    # Define the data to be written to result.csv
    data = [
        ["Name", "Age", "Location"],
        ["Alice", 30, "New York"],
        ["Bob", 25, "Los Angeles"],
        ["Charlie", 35, "Chicago"]
    ]

    # Write the data to result.csv
    with open("result.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    print("result.csv generated successfully.")

if __name__ == "__main__":
    # Call the function to generate result.csv
    generate_result_csv()
