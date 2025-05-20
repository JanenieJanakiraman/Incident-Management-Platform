# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# from collections import Counter
# from wordcloud import WordCloud
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# import string

# # Download NLTK data (first time only)
# nltk.download("stopwords")
# nltk.download("wordnet")

# # Initialize Stopwords & Lemmatizer
# stop_words = set(stopwords.words("english"))
# lemmatizer = WordNetLemmatizer()

# @st.cache_data
# def load_data():
#     file_path = "/Users/hardikchhipa/Desktop/Data_Manipulations_Projects/Autodesk/Incident/data.xlsx"
    
#     df = pd.read_excel(file_path, parse_dates=["Opened At", "Resolved Date"])
#     df.fillna("", inplace=True)

#     if "Resolved Time (days)" not in df.columns:
#         df["Resolved Time (days)"] = (df["Resolved Date"] - df["Opened At"]).dt.days

#     return df

# def clean_text(text):
#     """Cleans text by removing stopwords, punctuation, and applying lemmatization."""
#     if isinstance(text, str):  
#         text = text.lower().translate(str.maketrans("", "", string.punctuation))  # Lowercase & remove punctuation
#         words = text.split()
#         words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]  # Remove stopwords & lemmatize
#         return words
#     return []

# def get_most_frequent_words(text_column, n=20):
#     """Returns the top N most frequent words."""
#     all_words = [word for sublist in text_column.dropna() for word in sublist]
#     word_freq = Counter(all_words)
#     return word_freq.most_common(n)

# df = load_data()

# # Apply text cleaning to 'Close Notes' and 'Short Descriptions'
# df["cleaned_close_notes"] = df["Close Notes"].apply(clean_text)
# df["cleaned_short_desc"] = df["Short Description"].apply(clean_text)

# st.title("📊 Most Frequent Words in Close Notes & Short Descriptions")

# # Compute word frequencies
# close_notes_freq = get_most_frequent_words(df["cleaned_close_notes"])
# short_desc_freq = get_most_frequent_words(df["cleaned_short_desc"])

# words_close, freq_close = zip(*close_notes_freq) if close_notes_freq else ([], [])
# words_desc, freq_desc = zip(*short_desc_freq) if short_desc_freq else ([], [])

# # 🎨 PLOTLY BAR CHARTS (Side-by-side)
# fig = make_subplots(
#     rows=1, cols=2,
#     subplot_titles=("Top Words in Close Notes", "Top Words in Short Descriptions"),
#     horizontal_spacing=0.2  # ⬅️ Increase this value to widen the gap
# )

# fig.add_trace(go.Bar(
#     x=freq_close,
#     y=words_close,
#     orientation="h",
#     marker=dict(color=freq_close, colorscale="magma"),
#     name="Close Notes"
# ), row=1, col=1)

# fig.add_trace(go.Bar(
#     x=freq_desc,
#     y=words_desc,
#     orientation="h",
#     marker=dict(color=freq_desc, colorscale="viridis"),
#     name="Short Descriptions"
# ), row=1, col=2)

# fig.update_layout(
#     title="Bar Graph Between Close Notes & Short Descriptions",
#     template="plotly_dark",
#     height=600,
#     width=1200,
#     showlegend=False
# )

# st.plotly_chart(fig)

# col1, col2 = st.columns(2)

# # 🎨 WORD CLOUDS
# def generate_wordcloud(words):
#     if not words:
#         return None
#     wordcloud = WordCloud(width=800, height=500, background_color="black", colormap="plasma").generate(" ".join(words))
#     return wordcloud.to_array()

# with col1:
#     st.write("### 🌟 Close Notes Word Cloud")
#     frequent_close_notes = get_most_frequent_words(df["cleaned_close_notes"])
#     st.write(frequent_close_notes)
#     close_words = [word for sublist in df["cleaned_close_notes"] for word in sublist]
#     wordcloud_close = generate_wordcloud(close_words)
#     if wordcloud_close is not None:
#         st.image(wordcloud_close, use_container_width=True)

# with col2:
#     st.write("### 🔥 Short Descriptions Word Cloud")
#     frequent_short_desc = get_most_frequent_words(df["cleaned_short_desc"])
#     st.write(frequent_short_desc)
#     short_words = [word for sublist in df["cleaned_short_desc"] for word in sublist]
#     wordcloud_short = generate_wordcloud(short_words)
#     if wordcloud_short is not None:
#         st.image(wordcloud_short, use_container_width=True)



import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from collections import Counter
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

st.set_page_config(layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600&display=swap');
    
    * {
        font-family: 'Space Grotesk', sans-serif;
    }
    
    .main {
        background: #0f172a;
        color: #ffffff;
    }
    
    .header-card {
        background: linear-gradient(135deg, #1e3a8a 0%, #0f766e 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 4px 30px rgba(0,0,0,0.1);
    }
    
    .viz-card {
        background: rgba(30, 41, 59, 0.8);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #334155;
    }
    
    .metric-box {
        background: rgba(99, 102, 241, 0.15);
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Download NLTK data
nltk.download("stopwords")
nltk.download("wordnet")

# Initialize NLP components
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

@st.cache_data
def load_data():
    file_path = 'dataset/Incident_PreProcessed.xlsx'
    df = pd.read_excel(file_path, parse_dates=["Opened At", "Resolved Date"])
    df.fillna("", inplace=True)
    
    if "Resolved Time (days)" not in df.columns:
        df["Resolved Time (days)"] = (df["Resolved Date"] - df["Opened At"]).dt.days
    
    return df

def clean_text(text):
    """Enhanced text cleaning with emoji handling"""
    if isinstance(text, str):
        # Remove punctuation and numbers
        text = text.translate(str.maketrans('', '', string.punctuation + '0123456789'))
        # Lemmatization with POS tagging
        words = [lemmatizer.lemmatize(word) for word in text.lower().split() 
                if word not in stop_words and len(word) > 2]
        return words
    return []

def get_most_frequent_words(text_column, n=20):
    """Returns the top N most frequent words with enhanced processing"""
    # Flatten list of lists and filter out empty strings
    all_words = [word.strip() for sublist in text_column.dropna() for word in sublist if word.strip()]
    
    # Create frequency distribution with minimum length filter
    word_freq = Counter([word for word in all_words if len(word) > 2])
    
    return word_freq.most_common(n)


def generate_gradient_wordcloud(words, colormap):
    """Generate wordcloud with gradient effect"""
    if not words: return None
    wordcloud = WordCloud(
        width=800, height=500,
        background_color='#0f172a',
        colormap=colormap,
        contour_width=2,
        contour_color='#3b82f6'
    ).generate(" ".join(words))
    return wordcloud.to_array()

# Load data
df = load_data()
df["cleaned_close_notes"] = df["Close Notes"].apply(clean_text)
df["cleaned_short_desc"] = df["Short Description"].apply(clean_text)

# Page Header
st.markdown("""
    <div class="header-card">
        <h1 style='color: white; margin:0'>🔍 Text Analysis Dashboard</h1>
        <p style='color: #94a3b8; margin:0'>Deep dive into incident descriptions and notes</p>
    </div>
""", unsafe_allow_html=True)

# Key Metrics
col1, col2, col3 = st.columns(3)
with col1:
    total_words = sum(len(words) for words in df["cleaned_close_notes"])
    st.markdown(f"""
        <div class="metric-box">
            <div style='color: #94a3b8'>📝 Total Words Analyzed</div>
            <div style='color: #3b82f6; font-size:1.8rem'>{total_words:,}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    unique_words = len(set([word for sublist in df["cleaned_close_notes"] for word in sublist]))
    st.markdown(f"""
        <div class="metric-box">
            <div style='color: #94a3b8'>✨ Unique Words</div>
            <div style='color: #3b82f6; font-size:1.8rem'>{unique_words:,}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    avg_word_length = round(pd.Series([len(word) for sublist in df["cleaned_close_notes"] for word in sublist]).mean(), 1)
    st.markdown(f"""
        <div class="metric-box">
            <div style='color: #94a3b8'>📏 Avg Word Length</div>
            <div style='color: #3b82f6; font-size:1.8rem'>{avg_word_length}</div>
        </div>
    """, unsafe_allow_html=True)

# Visualization Section
with st.container():
    st.markdown('<div class="viz-card">', unsafe_allow_html=True)
    
    # Frequency Analysis
    st.markdown("### 📈 Top Word Frequency Analysis")
    
    # Get frequencies
    close_notes_freq = get_most_frequent_words(df["cleaned_close_notes"])
    short_desc_freq = get_most_frequent_words(df["cleaned_short_desc"])
    
    # Create animated bar charts
    fig = make_subplots(rows=1, cols=2, subplot_titles=(
        "🔮 Close Notes - Top Words", 
        "💡 Short Descriptions - Top Words"
    ))
    
    # Close Notes Trace
    fig.add_trace(
        go.Bar(
            x=[freq for word, freq in close_notes_freq],
            y=[word for word, freq in close_notes_freq],
            orientation='h',
            marker=dict(
                color=[freq for word, freq in close_notes_freq],
                colorscale='magma',
                line=dict(width=1, color='#3b82f6')
            ),
            name='Close Notes'
        ),
        row=1,
        col=1
    )

    # Short Descriptions Trace
    fig.add_trace(
        go.Bar(
            x=[freq for word, freq in short_desc_freq],
            y=[word for word, freq in short_desc_freq],
            orientation='h',
            marker=dict(
                color=[freq for word, freq in short_desc_freq],
                colorscale='viridis',
                line=dict(width=1, color='#3b82f6')
            ),
            name='Short Descriptions'
        ),
        row=1,
        col=2
    )
        
    fig.update_layout(
        template='plotly_dark',
        height=600,
        showlegend=False,
        hoverlabel=dict(
            bgcolor='#1e293b',
            font_size=14,
            font_color='white'
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Word Clouds Section
with st.container():
    st.markdown('<div class="viz-card">', unsafe_allow_html=True)
    st.markdown("### ☁️ Semantic Word Clouds")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🌌 Close Notes Word Cloud")
        close_words = [word for sublist in df["cleaned_close_notes"] for word in sublist]
        wc_close = generate_gradient_wordcloud(close_words, 'plasma')
        if wc_close is not None:
            st.image(wc_close, use_container_width=True)
        else:
            st.warning("Word cloud generation failed. Try again with different data.")
            st.download_button(
                "📥 Download Close Notes Words",
                "\n".join(close_words),
                "close_notes_words.txt"
            )
    
    with col2:
        st.markdown("#### 🌠 Short Descriptions Word Cloud")
        short_words = [word for sublist in df["cleaned_short_desc"] for word in sublist]
        wc_short = generate_gradient_wordcloud(short_words, 'viridis')
        if wc_close is not None:
            st.image(wc_close, use_container_width=True)
        else:
            st.warning("Word cloud generation failed. Try again with different data.")
            st.download_button(
                "📥 Download Short Desc Words",
                "\n".join(short_words),
                "short_desc_words.txt"
            )
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align:center; color:#64748b; margin: 2rem 0'>
        🚀 Developed By <a href='https://www.linkedin.com/in/hardik-chhipa-303040242/' target='_blank' style='color:#64748b; text-decoration:none; font-weight:bold;'>Hardik Chhipa</a>
    </div>
""", unsafe_allow_html=True)
