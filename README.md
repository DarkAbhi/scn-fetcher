# OLX API States, Cities, Neighbourhood fetcher

This Python script fetches all the states, cities, and neighborhoods in India using OLX's API. It makes HTTP GET requests with custom headers to retrieve the data. Please ensure that the user-agent in the request headers is set to 'PostmanRuntime/7.32.2' as the server may block requests that do not originate from a valid browser or mobile application.

## Prerequisites

To run this code, you need to have Python installed on your system. Additionally, make sure to install the `requests` library using pip:

```
pip install requests
```

Usage

1. Clone this repository or download the script directly.

2. Open the terminal or command prompt and navigate to the directory containing the script.

3. Run the following command to execute the script:

```
python scrape_scn.py
```

1. The script will fetch all the states and save the data to a file named states.json. Then, it will proceed to fetch all the cities using the states' data and save it to cities.json. Finally, it will fetch all the neighborhoods using the cities' data and save it to neighbourhoods.json.

Please note that the script assumes the presence of the states.json file in the same directory.

Please note that due to server limitations, there are chances of encountering request errors with a 503 HTTP status code. In such cases, you can try running the script again after some time.

### License

This project is licensed under the MIT License.

```
Feel free to modify the README according to your preferences or add any additional information you want to include.
```