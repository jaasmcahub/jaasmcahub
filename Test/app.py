from flask import Flask, render_template, request, jsonify
import subprocess
import csv
import os

app = Flask(__name__)

# Path to the Python script and result CSV file
PROCESS_SCRIPT = "process_data.py"  # Replace with the script to generate result.csv
RESULT_CSV = "result.csv"

@app.route("/")
def index():
    # Render the HTML page
    return render_template("index.html", data=[])

@app.route("/execute", methods=["POST"])
def execute_script():
    try:
        # Run the external Python script
        subprocess.run(["python", PROCESS_SCRIPT], check=True)
        
        # Check if the CSV file exists
        if not os.path.exists(RESULT_CSV):
            return jsonify({"error": "Result CSV file not found."}), 400

        # Read the CSV file and prepare data to return
        data = []
        with open(RESULT_CSV, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        
        return jsonify({"data": data})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Error executing script: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
