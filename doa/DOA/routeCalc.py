import requests
import math

coords = []

# Get the Latitude and Longitude of an address
def geocode_address(address, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        return {"lat": location["lat"], "lng": location["lng"]}
    else:
        raise Exception(f"Geocoding failed: {data['status']}")

# Convert an entire list of addresses to Lat and Lng
def getAddressPoints(addresses = [], _coords = [], use_tsp = False):
    api_key = "----------PUT YOUR API KEY HERE---------"

    # Loops through the addresses and appends them to a list of coordinates
    for address in addresses:
        location = geocode_address(address, api_key)
        if location:
            _coords.append({
                "lat": location["lat"],
                "lng": location["lng"]
            })
    min_cost, path = held_karp(list(_coords))
    optimized_coords = [_coords[i] for i in path]

    if use_tsp: return optimized_coords
    else: return _coords

# Euclidean distance between two points (latitude, longitude)
def euclidean_distance(p1, p2):
    lat1, lon1 = float(p1['lat']), float(p2['lng'])
    lat2, lon2 = float(p2['lat']), float(p2['lng'])
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

# Held-Karp Algorithm for TSP with path reconstruction
def held_karp(locations):
    n = len(locations)
    memo = {}
    parent = {} # to reconstruct the path

    # Helper function to compute the minimum cost of visiting a subset of nodes
    def dp(mask, pos):
        if mask == (1 << n) - 1:
            return euclidean_distance(locations[pos], locations[0]) # Return to the start
        if (mask, pos) in memo:
            return memo[(mask, pos)]
    
        ans = float('inf')
        best_next_node = None
        for i in range(n):
            if not (mask & (1 << i)):
                cost = euclidean_distance(locations[pos], locations[i]) + dp(mask | (1 << i), i)
                if cost < ans:
                    ans = cost
                    best_next_node = i

        memo[(mask, pos)] = ans
        parent[(mask, pos)] = best_next_node # Track the best next node for the path
        return ans
    
    # Start from node 0 with only the start node visitied
    min_cost = dp(1, 0)

    # Reconstruct the path
    mask = 1 # Start with the mask where only the node 0 is visited
    path = [0]
    while True:
        next_node = parent.get((mask, path[-1]))

        if next_node is None:
            print(f"Error: next_node is None at mask {mask} and path {path}")
            break

        if next_node < 0 or next_node >= n:
            print(f"Error: invalid next_node value {next_node} at mask {mask} and path {path}")
            break

        path.append(next_node)
        mask |= (1 << next_node)
        if len(path) == n:
            break
    path.append(0) # return to the start city

    return min_cost, path