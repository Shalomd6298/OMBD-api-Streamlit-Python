
import requests
import xml.etree.ElementTree as ET

# Make an API request and get the response
api_url = " "  # Replace with your API URL
response = requests.get(api_url)


if response.status_code == 200:
    xml_data = response.text
    
    root = ET.fromstring(xml_data)
    print(f"Total Results: {root.get('totalResults')}")
    print()
    
    for result in root.findall("result"):
        title = result.get("title")
        year = result.get("year")
        imdb_id = result.get("imdbID")
        poster_link = result.get("poster")

        print(f"Title: {title}")
        print(f"Year: {year}")
        print(f"IMDb ID: {imdb_id}")
        print(f"Poster URL: {poster_link}")
        print()
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    xml_data = None


