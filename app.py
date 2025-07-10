import os
import requests
import streamlit as st
import pandas as pd
import pickle

# ─── Download Helper ────────────────────────────────────────────────────────────
def download_if_missing(url: str, filename: str):
    """Download `filename` from `url` if not already present on disk."""
    if not os.path.exists(filename):
        with st.spinner(f"Downloading {filename}..."):
            resp = requests.get(url, stream=True)
            resp.raise_for_status()
            with open(filename, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

# ─── Google Drive Direct-Download URLs ────────────────────────────────────────
MOVIES_URL     = "https://drive.google.com/uc?export=download&id=1Bze3ZvzvedPYg_Yk--8tr_hSJUrJzT29"
SIMILARITY_URL = "https://drive.google.com/uc?export=download&id=13AQel0rbUjkW-UU-q9YawRUQ2BaRFRnH"

# ─── Ensure Pickles Are Present ────────────────────────────────────────────────
download_if_missing(MOVIES_URL, "Movies.pkl")
download_if_missing(SIMILARITY_URL, "Similarity.pkl")

# ─── Load Data ────────────────────────────────────────────────────────────────
@st.cache_data
def load_movies():
    with open("Movies.pkl", "rb") as f:
        movies_dict = pickle.load(f)
    return pd.DataFrame(movies_dict)

@st.cache_data
def load_similarity():
    with open("Similarity.pkl", "rb") as f:
        return pickle.load(f)

movies     = load_movies()
similarity = load_similarity()

# ─── TMDB Poster & IMDb Link Fetchers ─────────────────────────────────────────
def fetch_poster(movie_id: int) -> str:
    """Fetch poster URL from TMDB API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": "8265bd1679663a7ea12ac168da84d2e8", "language": "en-US"}
    data = requests.get(url, params=params).json()
    return f"https://image.tmdb.org/t/p/w500{data.get('poster_path','')}"

def fetch_imdb_link(movie_id: int) -> str:
    """Fetch IMDb URL via TMDB external IDs."""
    url    = f"https://api.themoviedb.org/3/movie/{movie_id}/external_ids"
    params = {"api_key": "8265bd1679663a7ea12ac168da84d2e8"}
    data   = requests.get(url, params=params).json()
    imdb   = data.get("imdb_id","")
    return f"https://www.imdb.com/title/{imdb}/" if imdb else "#"

# ─── Suggest & Recommend Logic ────────────────────────────────────────────────
def get_suggestions(query: str, titles: pd.Series, limit: int = 4):
    q = query.strip().lower()
    return [t for t in titles if q in t.lower()][:limit]

def recommend(selected_title: str, movies_df: pd.DataFrame, sim_mat):
    idx  = movies_df[movies_df['title'].str.lower() == selected_title.lower()].index[0]
    sims = sorted(list(enumerate(sim_mat[idx])), key=lambda x: x[1], reverse=True)[1:11]
    names, posters, links = [], [], []
    for mi, _ in sims:
        row = movies_df.iloc[mi]
        names.append(row.title)
        with st.spinner("Cooking your recommendations…"):
            posters.append(fetch_poster(row.id))
            links.append(fetch_imdb_link(row.id))
    return names, posters, links

# ─── Streamlit UI ─────────────────────────────────────────────────────────────
st.title('🎬 Your Personalised Movie Recommender')
st.markdown("**Search for a movie to get similar**")

search_query = st.text_input(
    label="💡 *Tips: Always use the exact spellings*",
    placeholder="Type the movie name…"
)

# Live suggestions
suggestions = get_suggestions(search_query, movies['title']) if search_query else []
selected_movie = st.selectbox('Did you mean…?', suggestions) if suggestions else None

if st.button('Show Recommendations') and selected_movie:
    names, posters, links = recommend(selected_movie, movies, similarity)

    # First row
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"[{names[i]}]({links[i]})", unsafe_allow_html=True)
            st.image(posters[i])

    # Second row
    cols = st.columns(5)
    for i, col in enumerate(cols, start=5):
        with col:
            st.markdown(f"[{names[i]}]({links[i]})", unsafe_allow_html=True)
            st.image(posters[i])