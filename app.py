import streamlit as st
import pickle
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64
from tmdb_app import get_movie_data_by_language, get_movie_by_title, extract_movie_features
from sklearn.exceptions import NotFittedError

# --- Set Background Image ---
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/jpg;base64,%s");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Set the background image
set_png_as_page_bg('wallpaper movie.jpg')

# Load model with feature names handling
try:
    with open("model/rating_model.pkl", "rb") as f:
        model = pickle.load(f)
    # Store feature names if available
    model_feature_names = getattr(model, 'feature_names_in_', None)
except (FileNotFoundError, NotFittedError, pickle.UnpicklingError) as e:
    st.error(f"Error loading model: {str(e)}")
    st.stop()

# Page configuration
st.set_page_config(
    page_title="🎬 Movie Rating Predictor", 
    layout="wide",
    page_icon="🎥"
)

# Custom CSS
st.markdown("""
<style>
    .main .block-container {
        background-color: rgba(14, 17, 23, 0.85);
        padding: 2rem;
        border-radius: 15px;
        backdrop-filter: blur(5px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    .header {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #FF4B4B !important;
        text-shadow: 2px 2px 4px #000000;
    }
    p, .stMarkdown, .stAlert {
        color: white !important;
        text-shadow: 1px 1px 2px black;
    }
    .metric-card {
        background: rgba(30, 32, 36, 0.9) !important;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
        border-left: 4px solid #FF4B4B;
        backdrop-filter: blur(2px);
    }
    .stSelectbox, .stButton>button {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border-radius: 10px;
        border: 1px solid #FF4B4B;
    }
    .js-plotly-plot .plotly, .js-plotly-plot .plotly div {
        background: rgba(14, 17, 23, 0.8) !important;
    }
    .footer {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1.5rem;
    }
    .success-box {
        background: rgba(0, 204, 150, 0.2);
        border: 2px solid #00CC96;
        backdrop-filter: blur(5px);
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header">
    <h1 style='text-align:center;'>🎥 Movie Rating Prediction Dashboard</h1>
</div>
""", unsafe_allow_html=True)

# Language selector
col1, col2 = st.columns(2)
with col1:
    language = st.selectbox("🌐 Choose Movie Language", ["Hindi", "English", "Bengali"])
with col2:
    movies = get_movie_data_by_language(language)
    movie_titles = [m["title"] for m in movies]
    selected_title = st.selectbox("🎬 Choose a Movie Title", movie_titles)

if selected_title:
    selected_movie = get_movie_by_title(language, selected_title)
    
    if selected_movie:
        # Extract movie data
        actor = selected_movie.get("actor", "Unknown")
        director = selected_movie.get("director", "Unknown")
        budget_crore = round(selected_movie.get("budget", 0) / 1e7, 2)
        popularity = selected_movie.get("popularity", 0.0)
        genre = selected_movie.get("genre", "Unknown")
        
        # Display movie info in cards
        st.markdown("### 🎭 Movie Details")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3 style='color:#FF4B4B;'>🎤 Actor</h3>
                <p style='font-size:18px;'>{actor}</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3 style='color:#FF4B4B;'>🎬 Director</h3>
                <p style='font-size:18px;'>{director}</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <h3 style='color:#FF4B4B;'>💰 Budget</h3>
                <p style='font-size:18px;'>₹{budget_crore} Cr</p>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <h3 style='color:#FF4B4B;'>🎭 Genre</h3>
                <p style='font-size:18px;'>{genre}</p>
            </div>
            """, unsafe_allow_html=True)

        # Predict button
        if st.button("🎯 Predict Rating", use_container_width=True):
            with st.spinner("🔮 Predicting rating..."):
                try:
                    input_data = extract_movie_features(selected_movie)
                    
                    # Handle feature names warning
                    if model_feature_names is not None:
                        input_df = pd.DataFrame([input_data], columns=model_feature_names)
                        predicted_rating = model.predict(input_df)[0]
                    else:
                        predicted_rating = model.predict([input_data])[0]
                    
                    # Save history
                    if "history" not in st.session_state:
                        st.session_state.history = []
                    st.session_state.history.append({
                        "Title": selected_title,
                        "Budget": budget_crore,
                        "Popularity": popularity,
                        "Genre": genre,
                        "Actor": actor,
                        "Director": director,
                        "Rating": round(predicted_rating, 2)
                    })
                    
                    # Success message
                    st.markdown(f"""
                    <div class="success-box">
                        <h2 style='color:#FF4B4B;'>⭐ Predicted Rating: {round(predicted_rating, 2)}/10 ⭐</h2>
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                    
                    # Show rating distribution
                    st.markdown("### 📊 Rating Distribution")
                    fig = go.Figure()
                    fig.add_trace(go.Indicator(
                        mode="number+gauge",
                        value=predicted_rating,
                        domain={'x': [0.1, 1], 'y': [0, 1]},
                        title={'text': "Predicted Rating"},
                        gauge={
                            'shape': "bullet",
                            'axis': {'range': [0, 10]},
                            'threshold': {
                                'line': {'color': "red", 'width': 2},
                                'thickness': 0.75,
                                'value': 6.5},
                            'steps': [
                                {'range': [0, 4], 'color': "red"},
                                {'range': [4, 7], 'color': "orange"},
                                {'range': [7, 10], 'color': "green"}],
                            'bar': {'color': "darkblue"}}))
                    st.plotly_chart(fig, use_container_width=True)
                
                except Exception as e:
                    st.error(f"Prediction failed: {str(e)}")

# Dashboard
if "history" in st.session_state and st.session_state.history:
    df_hist = pd.DataFrame(st.session_state.history)
    
    # Prepare data for visualizations
    numeric_cols = ["Budget", "Popularity", "Rating"]
    df_plot = df_hist.copy()
    df_plot[numeric_cols] = df_plot[numeric_cols].apply(pd.to_numeric, errors='coerce')
    df_plot = df_plot.dropna(subset=numeric_cols)
    
    if not df_plot.empty:
        st.markdown("## 📋 Prediction History & Analytics")
        
        # Key metrics
        st.markdown("### 📈 Key Metrics")
        avg_rating = df_plot["Rating"].mean()
        max_rating = df_plot["Rating"].max()
        total_budget = df_plot["Budget"].sum()
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("📊 Total Predictions", len(df_plot))
        m2.metric("⭐ Average Rating", f"{avg_rating:.1f}/10")
        m3.metric("🏆 Highest Rating", f"{max_rating:.1f}/10")
        m4.metric("💰 Total Budget", f"₹{total_budget:.1f} Cr")
        
        # Main charts in tabs
        tab1, tab2, tab3 = st.tabs(["📈 Rating Analysis", "💰 Budget Analysis", "🎭 Genre Analysis"])
        
        with tab1:
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### Rating Distribution")
                fig_hist = px.histogram(
                    df_plot, 
                    x="Rating",
                    nbins=10,
                    color_discrete_sequence=["#FF4B4B"],
                    marginal="box"
                )
                st.plotly_chart(fig_hist, use_container_width=True)
            
            with col2:
                st.markdown("### Rating Trend Over Time")
                df_plot["Prediction #"] = range(1, len(df_plot)+1)
                fig_line = px.line(
                    df_plot,
                    x="Prediction #",
                    y="Rating",
                    markers=True,
                    color_discrete_sequence=["#00CC96"],
                    title="Your Rating Prediction History"
                )
                fig_line.update_traces(line=dict(width=4))
                st.plotly_chart(fig_line, use_container_width=True)
        
        with tab2:
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### Budget vs Rating")
                fig_scatter = px.scatter(
                    df_plot,
                    x="Budget",
                    y="Rating",
                    size="Popularity",
                    color="Genre",
                    hover_name="Title",
                    color_discrete_sequence=px.colors.qualitative.Vivid
                )
                st.plotly_chart(fig_scatter, use_container_width=True)
            
            with col2:
                st.markdown("### Budget Distribution by Genre")
                fig_box = px.box(
                    df_plot,
                    x="Genre",
                    y="Budget",
                    color="Genre",
                    points="all"
                )
                st.plotly_chart(fig_box, use_container_width=True)
        
        with tab3:
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### Genre Popularity")
                genre_counts = df_plot["Genre"].value_counts().reset_index()
                genre_counts.columns = ["Genre", "Count"]
                fig_bar = px.bar(
                    genre_counts,
                    x="Genre",
                    y="Count",
                    color="Genre",
                    text="Count",
                    color_discrete_sequence=px.colors.qualitative.Pastel
                )
                st.plotly_chart(fig_bar, use_container_width=True)
            
            with col2:
                st.markdown("### Genre Rating Performance")
                fig_violin = px.violin(
                    df_plot,
                    x="Genre",
                    y="Rating",
                    color="Genre",
                    box=True,
                    points="all"
                )
                st.plotly_chart(fig_violin, use_container_width=True)
        
        # Correlation heatmap
        if len(df_plot) >= 2:
            st.markdown("### 🔥 Feature Correlation")
            corr_matrix = df_plot[numeric_cols].corr()
            
            fig_heat = go.Figure(
                data=go.Heatmap(
                    z=corr_matrix.values,
                    x=corr_matrix.columns,
                    y=corr_matrix.columns,
                    colorscale="Viridis",
                    hoverongaps=False,
                    text=corr_matrix.round(2).values,
                    texttemplate="%{text}",
                    zmin=-1,
                    zmax=1
                )
            )
            fig_heat.update_layout(
                title="Correlation Between Movie Features",
                xaxis_title="Features",
                yaxis_title="Features"
            )
            st.plotly_chart(fig_heat, use_container_width=True)
        else:
            st.warning("Need at least 2 predictions to show correlation")

        # Download button
        csv = df_hist.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Prediction History",
            data=csv,
            file_name='movie_rating_predictions.csv',
            mime='text/csv',
        )

# Footer
st.markdown("""
<div class="footer">
    <p style='text-align:center; color:#FF4B4B;'>🚀 Created by Srijan Roy | Powered by Streamlit</p>
</div>
""", unsafe_allow_html=True)