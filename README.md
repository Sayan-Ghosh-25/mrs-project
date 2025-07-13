# 🎬 Movie Recommender App

Welcome to your **Personalized Movie Recommendation System**!  
This web app suggests movies similar to your selected favorite, using content-based filtering and cosine similarity.

🔗 **Live App**: [Click Here To Try It Out](https://movies-recommendation-sg25.streamlit.app)

---

## 🚀 Features

- 🔍 Type any movie name & select the movie from a dropdown list of 4800+ titles.
- 🤖 View top 10 similar movies based on metadata similarity.
- 🖼️ Posters fetched live from **The Movie Database (TMDB)** API.
- ☁️ App runs entirely in the browser — no installation needed.

---

## 🧠 How It Works

- Built with **Streamlit**
- Movie data and similarity scores preprocessed and stored in:
  - `Movies.pkl`: metadata (title, tags, ID)
  - `Similarity.pkl`: cosine similarity matrix
  - When a movie is selected, it finds the top 10 similar movies using cosine similarity.

---

## 📦 Tech Stack

- `streamlit`
- `pandas`, `numpy`
- `scikit-learn`
- `requests` (for poster fetching)
- `gdown` (for downloading the files from Drive)

---

## 🧾 License

This project is for educational/demo purposes.  
Data sourced from [TMDB](https://www.themoviedb.org/), used under their API terms.

---

## 🙋‍♂️ Author

**Sayan Ghosh**  
Feel Free To Connect Me On [LinkedIn](https://www.linkedin.com/in/sayan-ghosh25) or Contribute To This Project 😎

