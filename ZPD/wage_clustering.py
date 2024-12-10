import json
import matplotlib.pyplot as plt
import numpy as np

# Load data from JSON
with open('classified_district_prices.json', encoding='utf-8') as f:
    data = json.load(f)

# Calculate the mean wage for each district, excluding those with fewer than 4 values
district_means = {
    district: np.mean(values) for district, values in data.items() if len(values) >= 4
}

# Sort districts by mean wage in descending order
sorted_districts = sorted(district_means.items(), key=lambda x: x[1], reverse=True)

# Extract sorted names and mean wages
sorted_names = [f"{district} (n={len(data[district])})" for district, _ in sorted_districts]
sorted_means = [mean for _, mean in sorted_districts]

# Plot ranked districts
plt.figure(figsize=(15, 7))
plt.bar(sorted_names, sorted_means, color='skyblue', edgecolor='black')
plt.xticks(rotation=90)
plt.ylabel('Average Wage')
plt.title('Districts Ranked by Average Wage (n ≥ 4)')
plt.tight_layout()

# Show the plot
plt.show()
