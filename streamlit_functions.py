import requests
import streamlit as st
import xml.etree.ElementTree as ET

# configs -->
api_key = '< enter your api key >'

def fetch_data(input, selected_payload_type):
    call_type = 'i'
    title = input
    url = f"https://www.omdbapi.com/?{call_type}={title}&r={selected_payload_type}&apikey={api_key}"

    res = requests.get(url)

    if(res.status_code == 200):
        if(selected_payload_type == 'JSON'):
            data = res.json()
            st.write(data)
        else:
            xml_data = res.text
            root = ET.fromstring(xml_data)
            st.write(f"Total Results: {root.get('response')}\n")
            
            for result in root.findall("movie"):
                title = result.get("title")
                year = result.get("year")
                imdb_id = result.get("imdbID")
                poster_link = result.get("poster")

                st.header(f"Title: {title}")
                st.header(f"Year: {year}")
                st.header(f"IMDb ID: {imdb_id}")
                st.header(f"Poster URL: {poster_link}\n")

    else :
        st.error(f"Failed to get the data due to an error. Status code: {res.status_code}")


def fetch_by_keyword(input, selected_payload_type):
    call_type = 's'
    title = input
    url = f"https://www.omdbapi.com/?{call_type}={title}&r={selected_payload_type}&apikey={api_key}"

    st.write(url)
    res = requests.get(url)

    if(res.status_code == 200):
        if(selected_payload_type == 'JSON'):
            data = res.json()
            t = [n for n in data['Search']]
            st.write(t)
        else:
            xml_data = res.text
            root = ET.fromstring(xml_data)
            st.write(f"Total Results: {root.get('totalResults')}\n")
            
            for result in root.findall("result"):
                title = result.get("title")
                year = result.get("year")
                imdb_id = result.get("imdbID")
                poster_link = result.get("poster")

                st.header(f"Title: {title}")
                st.write(f"Year: {year}")
                st.write(f"IMDb ID: {imdb_id}")
                st.write(f"Poster URL: {poster_link}\n")
        
    else:
        st.error(f"Failed to get the data due to an error. Status code: {res.status_code}")


def fetch_poster(input):
    call_type = 'i'
    title = input
    url = f"https://www.omdbapi.com/?{call_type}={title}&apikey={api_key}"

    res = requests.get(url)

    if(res.status_code == 200):
        data = res.json()
        movie_name = data['Title']
        poster_link = data['Poster']
        st.write(poster_link)
        
        # Display the image
        st.image(poster_link, caption=movie_name)
    else:
        st.error(f"Failed to get the data due to an error. Status code: {res.status_code}")