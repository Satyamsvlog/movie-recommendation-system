🎬 Movie Recommendation System

This is a basic Movie Recommendation System built using Python and Streamlit. It suggests movies similar to the one you select from a dropdown. I made this project to understand how recommendation systems work and to learn how to build a simple web app using Python.

📌 What This Project Does

I select a movie from the list.
It shows 5 similar movies based on content (like genre, description, etc.).
It uses a similarity score to find and recommend movies that are close to my choice.
🧰 Tools and Technologies Used

Python
Pandas for data handling
Scikit-learn for building the recommendation logic
Streamlit for creating the user interface
📁 Project Files

| File | Description |

'app.py' ( The main Streamlit app that runs the website ) 'movies.csv' ( The dataset containing movie names and details ) 'ratings.csv' ( (Optional) Used earlier for extra insights ) 'movies.pkl' ( Saved data after processing the movies ) 'similarity.pkl' (Matrix that holds similarity scores between movies )

🚀 How to Run the Project

Step 1: Install the required packages

pip install streamlit pandas scikit-learn
streamlit run app.py