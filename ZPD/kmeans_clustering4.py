import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

output_dir = 'dzivoklu_data'

# Load data
def load_data(location_name):
    try:
        # Load regular data
        with open(f"{output_dir}/{location_name}_prices.json", 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {"one_time_purchase": []}

    try:
        # Load archived data
        with open(f"{output_dir}/archived_{location_name}_prices.json", 'r', encoding='utf-8') as json_file:
            archived_data = json.load(json_file)
    except FileNotFoundError:
        archived_data = {"one_time_purchase": []}

    # Combine data from both sources
    combined_data = {
        "one_time_purchase": data["one_time_purchase"] + archived_data["one_time_purchase"]
    }
    return combined_data



def extract_prices_and_sizes(data):
    one_time_purchase = [(entry['Price_per_m²'], entry['Price'], entry['m²']) for entry in data['one_time_purchase']]
    return one_time_purchase


# Analyze clusters
def analyze_clusters(locations, n_clusters):
    all_one_time_purchase = []
    district_labels = []

    # Load data from each location
    for location in locations:
        location_name = location["name"]
        data = load_data(location_name)
        if data:
            one_time_purchase = extract_prices_and_sizes(data)
            all_one_time_purchase.extend(one_time_purchase)
            district_labels.extend([location_name] * len(one_time_purchase))

    # Convert data into arrays for clustering
    all_one_time_purchase = np.array(all_one_time_purchase)
    prices_per_m2 = all_one_time_purchase[:, 0]  # Price per m²
    sizes = all_one_time_purchase[:, 2]          # Size (m²)
    features = np.column_stack((prices_per_m2, sizes))

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(features)

    # Combine data into a DataFrame for easier analysis
    combined_data = pd.DataFrame({
        'District': district_labels,
        'Cluster': labels,
        'Size (m²)': sizes,
        'Price per m²': prices_per_m2
    })

    # Cluster composition by district
    cluster_summary = combined_data.groupby(['Cluster', 'District']).size().unstack(fill_value=0)

    # Descriptive statistics for clusters
    cluster_stats = combined_data.groupby('Cluster').agg({
        'Size (m²)': ['mean', 'median', 'std'],
        'Price per m²': ['mean', 'median', 'std']
    })

    # Print and visualize results
    print("Cluster Summary by District:")
    print(cluster_summary)

    print("\nDescriptive Statistics for Each Cluster:")
    print(cluster_stats)

    # Return combined data for further analysis if needed
    return combined_data, kmeans.cluster_centers_, cluster_summary


# Plot clusters on the original data
def plot_clusters(combined_data, cluster_centers):
    # Create the scatter plot figure
    plt.figure(figsize=(10, 6))

    # Plot data points colored by cluster
    for cluster_id in combined_data['Cluster'].unique():
        cluster_data = combined_data[combined_data['Cluster'] == cluster_id]
        plt.scatter(
            cluster_data['Size (m²)'],
            cluster_data['Price per m²'],
            label=f'Cluster {cluster_id}',
            alpha=0.6
        )

    # Plot cluster centers
    cluster_centers = np.array(cluster_centers)
    plt.scatter(cluster_centers[:, 1], cluster_centers[:, 0], c='red', marker='x', s=200, label='Cluster Centers')

    plt.title("KMeans Clustering of Price per m² and Size")
    plt.xlabel("Size (m²)")
    plt.ylabel("Price per m²")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()


# Plot the cluster composition heatmap
def plot_cluster_composition(cluster_summary):
    # Create the heatmap figure
    plt.figure(figsize=(12, 8))
    sns.heatmap(cluster_summary, cmap="YlGnBu", annot=True, fmt="d", linewidths=.5)
    plt.title("Cluster Composition by District")
    plt.xlabel("District")
    plt.ylabel("Cluster")
    plt.tight_layout()


# Full list of districts with details
locations = [
   {"name": "Centrs", "url": "https://www.ss.lv/lv/real-estate/flats/riga/centre/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/centre/page{}.html", "pages": 158},
    {"name": "Āgenskalns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/agenskalns/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/agenskalns/page{}.html", "pages": 34},
    {"name": "Aplokciems", "url": "https://www.ss.lv/lv/real-estate/flats/riga/aplokciems/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/aplokciems/page{}.html", "pages": 1},
    {"name": "Berģi", "url": "https://www.ss.lv/lv/real-estate/flats/riga/bergi/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/bergi/page{}.html", "pages": 1},
    {"name": "Bieriņi", "url": "https://www.ss.lv/lv/real-estate/flats/riga/bierini/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/bierini/page{}.html", "pages": 2},
    {"name": "Bolderāja", "url": "https://www.ss.lv/lv/real-estate/flats/riga/bolderaya/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/bolderaya/page{}.html", "pages": 8},
    {"name": "Brekši", "url": "https://www.ss.lv/lv/real-estate/flats/riga/breksi/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/breksi/page{}.html", "pages": 2},
    {"name": "Čiekurkalns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/chiekurkalns/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/chiekurkalns/page{}.html", "pages": 9},
    {"name": "Dārzciems", "url": "https://www.ss.lv/lv/real-estate/flats/riga/darzciems/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/darzciems/page{}.html", "pages": 10},

    {"name": "Daugavgrīva", "url": "https://www.ss.lv/lv/real-estate/flats/riga/daugavgriva/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/daugavgriva/page{}.html", "pages": 5},
    {"name": "Dreiliņi", "url": "https://www.ss.lv/lv/real-estate/flats/riga/dreilini/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/dreilini/page{}.html", "pages": 2},
    {"name": "Dzegužkalns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/dzeguzhkalns/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/dzeguzhkalns/page{}.html", "pages": 8},
    {"name": "Grīziņkalns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/grizinkalns/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/grizinkalns/page{}.html", "pages": 5},
    {"name": "Iļģuciems", "url": "https://www.ss.lv/lv/real-estate/flats/riga/ilguciems/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/ilguciems/page{}.html", "pages": 18},
    {"name": "Imanta", "url": "https://www.ss.lv/lv/real-estate/flats/riga/imanta/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/imanta/page{}.html", "pages": 29},
    {"name": "Jugla", "url": "https://www.ss.lv/lv/real-estate/flats/riga/yugla/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/yugla/page{}.html", "pages": 20},

    {"name": "Ķengarags", "url": "https://www.ss.lv/lv/real-estate/flats/riga/kengarags/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/kengarags/page{}.html", "pages": 36},
    {"name": "Ķīpsala", "url": "https://www.ss.lv/lv/real-estate/flats/riga/kipsala/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/kipsala/page{}.html", "pages": 2},

    {"name": "Klīversala", "url": "https://www.ss.lv/lv/real-estate/flats/riga/kliversala/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/kliversala/page{}.html", "pages": 4},
    {"name": "Krasta_r-ns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/krasta-st-area/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/krasta-st-area/page{}.html", "pages": 8},
    {"name": "Kundziņsala", "url": "https://www.ss.lv/lv/real-estate/flats/riga/kundzinsala/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/kundzinsala/page{}.html", "pages": 3},
    {"name": "Latgales_priekšpilsēta", "url": "https://www.ss.lv/lv/real-estate/flats/riga/maskavas-priekshpilseta/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/maskavas-priekshpilseta/page{}.html", "pages": 13},
    {"name": "Mangaļi", "url": "https://www.ss.lv/lv/real-estate/flats/riga/mangali/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/mangali/page{}.html", "pages": 3},
    {"name": "Mangaļsala", "url": "https://www.ss.lv/lv/real-estate/flats/riga/mangalsala/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/mangalsala/page{}.html", "pages": 4},
    {"name": "Mežaparks", "url": "https://www.ss.lv/lv/real-estate/flats/riga/mezhapark/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/mezhapark/page{}.html", "pages": 8},
    {"name": "Mežciems", "url": "https://www.ss.lv/lv/real-estate/flats/riga/mezhciems/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/mezhciems/page{}.html", "pages": 15},
    {"name": "Pļavnieki", "url": "https://www.ss.lv/lv/real-estate/flats/riga/plyavnieki/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/plyavnieki/page{}.html", "pages": 31},
    {"name": "Purvciems", "url": "https://www.ss.lv/lv/real-estate/flats/riga/purvciems/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/purvciems/page{}.html", "pages": 48},

    {"name": "Šampēteris-Pleskodāle", "url": "https://www.ss.lv/lv/real-estate/flats/riga/shampeteris-pleskodale/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/shampeteris-pleskodale/page{}.html", "pages": 7},
    {"name": "Sarkandaugava", "url": "https://www.ss.lv/lv/real-estate/flats/riga/sarkandaugava/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/sarkandaugava/page{}.html", "pages": 15},
    {"name": "Šķirotava", "url": "https://www.ss.lv/lv/real-estate/flats/riga/shkirotava/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/shkirotava/page{}.html", "pages": 1},
    {"name": "Teika", "url": "https://www.ss.lv/lv/real-estate/flats/riga/teika/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/teika/page{}.html", "pages": 26},
    {"name": "Torņakalns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/tornjakalns/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/tornjakalns/page{}.html", "pages": 6},


    
    {"name": "Vecmīlgrāvis", "url": "https://www.ss.lv/lv/real-estate/flats/riga/vecmilgravis/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/vecmilgravis/page{}.html", "pages": 12},
    {"name": "Vecrīga", "url": "https://www.ss.lv/lv/real-estate/flats/riga/vecriga/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/vecriga/page{}.html", "pages": 9},

    {"name": "Zasulauks", "url": "https://www.ss.lv/lv/real-estate/flats/riga/zasulauks/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/zasulauks/page{}.html", "pages": 1},
    {"name": "Ziepniekkalns", "url": "https://www.ss.lv/lv/real-estate/flats/riga/ziepniekkalns/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/ziepniekkalns/page{}.html", "pages": 22},
    {"name": "Zolitūde", "url": "https://www.ss.lv/lv/real-estate/flats/riga/zolitude/page{}.html", "archive_url": "https://www.ss.lv/lv/archive/real-estate/flats/riga/zolitude/page{}.html", "pages": 14},

    
    
    
]

# Run the analysis with 5 clusters
n_clusters = 22
combined_data, cluster_centers, cluster_summary = analyze_clusters(locations, n_clusters)

# Plot the scatter plot of clusters
plot_clusters(combined_data, cluster_centers)

# Plot the cluster composition heatmap
plot_cluster_composition(cluster_summary)

# Show both plots
plt.show()
