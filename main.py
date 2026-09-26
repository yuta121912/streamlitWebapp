import streamlit as st 
st.title("My First Streamlit App")
answer = st.radio("扉を置けますか？",["y","n"])
if answer == "y":
    st.write("扉を置くことができます。")
else:
    st.write("扉を置くことができません。")