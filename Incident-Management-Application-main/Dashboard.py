import streamlit as st

# Set page config for better layout
st.set_page_config(page_title="Incident Data Dashboard", layout="wide", page_icon="🚨")

# Custom CSS for advanced styling
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');
        
        * {
            font-family: 'Space Grotesk', sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #0a0e1a 0%, #1a1f2c 100%);
            color: #ffffff;
        }
        
        .gradient-header {
            font-size: 4.5rem !important;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin: 1rem 0;
            font-weight: 700;
            text-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }
        
        .feature-card {
            background: rgba(25, 29, 40, 0.8);
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem;
            border: 1px solid rgba(255,255,255,0.1);
            transition: all 0.3s ease;
            min-height: 250px;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            background: rgba(35, 40, 54, 0.9);
            box-shadow: 0 8px 25px rgba(78, 205, 196, 0.15);
        }
        
        .emoji-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .pulse {
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        .cta-button {
            background: linear-gradient(45deg, #4ecdc4, #45b7d1);
            color: white !important;
            padding: 1rem 2.5rem !important;
            border-radius: 50px !important;
            font-weight: 700 !important;
            border: none !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .cta-button:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(78, 205, 196, 0.4);
        }
        
        .radial-gradient {
            position: fixed;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle at 50% 50%, rgba(78, 205, 196, 0.1) 0%, transparent 60%);
            pointer-events: none;
            z-index: -1;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Radial gradient background element
st.markdown('<div class="radial-gradient"></div>', unsafe_allow_html=True)

# Page Header
st.markdown('<h1 class="gradient-header">Incident Intelligence Platform</h1>', unsafe_allow_html=True)
st.markdown(
    """
    <p style='text-align: center; font-size: 1.4rem; color: #a1aac3; margin-bottom: 3rem;'>
    Transform Raw Data into Actionable Security Insights
    </p>
    """,
    unsafe_allow_html=True
)

# Feature Grid
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="emoji-icon">📈</div>
            <h3>Advanced Analytics</h3>
            <p style='color: #a1aac3;'>Interactive visualizations with deep trend analysis and pattern recognition</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="feature-card pulse">
            <div class="emoji-icon">🤖</div>
            <h3>AI Predictions</h3>
            <p style='color: #a1aac3;'>Machine learning-powered incident resolution suggestions and risk forecasting</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="emoji-icon">⚡</div>
            <h3>Real-time Updates</h3>
            <p style='color: #a1ac3;'>Live data monitoring with instant alerting system</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# CTA Section
st.markdown(
    """
    <div style='text-align: center; margin: 4rem 0;'>
        <h2 style='margin-bottom: 2rem;'>Ready to Transform Your Incident Management?</h2>
        <button class="cta-button" onclick="window.location.href='#'">Explore Dashboard →</button>
    </div>
    """,
    unsafe_allow_html=True
)

# Stats Marquee (Horizontal Scroll)
st.markdown(
    """
    <div style='background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 12px; margin: 2rem 0;'>
        <div style='display: flex; justify-content: space-around; align-items: center;'>
            <div style='text-align: center;'>
                <div style='font-size: 2rem; color: #4ecdc4;'>45K+</div>
                <div style='color: #a1aac3;'>Processed Incidents</div>
            </div>
            <div style='text-align: center;'>
                <div style='font-size: 2rem; color: #ff6b6b;'>93%</div>
                <div style='color: #a1aac3;'>Accuracy Rate</div>
            </div>
            <div style='text-align: center;'>
                <div style='font-size: 2rem; color: #45b7d1;'>24/7</div>
                <div style='color: #a1aac3;'>Real-time Monitoring</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align:center; color:#64748b; margin: 2rem 0'>
        🚀 Developed By <a href='https://www.linkedin.com/in/hardik-chhipa-303040242/' target='_blank' style='color:#64748b; text-decoration:none; font-weight:bold;'>Hardik Chhipa</a>
    </div>
""", unsafe_allow_html=True)
