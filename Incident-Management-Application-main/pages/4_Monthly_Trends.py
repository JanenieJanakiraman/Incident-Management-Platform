# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from collections import Counter

# @st.cache_data
# def load_data():
#     file_path = '/Users/hardikchhipa/Desktop/Data_Manipulations_Projects/Incident Autodesk/dataset/Incident_PreProcessed.xlsx'
    
#     # Read the Excel file and parse date columns
#     df = pd.read_excel(file_path, parse_dates=["Opened At", "Resolved Date"])

#     # Handling missing values
#     df.fillna("", inplace=True)

#     # Compute Resolved Time (if not already present)
#     if "Resolved Time (days)" not in df.columns:
#         df["Resolved Time (days)"] = (df["Resolved Date"] - df["Opened At"]).dt.days

#     return df

# def clean_text(text):
#     """Function to clean text data by removing unwanted characters and splitting into words."""
#     if isinstance(text, str):
#         return text.lower().split()  # Simple split into words
#     return []

# def monthly_word_analysis(df, column):
#     """Generate the most frequent words per month."""
#     df["Month"] = df["Opened At"].dt.strftime("%Y-%m")
#     monthly_words = {}

#     for month in df["Month"].unique():
#         all_words = [word for sublist in df[df["Month"] == month][column].dropna() for word in sublist]
#         monthly_words[month] = Counter(all_words).most_common(10)

#     return monthly_words

# st.title("Monthly Frequent Words Analysis")

# # Sample data for visualization
# close_notes_data = {
#     "2024-09": [["issue", 2902], ["user", 2868], ["sfdc", 2652], ["order", 2598], ["solution", 2214]],
#     "2024-08": [["issue", 1734], ["sfdc", 1463], ["order", 1381], ["user", 1333], ["team", 1300]],
#     "2024-07": [["issue", 1831], ["user", 1254], ["order", 1227], ["team", 1146], ["please", 1126]],
# }
# short_desc_data = {
#     "2024-09": [["opshubinstant", 1071], ["number", 694], ["hypercare", 640], ["customers", 615], ["impacted", 579]],
#     "2024-08": [["opshubinstant", 846], ["number", 506], ["account", 460], ["access", 417], ["customers", 415]],
#     "2024-07": [["opshubinstant", 748], ["number", 509], ["access", 469], ["customers", 440], ["impacted", 402]],
# }

# # Convert JSON-like dictionary to DataFrame
# def json_to_dataframe(data):
#     records = []
#     for month, words in data.items():
#         for word, freq in words:
#             records.append({"Month": month, "Word": word, "Frequency": freq})
#     return pd.DataFrame(records)

# df_close_notes = json_to_dataframe(close_notes_data)
# df_short_desc = json_to_dataframe(short_desc_data)

# # Ensure correct month order (sorted)
# month_order = sorted(df_close_notes["Month"].unique())

# st.markdown("<br><br>", unsafe_allow_html=True)  # Adds vertical space

# # 🔹 Close Notes & Short Description Trends (Plotly)
# st.write("### 📈 Interactive Trends")

# fig_close = px.line(df_close_notes, x="Month", y="Frequency", color="Word",
#                     title="Top Words Trend in Close Notes (Interactive)",
#                     labels={"Month": "Month", "Frequency": "Word Frequency"},
#                     template="plotly_dark")

# fig_short = px.line(df_short_desc, x="Month", y="Frequency", color="Word",
#                     title="Top Words Trend in Short Descriptions (Interactive)",
#                     labels={"Month": "Month", "Frequency": "Word Frequency"},
#                     template="plotly_dark")

# st.plotly_chart(fig_close)
# st.plotly_chart(fig_short)

# st.markdown("<br><br>", unsafe_allow_html=True)  # Adds space

# # 🔹 Stacked Bar Chart (Plotly)
# st.write("### 📊 Monthly Word Distribution (Stacked Bars)")

# df_close_pivot = df_close_notes.pivot(index="Month", columns="Word", values="Frequency").fillna(0)
# df_short_pivot = df_short_desc.pivot(index="Month", columns="Word", values="Frequency").fillna(0)

# fig_bar_close = px.bar(df_close_pivot, x=df_close_pivot.index, y=df_close_pivot.columns,
#                     title="Monthly Word Distribution in Close Notes",
#                     labels={"value": "Total Frequency", "index": "Month"},
#                     template="plotly_dark")

# fig_bar_short = px.bar(df_short_pivot, x=df_short_pivot.index, y=df_short_pivot.columns,
#                     title="Monthly Word Distribution in Short Descriptions",
#                     labels={"value": "Total Frequency", "index": "Month"},
#                     template="plotly_dark")

# st.plotly_chart(fig_bar_close)
# st.plotly_chart(fig_bar_short)

# col1, col2 = st.columns(2)

# st.text("")  # Adds a small space
# st.text("")  # Adds more space

# df = load_data()

# with col1:
#     st.write("### Close Notes by Month")
#     monthly_close_notes = monthly_word_analysis(df, "cleaned_close_notes")
#     st.write(monthly_close_notes)

# with col2:
#     st.write("### Short Descriptions by Month")
#     monthly_short_desc = monthly_word_analysis(df, "cleaned_short_desc")
#     st.write(monthly_short_desc)


import streamlit as st
import pandas as pd
import plotly.express as px
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

st.set_page_config(layout="wide")
# Download NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize NLP components
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

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

@st.cache_data
def load_data():
    file_path = 'dataset/Incident_PreProcessed.xlsx'
    df = pd.read_excel(file_path, parse_dates=["Opened At", "Resolved Date"])
    df.fillna("", inplace=True)
    
    if "Resolved Time (days)" not in df.columns:
        df["Resolved Time (days)"] = (df["Resolved Date"] - df["Opened At"]).dt.days
    
    return df

def clean_text(text):
    """Enhanced text cleaning with stopword removal and lemmatization"""
    if isinstance(text, str):
        # Remove punctuation and numbers
        text = text.translate(str.maketrans('', '', string.punctuation + '0123456789'))
        # Lowercase and split
        words = text.lower().split()
        # Remove stopwords and short words
        filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
        # Lemmatize words
        lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
        return lemmatized_words
    return []

def monthly_word_analysis(df, column):
    """Generate cleaned monthly word frequencies"""
    df["Month"] = df["Opened At"].dt.strftime("%Y-%m")
    monthly_words = {}

    for month in df["Month"].unique():
        # Process text through clean_text
        all_words = [word for sublist in df[df["Month"] == month][column] for word in sublist]
        # Filter out residual stopwords and meaningless terms
        meaningful_words = [word for word in all_words if word not in ['', 'na', 'n/a']]
        monthly_words[month] = Counter(meaningful_words).most_common(10)
        
    return monthly_words

# Page Header
st.markdown("""
    <div class="header-card">
        <h1 style='color: white; margin:0'>📅 Monthly Word Trends Analysis</h1>
        <p style='color: #94a3b8; margin:0'>Track evolving patterns in incident documentation</p>
    </div>
""", unsafe_allow_html=True)

# Load data
df = load_data()

# Process text data
df["cleaned_close_notes"] = df["Close Notes"].apply(clean_text)
df["cleaned_short_desc"] = df["Short Description"].apply(clean_text)

# 🔥 Top Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
        <div class="metric-box">
            <div style='color: #94a3b8'>📆 Months Analyzed</div>
            <div style='color: #3b82f6; font-size:1.8rem'>{df['Opened At'].dt.to_period('M').nunique()}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    total_words = sum(len(words) for words in df['cleaned_close_notes'])
    st.markdown(f"""
        <div class="metric-box">
            <div style='color: #94a3b8'>📝 Total Words Tracked</div>
            <div style='color: #3b82f6; font-size:1.8rem'>{total_words:,}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    unique_words = len({word for sublist in df['cleaned_close_notes'] for word in sublist})
    st.markdown(f"""
        <div class="metric-box">
            <div style='color: #94a3b8'>✨ Unique Words</div>
            <div style='color: #3b82f6; font-size:1.8rem'>{unique_words:,}</div>
        </div>
    """, unsafe_allow_html=True)

# Interactive Trends Section
with st.container():
    st.markdown('<div class="viz-card">', unsafe_allow_html=True)
    st.markdown("### 🌟 Interactive Word Trajectories")
    
    # Create tabs for different visualizations
    tab1, tab2 = st.tabs(["📈 Dual Evolution Charts", "📊 Stacked Bars"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        # Close Notes Evolution
        with col1:
            close_notes_data = {
                "Month": ["2024-09", "2024-08", "2024-07"]*5,
                "Word": ["issue"]*3 + ["user"]*3 + ["sfdc"]*3 + ["order"]*3 + ["solution"]*3,
                "Frequency": [2902,1734,1831, 2868,1333,1254, 2652,1463,1227, 2598,1381,1146, 2214,1300,1126]
            }
            df_close = pd.DataFrame(close_notes_data)
            
            fig_close = px.line(df_close, x="Month", y="Frequency", color="Word",
                               line_shape="spline", markers=True,
                               title="<b>Close Notes Word Evolution</b>",
                               template="plotly_dark")
            fig_close.update_layout(height=400, hovermode="x unified")
            fig_close.update_traces(line_width=2, marker_size=8)
            st.plotly_chart(fig_close, use_container_width=True)

        # Short Descriptions Evolution
        with col2:
            short_desc_data = {
                "Month": ["2024-09", "2024-08", "2024-07"]*5,
                "Word": ["opshubinstant"]*3 + ["hypercare"]*3 + ["impacted"]*3 + ["customers"]*3 + ["access"]*3,
                "Frequency": [1071,846,748, 640,460,469, 579,417,402, 615,415,440, 417,460,469]
            }
            df_short = pd.DataFrame(short_desc_data)
            
            fig_short = px.line(df_short, x="Month", y="Frequency", color="Word",
                               line_shape="spline", markers=True,
                               title="<b>Short Descriptions Word Evolution</b>",
                               template="plotly_dark")
            fig_short.update_layout(height=400, hovermode="x unified")
            fig_short.update_traces(line_width=2, marker_size=8)
            st.plotly_chart(fig_short, use_container_width=True)
    
    with tab2:
        # Stacked Bar Charts
        col1, col2 = st.columns(2)
        
        with col1:
            df_close_pivot = df_close.pivot(index="Month", columns="Word", values="Frequency").fillna(0)
            fig_bar_close = px.bar(df_close_pivot, barmode="stack", 
                                  title="<b>Close Notes Word Distribution</b>",
                                  template="plotly_dark")
            fig_bar_close.update_layout(height=500)
            st.plotly_chart(fig_bar_close, use_container_width=True)
        
        with col2:
            df_short_pivot = df_short.pivot(index="Month", columns="Word", values="Frequency").fillna(0)
            fig_bar_short = px.bar(df_short_pivot, barmode="stack", 
                                  title="<b>Short Descriptions Word Distribution</b>",
                                  template="plotly_dark")
            fig_bar_short.update_layout(height=500)
            st.plotly_chart(fig_bar_short, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Monthly Breakdown Section
with st.container():
    st.markdown('<div class="viz-card">', unsafe_allow_html=True)
    st.markdown("### 📆 Monthly Word Breakdown (Enhanced Analysis)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### 🗒️ Close Notes Insights")
        monthly_close = monthly_word_analysis(df, "cleaned_close_notes")
        for month in sorted(monthly_close.keys(), reverse=True):
            with st.expander(f"📅 {month}"):
                for word, freq in monthly_close[month][:5]:
                    st.markdown(f"""
                        <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                            <span style="color: #3b82f6">🔹 {word.title()}</span>
                            <span style="color: #94a3b8">{freq:,} occurrences</span>
                        </div>
                    """, unsafe_allow_html=True)

    with col2:
        st.markdown("##### 📋 Short Descriptions Insights")
        monthly_short = monthly_word_analysis(df, "cleaned_short_desc")
        for month in sorted(monthly_short.keys(), reverse=True):
            with st.expander(f"📅 {month}"):
                for word, freq in monthly_short[month][:5]:
                    st.markdown(f"""
                        <div style="display: flex; justify-content: space-between; margin: 0.5rem 0;">
                            <span style="color: #10b981">🔸 {word.title()}</span>
                            <span style="color: #94a3b8">{freq:,} occurrences</span>
                        </div>
                    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align:center; color:#64748b; margin: 2rem 0'>
        🚀 Developed By <a href='https://www.linkedin.com/in/hardik-chhipa-303040242/' target='_blank' style='color:#64748b; text-decoration:none; font-weight:bold;'>Hardik Chhipa</a>
    </div>
""", unsafe_allow_html=True)
