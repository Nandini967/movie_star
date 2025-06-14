# 🎬 Movie Recommender System using Streamlit

Welcome to the **Movie Recommender System** – a web application that helps users find movie suggestions based on their preferences for **Genre**, **Language**, and **Theme**. Built using **Streamlit** and a basic **Machine Learning model (KNN)**, this project demonstrates a clean UI, simple logic, and customizable design.

---

## 🌐 Demo

![image](https://github.com/user-attachments/assets/c01d3fdc-68ef-4eea-b680-e3f9e7397890)


## 🧠 How It Works

This app allows users to:

1. Select a **Genre** (e.g., Action, Comedy, Drama).
2. Choose a **Language** (e.g., English, Hindi, Bengali).
3. Pick a **Theme** (e.g., Love, Friendship, Patriotism).

💡 Once the preferences are selected, the system searches for exact matches in a movie dataset. If an exact match is found, it shows the top results. If not, it falls back to a similarity-based search using **K-Nearest Neighbors (KNN)** with **OneHotEncoding** of categorical features.

---

## 📸 Features

- 🎭 Filter movies based on Genre, Language, and Theme
- 🎯 Instant recommendations via button click
- 🖼️ Custom background and stylized UI using CSS
- 🤖 Fallback logic using machine learning (KNN) when exact match is not available
- 🔁 Easily extendable dataset and logic

---

## 🧾 Dataset

Located at: `data/movies.csv`

**Columns:**
- `Movie Name`
- `Genre`
- `Language`
- `Theme`

Example row:
```csv
Movie Name,Genre,Language,Theme
3 Idiots,Comedy,Hindi,Friendship
```

---

## 📂 Project Structure

```bash
movie_recommender/
│
├── app.py                   # Main Streamlit frontend
├── recommender.py           # ML logic for filtering and fallback recommendations
├── utils.py                 # Formatting utility
├── data/
│   └── movies.csv           # Movie dataset
├── static/
│   └── background.jpg       # Background image
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---
## 🚀 Installation and Usage

### 1. Clone the repository
```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run app.py
```

---

## 📱 User Flow

1. Launch the app in your browser after running the command above.
2. A beautiful interface with a background image appears.
3. Select your preferences from the dropdown menus:
    - **Genre**
    - **Language**
    - **Theme**
4. Click on **🍿 Recommend Movies**.
5. 🎬 The app will display 1–3 recommended movies that match your taste.
6. If no exact match exists, it will suggest similar movies using machine learning.

---

## 🛠️ Built With

- **Python 3.x**
- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [pandas](https://pandas.pydata.org/)
- HTML + CSS for UI styling

---

## 🎯 Future Enhancements

- Add movie posters and trailers
- Include ratings and year of release
- Add partial match filtering (not case-sensitive, fuzzy matching)
- User authentication & history tracking
- API integration for dynamic datasets (e.g., TMDB)

---


## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🌟 Show Your Support

If you found this helpful, give it a ⭐ on GitHub and share it with friends!




