# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import matplotlib.pyplot as plt
# import seaborn as sns

# @st.cache_data
# def load_data():
#     file_path = "/Users/hardikchhipa/Desktop/Data_Manipulations_Projects/Autodesk/Incident/data.xlsx"
    
#     # Read the Excel file and parse date columns
#     df = pd.read_excel(file_path, parse_dates=["Opened At", "Resolved Date"])

#     # Handling missing values
#     df.fillna("", inplace=True)

#     # Compute Resolved Time (if not already present)
#     if "Resolved Time (days)" not in df.columns:
#         df["Resolved Time (days)"] = (df["Resolved Date"] - df["Opened At"]).dt.days

#     return df

# st.title("Resolved Time Trends")

# df = load_data()




# # 🔹 Plotly Interactive Line Chart
# fig_plotly = px.line(df, x="Opened At", y="Resolved Time (days)",
#                       title="Resolved Time Over Time (Interactive)",
#                       labels={"Opened At": "Opened Date", "Resolved Time (days)": "Resolution Days"},
#                       template="plotly_dark", color_discrete_sequence=["cyan"])

# fig_plotly.update_xaxes(tickangle=45, title_text="Opened At")
# fig_plotly.update_yaxes(title_text="Resolved Time (days)")

# st.plotly_chart(fig_plotly)
# st.write("")
# st.write("")
# st.write("")
# st.write("")
# st.write("")
# st.write("")
# st.write("")
# st.write("")
# st.write("")
# st.write("")


# # 🔹 Seaborn Line Chart (Matplotlib)

# fig, ax = plt.subplots(figsize=(12, 6))

# # Set background color
# fig.patch.set_facecolor("#0E1118")  # Background color of figure
# ax.set_facecolor("#0E1118")  # Background color of plot area

# # Plot the line chart
# sns.lineplot(x=df["Opened At"], y=df["Resolved Time (days)"], ax=ax, color="royalblue")

# # Set title and labels with white text
# ax.set_title("Resolved Time Over Time", fontsize=14, fontweight="bold", color="white")
# ax.set_xlabel("Opened At", fontsize=12, color="white")
# ax.set_ylabel("Resolved Time (days)", fontsize=12, color="white")

# # Change tick labels to white
# ax.tick_params(axis="x", 
#                 # rotation=45, 
#                 colors="white")
# ax.tick_params(axis="y", colors="white")

# # Change grid lines for better visibility
# ax.grid(True, linestyle="--", linewidth=0.5, color="gray", alpha=0.5)  # Optional

# # Display in Streamlit
# st.pyplot(fig)



import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


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

@st.cache_data
def load_data():
    file_path = 'dataset/Incident_PreProcessed.xlsx'
    df = pd.read_excel(file_path, parse_dates=["Opened At", "Resolved Date"])
    df.fillna("", inplace=True)
    
    if "Resolved Time (days)" not in df.columns:
        df["Resolved Time (days)"] = (df["Resolved Date"] - df["Opened At"]).dt.days
    
    return df

# Page Header
st.markdown("""
    <div class="header-card">
        <h1 style='color: white; margin:0'>⏳ Resolution Time Analysis</h1>
        <p style='color: #94a3b8; margin:0'>Track and analyze incident resolution performance over time</p>
    </div>
""", unsafe_allow_html=True)

df = load_data()

# Key Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    avg_time = df["Resolved Time (days)"].mean()
    st.markdown(f"""
        <div class="metric-box">
            <div style='color: #94a3b8'>📅 Avg Resolution</div>
            <div style='color: #3b82f6; font-size:1.8rem'>{avg_time:.1f} days</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    max_time = df["Resolved Time (days)"].max()
    st.markdown(f"""
        <div class="metric-box">
            <div style='color: #94a3b8'>⏰ Longest Resolution</div>
            <div style='color: #ef4444; font-size:1.8rem'>{max_time} days</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    min_time = df["Resolved Time (days)"].min()
    st.markdown(f"""
        <div class="metric-box">
            <div style='color: #94a3b8'>⚡ Quickest Resolution</div>
            <div style='color: #10b981; font-size:1.8rem'>{min_time} days</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    resolved_count = len(df[df["Resolved Time (days)"] > 0])
    st.markdown(f"""
        <div class="metric-box">
            <div style='color: #94a3b8'>✅ Resolved Cases</div>
            <div style='color: #8b5cf6; font-size:1.8rem'>{resolved_count}</div>
        </div>
    """, unsafe_allow_html=True)

# Main Visualization Section
with st.container():
    st.markdown('<div class="viz-card">', unsafe_allow_html=True)
    st.markdown("### 📈 Resolution Time Trends")
    
    tab1, tab2 = st.tabs(["Interactive Analysis", "Statistical View"])
    
    with tab1:
        # Enhanced Plotly Chart
        fig = px.line(df, x="Opened At", y="Resolved Time (days)", 
                     title="<b>Resolution Timeline</b>",
                     template="plotly_dark",
                     color_discrete_sequence=["#00ffff"],
                     labels={"Opened At": "Report Date", "Resolved Time (days)": "Days to Resolve"},
                     hover_data={"Opened At": "|%B %d, %Y", "Resolved Time (days)": ":.1f"})
        
        fig.update_layout(
            hoverlabel=dict(
                bgcolor="#1e293b",
                font_size=14,
                font_color="white"
            ),
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(step="all")
                    ])
                ),
                rangeslider=dict(visible=True),
                type="date"
            ),
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        # Enhanced Seaborn Chart
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.patch.set_facecolor('#0f172a')
        ax.set_facecolor('#0f172a')
        
        sns.lineplot(
            x=df["Opened At"], 
            y=df["Resolved Time (days)"], 
            color="#00ffff",
            linewidth=2,
            ax=ax
        )
        
        # Styling
        ax.set_title("Resolution Time Distribution", color="white", fontsize=14, pad=20)
        ax.set_xlabel("Report Date", color="white", fontsize=12)
        ax.set_ylabel("Days to Resolve", color="white", fontsize=12)
        ax.tick_params(colors='white')
        
        # Custom grid
        ax.grid(True, color='#334155', linestyle='--', linewidth=0.5)
        
        # Annotations
        max_idx = df["Resolved Time (days)"].idxmax()
        ax.annotate(f'Longest: {df["Resolved Time (days)"].max()} days',
                    xy=(df["Opened At"][max_idx], df["Resolved Time (days)"][max_idx]),
                    xytext=(15, 15), textcoords='offset points',
                    arrowprops=dict(arrowstyle="->", color='white'),
                    color='white')
        
        st.pyplot(fig)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Additional Analysis
with st.container():
    st.markdown('<div class="viz-card">', unsafe_allow_html=True)
    st.markdown("### 📊 Distribution Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Histogram
        fig_hist = px.histogram(df, x="Resolved Time (days)", 
                               nbins=50,
                               title="Resolution Time Distribution",
                               color_discrete_sequence=["#00ffff"],
                               template="plotly_dark")
        fig_hist.update_layout(
            bargap=0.1,
            xaxis_title="Days to Resolve",
            yaxis_title="Number of Cases"
        )
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        # Box Plot
        fig_box = px.box(df, y="Resolved Time (days)", 
                        title="Resolution Time Spread",
                        color_discrete_sequence=["#00ffff"],
                        template="plotly_dark")
        fig_box.update_layout(
            yaxis_title="Days to Resolve",
            showlegend=False
        )
        st.plotly_chart(fig_box, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align:center; color:#64748b; margin: 2rem 0'>
        🚀 Developed By <a href='https://www.linkedin.com/in/hardik-chhipa-303040242/' target='_blank' style='color:#64748b; text-decoration:none; font-weight:bold;'>Hardik Chhipa</a>
    </div>
""", unsafe_allow_html=True)
