import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import random


# Load and preprocess data
@st.cache_data
def load_data():
    data = pd.read_csv('data/markets.csv')
    data = data.dropna(subset=['x', 'y'])
    return data

data = load_data()

# List of possible locations (for simplicity, using a static list; in practice, this might come from the dataset)
possible_locations = [
    "San Francisco, CA", "Los Angeles, CA", "New York, NY",
    "Chicago, IL", "Houston, TX", "Phoenix, AZ"
]

# List of possible preferences (derived from the dataset columns)
possible_preferences = [
    'Organic', 'Bakedgoods', 'Cheese', 'Crafts', 'Flowers', 'Eggs', 
    'Seafood', 'Herbs', 'Vegetables', 'Honey', 'Jams', 'Maple', 
    'Meat', 'Nursery', 'Nuts', 'Plants', 'Poultry', 'Prepared', 
    'Soap', 'Trees', 'Wine', 'Coffee', 'Beans', 'Fruits', 'Grains', 
    'Juices', 'Mushrooms', 'PetFood', 'Tofu', 'WildHarvested'
]

# Geocoding function
def geocode_location(location):
    geolocator = Nominatim(user_agent="market_recommender",timeout=10)
    geocode_result = geolocator.geocode(location)
    if geocode_result:
        return geocode_result.latitude, geocode_result.longitude
    else:
        return None

# Reverse geocoding function to get address from coordinates
def reverse_geocode(lat, lon):
    geolocator = Nominatim(user_agent="market_recommender")
    location = geolocator.reverse((lat, lon))
    return location.address if location else "Address not found"

# Distance calculation function
def calculate_distances(user_coords, markets):
    distances = []
    for index, row in markets.iterrows():
        market_coords = (row['y'], row['x'])
        distance = geodesic(user_coords, market_coords).miles
        distances.append(distance)
    markets['distance'] = distances
    return markets

# Filter markets by distance function
def filter_markets_by_distance(markets, max_distance=20):
    return markets[markets['distance'] <= max_distance]

# Filter and recommend markets function
def recommend_markets(user_coords, markets, max_distance=20, preferences=None, num_recommendations=10):
    markets_with_distances = calculate_distances(user_coords, markets)
    filtered_markets = filter_markets_by_distance(markets_with_distances, max_distance)
    
    if preferences:
        for pref in preferences:
            filtered_markets = filtered_markets[filtered_markets[pref] == 'Y']
    
    # Sort by distance and get the top recommendations
    sorted_markets = filtered_markets.sort_values(by='distance')
    top_markets = sorted_markets.head(num_recommendations)
    
    # Select the required columns
    result = top_markets[['MarketName', 'Location', 'Website', 'Season1Time', 'x', 'y']]
    
    return result

def recommendation_page():
    st.title("Market Recommendations")

    # User input for location and preferences
    user_location = st.selectbox("Select your location:", possible_locations)
    user_preferences = st.multiselect("Select your preferences:", possible_preferences)

    # Recommendation button
    if st.button("Get Recommendations"):
        # Geocode user location
        user_coords = geocode_location(user_location)
        
        if user_coords:
            recommended_markets = recommend_markets(user_coords, data, preferences=user_preferences)
            st.subheader("Recommended Markets")
            # Array of images 
            image_urls = [
                "pages\Farmers_market.jpeg",
                "pages\Farmers_market2.jpeg"
            ]
           
            

            # for loop for each recommendation markets
            for _, row in recommended_markets.iterrows():
                with st.expander(f"{row['MarketName']}"):
                    # Select a random image URL
                    selected_image_url = random.randint(0,1)
                    # Display image placeholder (since the dataset might not have image URLs)
                    st.image(image_urls[selected_image_url], width=200)
                    st.write(f"**Location**: {reverse_geocode(row['y'], row['x'])}")
                    st.write(f"**Latitude**: {row['y']}")
                    st.write(f"**Longitude**: {row['x']}")
                    st.write(f"**Website**: {row['Website']}")
                    st.write(f"**Opening Hours**: {row['Season1Time']}")
        else:
            st.error("Location not found. Please enter a valid location.")
if __name__ == '__main__':
    recommendation_page()
