import json
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import weibull_min
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

    # Step 4: Fit a Weibull distribution
    params = weibull_min.fit(wind_speeds)

    # Generate data points for the Weibull distribution
    x = np.linspace(0, wind_speeds.max(), 100)
    y = weibull_min.pdf(x, *params)

    # Step 5: Plot the probability distribution graph
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Weibull Fit')
    plt.hist(wind_speeds, bins=20, density=True, alpha=0.6, label='Velocidad del Viento')
    plt.title(f'Distribución de probabilidad para la Velocidad del Viento en {city}')
    plt.xlabel('Velocidad del Viento (m/s)')
    plt.ylabel('Densidad de Probabilidad')
    plt.legend()

    # Save the plot as an image
    plt.savefig(f'{city}_distribución.png')

    # Show the plot
    plt.show()
