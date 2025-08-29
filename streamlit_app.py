import streamlit as st
import requests
import json

st.set_page_config(page_title="BFHL Tester")
st.title("BFHL API Tester ")

st.markdown("""Enter comma-separated values (they will be sent as strings).""")

api_base = st.text_input("API base URL", value="http://localhost:8000")
user_text = st.text_input("Input list (comma-separated)")


def to_list(text):
    raw = [x.strip() for x in text.split(",")]
    return [x for x in raw if x != ""]

if st.button("Send ▶️"):
    data = {"data": to_list(user_text)}
    st.write("Request JSON:", data)
    try:
        r = requests.post(f"{api_base}/bfhl", json=data, timeout=20)
        st.write("Status:", r.status_code)
        try:
            st.json(r.json())
        except Exception:
            st.write(r.text)
    except Exception as e:
        st.error(f"Request failed: {e}")
