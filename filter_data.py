import json


# Load the JSON data from the file
with open("input/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Filter the data by municipality
filtered_data = [entry for entry in data if entry["Municipality"] in ["SAN GIL", "POPAYÁN"]]

# Save the filtered data to a new file
with open("input/filtered_data.json", "w") as f:
    json.dump(filtered_data, f, indent=2)