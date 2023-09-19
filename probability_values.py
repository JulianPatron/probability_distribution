import json
import os
import pandas as pd
from scipy.optimize import minimize_scalar
from scipy.stats import weibull_min


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

    # Step 4: Fit a Weibull distribution
    params = weibull_min.fit(wind_speeds)

    # Step 5: Find the mode (most probable wind speed)
    mode = params[1]

    # Step 6: Define a function to maximize for wind energy
    def wind_energy(wind_speed):
        return -wind_speed**3 * weibull_min.pdf(wind_speed, *params)

    # Step 7: Find the wind speed that maximizes wind energy
    result = minimize_scalar(wind_energy)
    max_wind_energy_speed = result.x

    # Specify the full path to the output file in the 'output' folder
    output_file_path = os.path.join('output', f'{city}_wind_results.txt')

    # Write the results to the output file
    with open(output_file_path, 'w') as result_file:
        result_file.write(f'City: {city}\n')
        result_file.write(f'Most Probable Wind Speed (Mode): {mode}\n')
        result_file.write(f'Wind Speed for Max Wind Energy: {max_wind_energy_speed}\n')
        result_file.write('\n')
