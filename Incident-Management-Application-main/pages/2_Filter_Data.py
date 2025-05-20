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

# st.title("Filter Incident Data")

# # Filter by Status
# st.subheader("Filter by Incident Status")
# status_options = df["Status"].unique()
# selected_status = st.multiselect("Select Status", status_options, default=status_options)
# filtered_df = df[df["Status"].isin(selected_status)]
# st.write(filtered_df)

# st.write("")
# st.write("")
# st.write("")
# st.write("")
# st.write("")
# st.write("")

# # Filter by Priority
# st.subheader("Filter by Priority")
# priority_options = df["Priority"].unique()
# selected_priority = st.multiselect("Select Priority", priority_options, default=priority_options)
# filtered_df = filtered_df[filtered_df["Priority"].isin(selected_priority)]
# st.write(filtered_df)


# import streamlit as st
# import pandas as pd

# pd.set_option("styler.render.max_elements", 2_000_000)  # Increase from default 262,144

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
    
#     .header-card {
#         background: rgba(30, 41, 59, 0.8);
#         border-radius: 15px;
#         padding: 1.5rem;
#         margin: 1rem 0;
#         border: 1px solid #334155;
#         box-shadow: 0 4px 30px rgba(0,0,0,0.1);
#     }
    
#     .filter-card {
#         background: rgba(30, 41, 59, 0.6);
#         border-radius: 12px;
#         padding: 1.5rem;
#         margin: 1rem 0;
#         border: 1px solid #3b82f6;
#     }
    
#     .stDataFrame {
#         border-radius: 10px !important;
#         border: 1px solid #334155 !important;
#     }
    
#     .metric-box {
#         background: rgba(99, 102, 241, 0.15);
#         border-radius: 10px;
#         padding: 1rem;
#         margin: 0.5rem;
#         text-align: center;
#     }
    
#     .highlight {
#         color: #3b82f6;
#         font-weight: 600;
#     }
#     </style>
# """, unsafe_allow_html=True)

# @st.cache_data
# def load_data():
#     file_path = 'dataset/data.xlsx'
#     df = pd.read_excel(file_path, parse_dates=["Opened At", "Resolved Date"])
#     df.fillna("", inplace=True)
    
#     if "Resolved Time (days)" not in df.columns:
#         df["Resolved Time (days)"] = (df["Resolved Date"] - df["Opened At"]).dt.days
    
#     return df

# df = load_data()

# # Page Title
# st.markdown("""
#     <div class="header-card">
#         <h1 style='color: #3b82f6; margin:0'>🔍 Incident Data Filter</h1>
#         <p style='color: #94a3b8; margin:0'>Explore and filter incident reports</p>
#     </div>
# """, unsafe_allow_html=True)


# # Filter Section
# with st.container():
#     st.markdown('<div class="filter-card">', unsafe_allow_html=True)
    
#     # Status Filter
#     col1, col2 = st.columns([3, 1])
#     with col1:
#         st.markdown("#### 🚨 Incident Status Filter")
#         status_options = df["Status"].unique()
#         selected_status = st.multiselect(
#             "Select statuses to include:",
#             options=status_options,
#             default=status_options,
#             label_visibility="collapsed"
#         )
    
#     with col2:
#         st.markdown("### ")
#         if st.button("↺ Reset Filters"):
#             selected_status = status_options
    
#     # Priority Filter
#     st.markdown("#### 🚩 Priority Level Filter")
#     priority_options = df["Priority"].unique()
#     selected_priority = st.multiselect(
#         "Select priorities to include:",
#         options=priority_options,
#         default=priority_options,
#         label_visibility="collapsed"
#     )
    
#     st.markdown('</div>', unsafe_allow_html=True)

# # Apply Filters
# filtered_df = df[df["Status"].isin(selected_status)]
# filtered_df = filtered_df[filtered_df["Priority"].isin(selected_priority)]

# # Display Results
# with st.container():
#     st.markdown("#### 📊 Filtered Results")
#     st.dataframe(
#         filtered_df.style
#         .background_gradient(subset=["Resolved Time (days)"], cmap='Blues')
#         .format({"Resolved Time (days)": "{:.1f}"}),
#         use_container_width=True,
#         height=400
#     )
    
#     # Download Button
#     st.download_button(
#         label="📥 Download Filtered Data",
#         data=filtered_df.to_csv(index=False).encode('utf-8'),
#         file_name='filtered_incidents.csv',
#         mime='text/csv'
#     )
# # Metrics Overview
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.markdown(f"""
#         <div class="metric-box">
#             <div style='color: #94a3b8; font-size:0.9rem'>Total Incidents</div>
#             <div style='color: #3b82f6; font-size:2rem; font-weight:600'>{len(df)}</div>
#         </div>
#     """, unsafe_allow_html=True)

# with col2:
#     avg_res_time = df["Resolved Time (days)"].mean()
#     st.markdown(f"""
#         <div class="metric-box">
#             <div style='color: #94a3b8; font-size:0.9rem'>Avg Resolution</div>
#             <div style='color: #3b82f6; font-size:2rem; font-weight:600'>{avg_res_time:.1f} days</div>
#         </div>
#     """, unsafe_allow_html=True)

# with col3:
#     active_cases = len(df[df['Status'].str.contains('Open|Pending', case=False)])
#     st.markdown(f"""
#         <div class="metric-box">
#             <div style='color: #94a3b8; font-size:0.9rem'>Active Cases</div>
#             <div style='color: #3b82f6; font-size:2rem; font-weight:600'>{active_cases}</div>
#         </div>
#     """, unsafe_allow_html=True)


# # Empty spaces with decorative elements
# st.markdown("---")
# st.markdown("""
#     <div style='text-align:center; color:#64748b; margin: 2rem 0'>
#         Developed By Janenie J.
#     </div>
# """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
pd.set_option("styler.render.max_elements", 2_000_000)  # Increase from default 262,144

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
    
    .header-card {
        background: rgba(30, 41, 59, 0.8);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #334155;
        box-shadow: 0 4px 30px rgba(0,0,0,0.1);
    }
    
    .filter-card {
        background: rgba(30, 41, 59, 0.6);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #3b82f6;
    }
    
    .stDataFrame {
        border-radius: 10px !important;
        border: 1px solid #334155 !important;
    }
    
    .metric-box {
        background: rgba(99, 102, 241, 0.15);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem;
        text-align: center;
    }
    
    .highlight {
        color: #3b82f6;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    file_path = 'dataset/Incident_PreProcessed.xlsx'
    df = pd.read_excel(file_path, parse_dates=["Opened At", "Resolved Date"])
    df.fillna("", inplace=True)
    
    return df

df = load_data()

# Page Title
st.markdown("""
    <div class="header-card">
        <h1 style='color: #3b82f6; margin:0'>🔍 Incident Data Filter</h1>
        <p style='color: #94a3b8; margin:0'>Explore and filter incident reports</p>
    </div>
""", unsafe_allow_html=True)


# Filter Section
with st.container():
    st.markdown('<div class="filter-card">', unsafe_allow_html=True)
    
    # Status Filter
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("#### 🚨 Incident Status Filter")
        status_options = df["Status"].unique()
        selected_status = st.multiselect(
            "Select statuses to include:",
            options=status_options,
            default=status_options,
            label_visibility="collapsed"
        )
    
    with col2:
        st.markdown("### ")
        if st.button("↺ Reset Filters"):
            selected_status = status_options
    
    # Priority Filter
    st.markdown("#### 🚩 Priority Level Filter")
    priority_options = df["Priority"].unique()
    selected_priority = st.multiselect(
        "Select priorities to include:",
        options=priority_options,
        default=priority_options,
        label_visibility="collapsed"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)

# Apply Filters
filtered_df = df[df["Status"].isin(selected_status)]
filtered_df = filtered_df[filtered_df["Priority"].isin(selected_priority)]

# Display Results
with st.container():
    st.markdown("#### 📊 Filtered Results")
    st.dataframe(
        filtered_df.style
        .background_gradient(subset=["Ticket Age"], cmap='Blues')
        .format({"Ticket Age": "{:.1f}"}),
        use_container_width=True,
        height=400
    )
    
    # Download Button
    st.download_button(
        label="📥 Download Filtered Data",
        data=filtered_df.to_csv(index=False).encode('utf-8'),
        file_name='filtered_incidents.csv',
        mime='text/csv'
    )
# Metrics Overview
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
        <div class="metric-box">
            <div style='color: #94a3b8; font-size:0.9rem'>Total Incidents</div>
            <div style='color: #3b82f6; font-size:2rem; font-weight:600'>{len(df)}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    avg_res_time = df["Ticket Age"].mean()
    st.markdown(f"""
        <div class="metric-box">
            <div style='color: #94a3b8; font-size:0.9rem'>Avg Resolution</div>
            <div style='color: #3b82f6; font-size:2rem; font-weight:600'>{avg_res_time:.1f} days</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    active_cases = len(df[df['Status'].str.contains('Open|Pending', case=False)])
    st.markdown(f"""
        <div class="metric-box">
            <div style='color: #94a3b8; font-size:0.9rem'>Active Cases</div>
            <div style='color: #3b82f6; font-size:2rem; font-weight:600'>{active_cases}</div>
        </div>
    """, unsafe_allow_html=True)


# Empty spaces with decorative elements
st.markdown("---")
st.markdown("""
    <div style='text-align:center; color:#64748b; margin: 2rem 0'>
        Developed By Hardik Chhipa
    </div>
""", unsafe_allow_html=True)
