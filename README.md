# 🎬 Movie Rating Prediction App

**Predict IMDb ratings of movies using machine learning and real-time metadata from TMDb!**  
This is an end-to-end intelligent system that forecasts a movie's potential rating based on its **cast, director, genre, budget, popularity, and language**.

![App Screenshot](wallpaper%20movie.jpg)

---

## 🚀 Live Demo

👉 [Click here to try the app](https://your-streamlit-link.streamlit.app)

---

## 📌 Features

- 🎥 Predict IMDb-like rating for movies (Hindi, English, Bengali)
- 🧠 Trained on real-world movie data using **Gradient Boosting**
- 🌐 Fetches live data using **TMDb API**
- 📊 Real-time interactive dashboards (Plotly)
- 💰 Analyzes impact of budget, genre, cast & more
- 💾 Session-based history tracking with CSV export
- 🎨 Beautiful responsive UI using Streamlit & custom CSS

---

## 🧠 Tech Stack

| Area               | Tools Used |
|--------------------|------------|
| ML Models          | `scikit-learn`, `GradientBoostingClassifier`, `SMOTE` |
| Data Visualization | `plotly`, `pandas` |
| Web App            | `Streamlit` |
| API Integration    | `TMDb API`, `requests` |
| Deployment         | `Streamlit Cloud` |
| Styling            | `CSS`, `base64` background |

---

## 🧪 Input Features

The model uses the following:
- Genre (e.g., Action, Drama)
- Budget (in INR ₹)
- Language (Hindi, English, Bengali)
- Popularity (from TMDb)
- Actor name
- Director name

---

## 📂 Project Structure

movie-rating-predictor/
├── app.py # Main Streamlit app
├── model/
│ └── rating_model.pkl # Trained ML model
├── tmdb_app/
│ └── tmdb_api.py # API call functions
├── static_movies/
│ ├── hindi_movies.json
│ ├── english_movies.json
│ └── bengali_movies.json
├── wallpaper movie.jpg # Background image
├── requirements.txt # Python dependencies
├── README.md # Project info
└── .streamlit/
└── secrets.toml # API key config (not pushed)

yaml
Copy
Edit

---

## 🛠️ Setup Instructions

1. **Clone the Repo**
   ```bash
   git clone https://github.com/SrijanRoy12/movie-rating-predictor.git
   cd movie-rating-predictor
Install Requirements

bash
Copy
Edit
pip install -r requirements.txt
Add TMDb API Key
Create .streamlit/secrets.toml:

toml
Copy
Edit
[tmdb]
api_key = "your_tmdb_api_key_here"
Run the App

bash
Copy
Edit
streamlit run app.py
📈 Sample Output
⭐ Predicted rating (e.g., 7.6 / 10)

📊 Budget vs Rating visualizations

🎭 Genre-wise trends

🔥 Correlation heatmap of features

🎓 Project Context
This app was built as my final project with InternPe to demonstrate:

Machine learning deployment

API usage

Real-time dashboard analytics

Full product lifecycle from training → app → deployment

📁 GitHub Repository
🔗 https://github.com/SrijanRoy12/movie-rating-predictor

🤝 Connect with Me
📧 Email: srijanroy.dev@gmail.com
🌐 Portfolio: Coming Soon
💼 LinkedIn: linkedin.com/in/srijanroy12

🏁 Future Enhancements
📽️ Add poster + trailer preview from TMDb

🧠 Deep learning-based rating model

🌎 Support more languages & global datasets

🧩 User login and saved prediction history

