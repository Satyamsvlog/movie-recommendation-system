
import streamlit as st
import pickle
import pandas as pd

# Load movie data and similarity
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
    return recommended_movies

st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Choose a movie to get similar recommendations:",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.write("### Recommended Movies:")
    for i, title in enumerate(recommendations, 1):
        st.write(f"{i}. {title}")
