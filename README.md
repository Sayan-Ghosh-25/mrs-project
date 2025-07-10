# 🎬 Movie Recommender App

Welcome to your **personalized movie recommendation system**!  
This web app suggests movies similar to your selected favorite, using content-based filtering and cosine similarity.

🔗 **Live App**: [Click here to try it out](https://DivineSayan-movie-recommender-app.hf.space/)  
📦 **Dataset Repo**: [DivineSayan/Recommendation-System](https://huggingface.co/datasets/DivineSayan/Recommendation-System)

---

## 🚀 Features

- 🔍 Select any movie from a dropdown list of 4800+ titles.
- 🤖 View top 10 similar movies based on metadata similarity.
- 🖼️ Posters fetched live from **The Movie Database (TMDB)** API.
- ☁️ App runs entirely in the browser — no installation needed.

---

## 🧠 How It Works

- Built with **Streamlit**
- Movie data and similarity scores preprocessed and stored in:
  - `Movies.pkl`: metadata (title, tags, ID)
  - `Similarity.pkl`: cosine similarity matrix
- These files are hosted on the Hugging Face Hub and downloaded dynamically using the `huggingface_hub` package.
- When a movie is selected, it finds the top 10 similar movies using cosine similarity.

---

## 📦 Tech Stack

- `streamlit`
- `pandas`, `numpy`
- `scikit-learn`
- `requests` (for poster fetching)
- `huggingface_hub` (for dataset integration)

---

## 🧾 License

This project is for educational/demo purposes.  
Data sourced from [TMDB](https://www.themoviedb.org/), used under their API terms.

---

## 🙋‍♂️ Author

**Sayan Ghosh**  
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/sayan-ghosh25) or contribute to this project!

