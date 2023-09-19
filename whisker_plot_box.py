import json
import os
import pandas as pd
import numpy as np


# Step 1: Read the JSON file
with open('input/filtered_data.json', 'r') as file:
    data = json.load(file)

# Convert the JSON data into a DataFrame
df = pd.DataFrame(data)

# Define the cities
cities = ['POPAYÁN', 'SAN GIL']  # Replace 'Another_City' with the name of the other city

for city in cities:
    # Step 2: Filter data for each city
    city_data = df[df['Municipality'] == city]

    # Step 3: Extract Velocity_of_the_Wind values
    wind_speeds = city_data['Velocity_of_the_Wind'].astype(float)

    # Step 4: Generate box plot statistics
    quartiles = np.percentile(wind_speeds, [25, 50, 75])
    q1, median, q3 = quartiles
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    # Detect and print outliers
    outliers = wind_speeds[(wind_speeds < lower_bound) | (wind_speeds > upper_bound)]

    # Specify the full path to the output file in the 'output' folder
    output_file_path = os.path.join('output', f'{city}_whisker_plot_values.txt')

    # Print statistics to the console
    with open(output_file_path, 'w') as result_file:
        result_file.write(f'City: {city}\n')
        result_file.write(f'Q1: {q1}\n')
        result_file.write(f'Median (Q2): {median}\n')
        result_file.write(f'Q3: {q3}\n')
        result_file.write(f'IQR: {iqr}\n')
        result_file.write(f'Lower Bound: {lower_bound}\n')
        result_file.write(f'Upper Bound: {upper_bound}\n')
        result_file.write(f'Outliers: {list(outliers)}\n')
        result_file.write('\n')
