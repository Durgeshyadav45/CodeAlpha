
import requests
import folium

def get_geolocation(ip_address):
    # Use ipinfo.io to get geolocation based on IP address
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data

def display_on_map(latitude, longitude):
    # Create a map centered around the provided latitude and longitude
    geo_map = folium.Map(location=[latitude, longitude], zoom_start=10)
    
    # Add a marker for the user's location
    folium.Marker([latitude, longitude], popup="Your Location").add_to(geo_map)
    
    # Save the map as an HTML file
    geo_map.save("geolocation_map.html")

if __name__ == "__main__":
    # Replace with the desired IP address or leave it blank to get the user's own IP
    target_ip = input("Enter the target IP address (or press Enter to use your own IP): ")

    if not target_ip:
        # Use the user's own IP address
        response = requests.get("http://ipinfo.io/json")
        data = response.json()
        target_ip = data.get("ip")

    if target_ip:
        geolocation_data = get_geolocation(target_ip)

        # Extract latitude and longitude from the geolocation data
        latitude, longitude = map(float, geolocation_data.get("loc", "").split(","))

        # Display the location on a map
        display_on_map(latitude, longitude)

        print(f"Geolocation for IP address {target_ip}:")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print("Map saved as 'geolocation_map.html'")
    else:
        print("Invalid IP address.")
