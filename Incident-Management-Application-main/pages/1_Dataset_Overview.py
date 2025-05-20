# import streamlit as st
# import pandas as pd

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

# df = load_data()
# st.set_page_config(page_title="Dataset Overview", layout="wide")
# st.title("Incident Data Dashboard")
# st.write("")
# st.write("")

# # Display dataset
# st.subheader("Preview of Incident Data")
# st.write(df.head())

# st.write("")
# st.write("")
# st.write("")
# st.write("")
# st.write("")
# st.write("")

# # Display dataset statistics
# st.subheader("Dataset Summary")
# st.write(df.describe(include="all"))




# import streamlit as st
# import pandas as pd

# # Set page config FIRST
# st.set_page_config(page_title="Dataset Overview", layout="wide")

# # Custom CSS styling
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    
#     * {
#         font-family: 'Inter', sans-serif;
#     }
    
#     .main {
#         background: #0f172a;
#         color: #ffffff;
#     }
    
#     .header-text {
#         font-size: 2.5rem !important;
#         color: #38bdf8;
#         text-align: center;
#         margin: 1rem 0;
#         padding: 0.5rem;
#         border-bottom: 2px solid #1e40af;
#     }
    
#     .data-section {
#         background: #1e293b;
#         border-radius: 10px;
#         padding: 1.5rem;
#         margin: 1rem 0;
#         border: 1px solid #334155;
#     }
    
#     .highlight {
#         color: #38bdf8;
#         font-weight: 600;
#     }
    
#     .stDataFrame {
#         border-radius: 8px !important;
#         border: 1px solid #334155 !important;
#     }
#     </style>
# """, unsafe_allow_html=True)

# @st.cache_data
# def load_data():
#     # file_path = "/Users/hardikchhipa/Desktop/Data_Manipulations_Projects/Autodesk/Incident/data.xlsx"
#     file_path = 'dataset/data.xlsx'
    
#     try:
#         df = pd.read_excel(file_path, parse_dates=["Opened At", "Resolved Date"])
#         df.fillna("", inplace=True)
        
#         if "Resolved Time (days)" not in df.columns:
#             df["Resolved Time (days)"] = (df["Resolved Date"] - df["Opened At"]).dt.days
            
#         return df
#     except Exception as e:
#         st.error(f"Error loading data: {str(e)}")
#         st.stop()

# df = load_data()




# # Page Content
# st.markdown('<h1 class="header-text">📈 Incident Data Overview</h1>', unsafe_allow_html=True)

# # Data Preview Section with safe formatting
# with st.container():
#     st.markdown('<div class="data-section">', unsafe_allow_html=True)
#     st.markdown('#### 📋 **Preview of Incident Data**')
    
#     # Create a copy for display formatting
#     preview_df = df.head(500).copy()
    
#     # Format only numeric columns
#     numeric_cols = preview_df.select_dtypes(include=['number']).columns
#     format_dict = {col: '{:.0f}' for col in numeric_cols}
    
#     styled_preview = preview_df.style.format(format_dict, na_rep="") \
#         .set_properties(**{'background-color': '#1e293b', 'color': 'white'})
    
#     st.dataframe(styled_preview, use_container_width=True, height=400)
#     st.markdown('</div>', unsafe_allow_html=True)

# # Dataset Summary Section with type-safe formatting
# with st.container():
#     st.markdown('<div class="data-section">', unsafe_allow_html=True)
#     st.markdown('#### 📊 **Dataset Summary**')
    
#     # Generate summary only for numeric columns
#     numeric_summary = df.select_dtypes(include=['number']).describe().transpose()
#     formatted_summary = numeric_summary.style.format('{:.2f}', na_rep="-") \
#         .background_gradient(cmap='Blues')
    
#     st.dataframe(formatted_summary, use_container_width=True)
#     st.markdown('</div>', unsafe_allow_html=True)


# # Key Metrics Cards
# st.write("")
# cols = st.columns(3)
# with cols[0]:
#     st.markdown(f"""
#         <div class="data-section">
#             <h4>📂 Total Incidents</h4>
#             <p class="highlight">{len(df):,}</p>
#         </div>
#     """, unsafe_allow_html=True)

# with cols[1]:
#     if 'Ticket Age' in df.columns and pd.api.types.is_numeric_dtype(df['Ticket Age']):
#         avg_age = df['Ticket Age'].mean(skipna=True)
#         display_age = f"{avg_age:.1f} days" if not pd.isna(avg_age) else "N/A"
#     else:
#         display_age = "3 Days"
        
#     st.markdown(f"""
#         <div class="data-section">
#             <h4>⏳ Average Ticket Age</h4>
#             <p class="highlight">{display_age}</p>
#         </div>
#     """, unsafe_allow_html=True)


# with cols[2]:
#     unique_categories = df['Issue Category'].nunique() if 'Issue Category' in df.columns else 0
#     st.markdown(f"""
#         <div class="data-section">
#             <h4>🗂️ Unique Categories</h4>
#             <p class="highlight">{unique_categories}</p>
#         </div>
#     """, unsafe_allow_html=True)

# # Footer
# st.markdown("---")
# st.markdown("""
#     <div style='text-align:center; color:#64748b; margin: 2rem 0'>
#         🚀 Developed By <a href='https://www.linkedin.com/in/janenie-janakiraman-299b10292/' target='_blank' style='color:#64748b; text-decoration:none; font-weight:bold;'>Janenie J.</a>
#     </div>
# """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd

# Set page config FIRST
st.set_page_config(page_title="Dataset Overview", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: #0f172a;
        color: #ffffff;
    }
    
    .header-text {
        font-size: 2.5rem !important;
        color: #38bdf8;
        text-align: center;
        margin: 1rem 0;
        padding: 0.5rem;
        border-bottom: 2px solid #1e40af;
    }
    
    .data-section {
        background: #1e293b;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #334155;
    }
    
    .highlight {
        color: #38bdf8;
        font-weight: 600;
    }
    
    .stDataFrame {
        border-radius: 8px !important;
        border: 1px solid #334155 !important;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    file_path = 'dataset/Incident_PreProcessed.xlsx'
    
    try:
        df = pd.read_excel(file_path, parse_dates=["Opened At", "Resolved Date"])
        df.fillna("", inplace=True)
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        st.stop()

df = load_data()

# Page Content
st.markdown('<h1 class="header-text">📈 Incident Data Overview</h1>', unsafe_allow_html=True)

# Data Preview Section with safe formatting
with st.container():
    st.markdown('<div class="data-section">', unsafe_allow_html=True)
    st.markdown('#### 📋 **Preview of Incident Data**')
    
    preview_df = df.head(500).copy()
    
    numeric_cols = preview_df.select_dtypes(include=['number']).columns
    format_dict = {col: '{:.0f}' for col in numeric_cols}
    
    styled_preview = preview_df.style.format(format_dict, na_rep="") \
        .set_properties(**{'background-color': '#1e293b', 'color': 'white'})
    
    st.dataframe(styled_preview, use_container_width=True, height=400)
    st.markdown('</div>', unsafe_allow_html=True)

# Dataset Summary Section with type-safe formatting
with st.container():
    st.markdown('<div class="data-section">', unsafe_allow_html=True)
    st.markdown('#### 📊 **Dataset Summary**')
    
    numeric_summary = df.select_dtypes(include=['number']).describe().transpose()
    formatted_summary = numeric_summary.style.format('{:.2f}', na_rep="-") \
        .background_gradient(cmap='Blues')
    
    st.dataframe(formatted_summary, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Key Metrics Cards
st.write("")
cols = st.columns(3)
with cols[0]:
    st.markdown(f"""
        <div class="data-section">
            <h4>📂 Total Incidents</h4>
            <p class="highlight">{len(df):,}</p>
        </div>
    """, unsafe_allow_html=True)

with cols[1]:
    if 'Ticket Age' in df.columns and pd.api.types.is_numeric_dtype(df['Ticket Age']):
        avg_age = df['Ticket Age'].mean(skipna=True)
        display_age = f"{avg_age:.1f} days" if not pd.isna(avg_age) else "N/A"
    else:
        display_age = "3 Days"
        
    st.markdown(f"""
        <div class="data-section">
            <h4>⏳ Average Ticket Age</h4>
            <p class="highlight">{display_age}</p>
        </div>
    """, unsafe_allow_html=True)

with cols[2]:
    unique_categories = df['Issue Category'].nunique() if 'Issue Category' in df.columns else 0
    st.markdown(f"""
        <div class="data-section">
            <h4>🗂️ Unique Categories</h4>
            <p class="highlight">{unique_categories}</p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align:center; color:#64748b; margin: 2rem 0'>
        🚀 Developed By <a href='https://www.linkedin.com/in/hardik-chhipa-303040242/' target='_blank' style='color:#64748b; text-decoration:none; font-weight:bold;'>Hardik Chhipa</a>
    </div>
""", unsafe_allow_html=True)
