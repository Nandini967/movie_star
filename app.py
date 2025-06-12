import streamlit as st
import base64
from recommender import MovieRecommender
from utils import format_movie_list

# Load ML model
recommender = MovieRecommender()

# Set page config
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")
st.title("🎥 Movie Recommender System")

# ---------- Background Image ----------
def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(image_file):
    base64_img = get_base64(image_file)
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{base64_img}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
    """, unsafe_allow_html=True)

# Set background
set_background("static/background.jpg")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    .big-font {
        font-size: 16px !important;
        font-weight: 600;
        margin-bottom: 10px;
        color: #000000;
    }

    .black-font {
        font-size: 26px !important;
        font-weight: 700;
        margin-bottom: 10px;
        color: #000000;
    }

    .tight-label {
        font-size: 18px !important;
        font-weight: 600;
        color: black;
        margin-bottom: 0px !important;
        padding-bottom: 0px !important;
        line-height: 1 !important;
    }

    /* Reduce vertical spacing above/below selectbox */
    .stSelectbox > div:first-child {
        margin-bottom: 0px !important;
        padding-bottom: 0px !important;
    }

    div[data-baseweb="select"] {
        margin-top: -8px !important;
    }

    div[data-baseweb="select"] > div {
        font-size: 18px !important;
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- UI Section ----------
st.markdown("<p class='black-font'>Select your preferences to get movie suggestions:</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='tight-label'>🎭 Genre</div>", unsafe_allow_html=True)
    selected_genre = st.selectbox(" ", sorted(recommender.df['Genre'].unique()), key="genre")

with col2:
    st.markdown("<div class='tight-label'>🗣️ Language</div>", unsafe_allow_html=True)
    selected_language = st.selectbox("  ", sorted(recommender.df['Language'].unique()), key="language")

with col3:
    st.markdown("<div class='tight-label'>🎯 Theme</div>", unsafe_allow_html=True)
    selected_theme = st.selectbox("   ", sorted(recommender.df['Theme'].unique()), key="theme")

# ---------- Recommendation ----------
if st.button("🍿 Recommend Movies"):
    st.subheader("Recommended Movies:")
    results = recommender.recommend(selected_genre, selected_language, selected_theme, top_k=3)

    if results:
        for movie in results:
            st.markdown(f"<div class='big-font'>🎬 {movie}</div>", unsafe_allow_html=True)
    else:
        st.warning("No recommendations found for your selected preferences.")
