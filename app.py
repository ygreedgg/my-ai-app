import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6LU0IXQcLpjMu26Lw3-bE9G3RxVktDc8lJKVtPIq75mPg") 

st.title("🎬 AI Video Recap Tool")

video_url = st.text_input("YouTube ဗီဒီယို လင့်ခ်ကို ထည့်ပါ:")
duration = st.slider("လိုချင်တဲ့ ဗီဒီယိုအရှည် (မိနစ်)", 1, 10, 5)

if st.button("Start"):
    if video_url:
        try:
            st.write(f"ဗီဒီယိုကို လေ့လာနေပါပြီ...")
            # ဒီမှာ gemini-1.5-flash ကို သုံးထားပါတယ်
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(f"Summarize this video in {duration} minutes: {video_url}")
            st.subheader("AI ရဲ့ အနှစ်ချုပ်")
            st.write(response.text)
        except Exception as e:
            st.error(f"အမှားတစ်ခု ဖြစ်ပေါ်နေပါတယ်: {e}")
    else:
        st.error("ကျေးဇူးပြု၍ လင့်ခ်တစ်ခု ထည့်ပေးပါ။")

