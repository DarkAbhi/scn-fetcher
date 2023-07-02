import requests
import json

"""
FETCH ALL STATES IN INDIA
"""

# URL to get all the states in India
states_url = "https://www.olx.in/api/locations?levels=state&hideAddressComponents=true&lang=en-IN"

headers = {
    'User-Agent': 'PostmanRuntime/7.32.2'
}

# Array to store the response data
states_response_data = []

# Make the GET request with the custom headers to get all states
response = requests.get(states_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response as JSON
    json_data = response.json()
    # Get the 'data' key from the response and append it to response_data
    states_response_data.extend(json_data.get('data', []))
else:
    print(f"Request failed with status code {response.status_code}")

# Save all the states response data to a file
with open('states.json', 'w') as file:
    json.dump(states_response_data, file)

print("All states data saved to 'states.json' file.")


def fetch_with_parents(open_file_name, write_file_name):
    # Read the states JSON file
    with open(open_file_name, 'r') as file:
        data = json.load(file)

    response_data = []

    # Iterate over each JSON object in the array
    for obj in data:
        # Get the value of the 'id' key
        parent_id = obj['id']

        # Construct the URL with the parent parameter
        url = f"https://www.olx.in/api/locations?parent={parent_id}&hideAddressComponents=true&lang=en-IN"

        # Make the GET request with the custom headers
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response as JSON
            json_data = response.json()

            # Get the 'data' key from the response and append it to response_data
            response_data.extend(json_data.get('data', []))
        else:
            print(f"Request failed with status code {response.status_code}")

    # Save the response data to a file
    with open(write_file_name, 'w') as file:
        json.dump(response_data, file)

    index = write_file_name.find('.')
    if index != -1:
        type = write_file_name[:index]
    print(f"All {type} data saved to '{write_file_name}' file.")

""" 
Begin fetching cities
"""
fetch_with_parents("states.json", "cities.json")

""" 
Begin fetching neighbourhoods
"""
fetch_with_parents("cities.json", "neighbourhoods.json")
