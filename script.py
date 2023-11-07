import requests
import streamlit as st
import streamlit_functions

# ------------------------- STREAMLIT STARTS -------------------------

st.title("Proof Interview - OMDB API")

selected_option = st.radio("Choose an option:", 
                        ["Search by ID or Movie Name", "Search by Keyword", "Display Poster by ID or Movie Name"])

# tt3896198 --> guardians galaxy
input = st.text_input("Enter a movie title or an ID or a keyword to search :\n")

if selected_option == "Search by ID or Movie Name":
    selected_payload_type = st.radio("Choose payload type:", 
                            ["JSON", "XML"])
    st.write(f"Returning the {selected_payload_type} payload retrieved from OMDB API : \n" )
    streamlit_functions.fetch_data(input, selected_payload_type)

elif selected_option == "Search by Keyword":
    selected_payload_type = st.radio("Choose payload type:", 
                        ["JSON", "XML"])
    st.write("Returning all movie names with specified keyword :\n")
    streamlit_functions.fetch_by_keyword(input, selected_payload_type)

elif selected_option == "Display Poster by ID or Movie Name":
    st.write("Returning Movie Poster : \n")
    streamlit_functions.fetch_poster(input)

