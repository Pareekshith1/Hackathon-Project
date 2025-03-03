# main_app.py
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="CreativeStudio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom styling
st.markdown(
    """
    <style>
        body {
            background-color: #f5f5f5;
            font-family: 'Arial', sans-serif;
        }
        .header {
            padding: 20px;
            background-color: white;  /* Change the background color of the main title */
            color: #394240;  /* Change the text color of the main title */
            text-align: center;
        }
        .section {
            margin: 20px 0;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .footer {
            background-color: #394240;
            padding: 10px;
            color: white;
            text-align: center;
            border-radius: 10px;
            margin-top: 20px;
        }
        .feature-title {
            color: #1f6f8b; /* Change the color for feature titles */
        }
        .custom-text {
            font-size: 19px;  /* Increase the font size for st.write paragraphs */
            font-weight: bold;  /* Make the text bold */
            font-style: italic;  /* Make the text italic */
            line-height: 1.6;  /* Set line height for better readability */
            font-family: 'Georgia', serif;  /* Change the font for st.write paragraphs */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<div class="header"><h1>Welcome to <span style="color: #1f6f8b;">CreativeStudio</span> 🎨</h1></div>', unsafe_allow_html=True)

# About CreativeStudio
st.markdown('<div class="section"><h2>About CreativeStudio:</h2>', unsafe_allow_html=True)
st.write(
    "CreativeStudio is your all-in-one creative hub, providing powerful tools for image generation, "
    "background removal, and filter addition. Elevate your designs effortlessly with our AI-driven applications."
)
st.markdown('</div>', unsafe_allow_html=True)

# Key Features
st.markdown('<div class="section"><h2 class="feature-title">Key Features:</h2>', unsafe_allow_html=True)
features = {
    "AI Editor": "Generate stunning images from text with advanced AI algorithms.",
    "Background Remover": "Remove backgrounds seamlessly and enhance your visuals.",
    "Filter Adder": "Apply artistic filters to your images for a unique touch.",
}

for feature, description in features.items():
    st.markdown(f"<p class='custom-text'>{feature}: {description}</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Explore each feature in-depth
st.markdown('<div class="section"><h2 class="feature-title">Explore each feature in-depth:</h2>', unsafe_allow_html=True)
feature_details = {
    "AI Editor": "Craft unique images by providing text prompts to our AI model. It goes beyond DALL-E to bring your imagination to life.",
    "Background Remover": "Effortlessly remove backgrounds from your images, making them suitable for various contexts.",
    "Filter Adder": "Add artistic filters to your images, enhancing their visual appeal and giving them a personalized touch.",
}

for feature, detail in feature_details.items():
    st.markdown(f"<p class='custom-text'>- {feature}: {detail}</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Get Started
st.markdown('<div class="section"><h2 class="feature-title">Get Started:</h2>', unsafe_allow_html=True)
st.markdown("<p class='custom-text'>Use the sidebar to navigate between different features and let your creativity soar!</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Contact Us
st.markdown('<div class="section"><h2 class="feature-title">Contact Us:</h2>', unsafe_allow_html=True)
st.markdown("<p class='custom-text'>Have questions or feedback? Reach out to us at contact@creativestudio.com</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer"><p class="custom-text">Designed with ❤️ by CreativeStudio</p></div>', unsafe_allow_html=True)
