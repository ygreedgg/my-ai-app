import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6IrOA2CEt6iFVGrYOlqpVbTsH4xFTEjKvvrPi0NkV0P0w") 

st.title("🎬 AI Video Recap Tool")

video_url = st.text_input("YouTube ဗီဒီယို လင့်ခ်ကို ထည့်ပါ:")
duration = st.slider("လိုချင်တဲ့ ဗီဒီယိုအရှည် (မိနစ်)", 1, 10, 5)

if st.button("Start"):
    if video_url:
        st.write(f"ဗီဒီယိုကို လေ့လာနေပါပြီ... (Duration: {duration} min)")
        
        # Gemini AI ကို မေးခွန်းထုတ်ခြင်း
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Summarize this video for me in {duration} minutes: {video_url}")
        
        st.subheader("AI ရဲ့ အနှစ်ချုပ်")
        st.write(response.text)
    else:
        st.error("ကျေးဇူးပြု၍ လင့်ခ်တစ်ခု ထည့်ပေးပါ။")
