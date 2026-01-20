import streamlit as st

st.title("Hello, Streamlit!")
st.subheader("Getting Started")
st.text("This is a simple Streamlit application.")
st.write("Welcome to your first Streamlit app.")
if st.button("Click Me"):
    st.write("Button clicked!")

tnc = st.checkbox("I agree to the terms and conditions")
if tnc:
    st.write("Thank you for agreeing to the terms and conditions.")

fruit_type = st.radio("select your fruit type",["fresh","dried","canned"])
st.write(f"You selected: {fruit_type} fruit")

flavour = st.select_slider("select your flavour",["sweet","sour","bitter","salty","umami"])
st.write(f"You selected: {flavour} flavour")

flav = st.selectbox("choose your favourite flavour",["chocolate","vanilla","strawberry","butterscotch","mango"])
st.write(f"You selected: {flav} flavour")

fruits = st.selectbox("choose one",["strawberry","raspberry","kiwi","mango","pineapple"])

st.write(f"your choice IS {fruits} EXCELLENT CHOICE")

st.success('your fruit is selected successfully!')