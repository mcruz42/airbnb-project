import streamlit as st

st.set_page_config(
    page_title = "Home",
    page_icon = "🏠",
    # layout = "wide"
)

# Centered Title using HTML and Markdown
st.markdown(
    """
    <h2 style = "text-align: center; color: #69503c;">Airbnb Price Predictor 🏠</h2>
    """,
    unsafe_allow_html = True,
)

# Subtitle with styling
st.markdown(
    """
    <h3 style = "text-align: center; color: #1c2d8f; font-family: Arial, sans-serif;">
    Use this app to predict your LA Airbnb cost!
    </h3>
    """,
    unsafe_allow_html = True,
)

# Insert an image
st.image('airbnb_gif.gif', use_column_width = True, 
         caption = "Predict your LA Airbnb price based on your preferences")