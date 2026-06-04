import streamlit as st

st.title("My AI Video Tool")
st.write("ကျွန်တော့်ရဲ့ AI ဝက်ဆိုက်လေး ဖြစ်ပါတယ်!")

user_input = st.text_input("ဘာလုပ်ပေးရမလဲ?")
if st.button("စတင်မယ်"):
    st.write(f"သင်ပြောတာ: {user_input}")
  
