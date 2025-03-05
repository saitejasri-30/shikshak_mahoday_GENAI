import streamlit as st
import openai  # Replace with Google PaLM integration if needed
import requests
import speech_recognition as sr
import time

# Set up Streamlit page config
st.set_page_config(
    page_title="Shikshak Mahoday - AI Learning Platform",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            background-color: #f4f4f4;
        }
        .title {
            font-size: 42px;
            font-weight: bold;
            color: #2C3E50;
            text-align: center;
        }
        .subtitle {
            font-size: 20px;
            text-align: center;
            color: #7F8C8D;
        }
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
            background-color: #2980B9;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Title & Description
st.markdown('<p class="title">Shikshak Mahoday: AI-Powered Learning</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Personalized, Adaptive Learning for Data Science</p>', unsafe_allow_html=True)

# Input fields in columns for better UI layout
col1, col2 = st.columns([3, 1])

with col1:
    learner_input = st.text_input("🔍 What would you like to learn about?", placeholder="Enter a topic...")

with col2:
    learner_progress = st.selectbox("📈 Select your level:", ["Beginner", "Intermediate", "Advanced"])

# API Key (Secure method: Store in environment variables or config files)
OPENAI_API_KEY = "your-secure-api-key"

# Function to generate learning content using OpenAI or Google PaLM
def generate_personalized_content(input_text, learner_progress):
    if not OPENAI_API_KEY:
        return "Error: API key is missing. Please configure the API key."

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Generate a personalized data science learning module for {input_text} at {learner_progress} level.",
        max_tokens=200
    )
    return response.choices[0].text.strip()

# Generate learning content when button is clicked
if st.button("✨ Generate Learning Content"):
    if learner_input:
        with st.spinner("🔄 Generating learning content... Please wait."):
            time.sleep(2)  # Simulating API response time
            personalized_content = generate_personalized_content(learner_input, learner_progress)
        st.success("🎉 Learning Content Generated!")
        st.write(f"📘 Learning Content:\n\n{personalized_content}")
    else:
        st.warning("⚠ Please enter a topic to generate content.")

# Display latest research papers in an attractive way
st.subheader("📚 Latest Research in Data Science")

def fetch_latest_research():
    research_papers = [
        {"title": "Recent Advances in Machine Learning", "link": "https://arxiv.org/abs/1234567"},
        {"title": "Deep Learning in Data Science", "link": "https://scholar.google.com/xyz"}
    ]
    return research_papers

for paper in fetch_latest_research():
    st.markdown(f"- 🔗 *[{paper['title']}]({paper['link']})*")

# Voice Interaction Section
st.subheader("🎙 Voice Interaction - Convert Speech to Text")

if st.button("🎤 Start Listening"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now!")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.success(f"🗣 Recognized Speech: {text}")
        except Exception as e:
            st.error("❌ Could not understand the audio.")

# Footer
st.markdown("---")
st.markdown("👨‍🏫 Developed by *Shikshak Mahoday AI Team* | 🚀 Powered by OpenAI | 🤖 Adaptive Learning Platform")