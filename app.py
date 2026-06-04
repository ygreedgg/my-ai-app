import streamlit as st
import google.generativeai as genai

# Secrets ထဲက Key ကို ခေါ်သုံးခြင်း
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

st.title("🎬 AI Video Recap Tool")

video_url = st.text_input("YouTube ဗီဒီယို လင့်ခ်ကို ထည့်ပါ:")
duration = st.slider("လိုချင်တဲ့ ဗီဒီယိုအရှည် (မိနစ်)", 1, 10, 5)

if st.button("Start"):
    if video_url:
        st.write("ဗီဒီယိုကို လေ့လာနေပါပြီ...")
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Summarize this video in {duration} minutes: {video_url}")
        st.subheader("AI ရဲ့ အနှစ်ချုပ်")
        st.write(response.text)
    else:
        st.error("လင့်ခ်တစ်ခု ထည့်ပေးပါ။")

