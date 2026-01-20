import streamlit as st

st.title("FRUIT SELECTION APP")
st.subheader("Getting Started")
st.text("This is a simple Streamlit application.")
st.write("Welcome to our fruit selection app.")
if st.button("start"):
    st.write("getting started with fruit selection!")

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

cups = st.number_input("how many fruits do you want?",min_value=1,max_value=10,step=1,key='num_fruits')
st.write(f"You want {cups} fruits.")

name=st.text_input("enter your name")
st.write(f"Hello, {name}!")

expiry = st.date_input("select the expiry date")
st.write(f"Expiry date selected: {expiry}")

time=st.time_input("select the pickup time")
st.write(f"Pickup time selected {time}")

col1,col2,col3,col4,col5=st.columns(5)

with col1:
    st.subheader("raspberry")
    #st.image("https://sl.bing.net/kAqQ3Xo9CTs",width=100)
    vote1 = st.button("why")


with col2:
    st.subheader("pineapple")
    vote2 = st.button("to")

with col3:
    st.subheader("strawberry")
    vote3 = st.button("cart")

with col4:
    st.subheader("kiwi")
    vote4 = st.button("Add to cart")

with col5:
    st.subheader("mango")
    vote5 = st.button("add")
st.sidebar.title("Sidebar")
name= st.sidebar.text_input("enter your name")
fruit=st.sidebar.selectbox("choose your fruit",["strawberry","kiwi","mango"])

st.sidebar.write(f"Hello, {name}! You selected {fruit}.")

with st.expander("see your fruit selection details"):
    st.write("Here are the details of your fruit selection:")
    st.write(f"Fruit Type: {fruit_type}")
    st.write(f"Flavour: {flavour}")
    st.write(f"Favourite Flavour: {flav}")
    st.write(f"Number of Fruits: {cups}")
    st.write(f"Expiry Date: {expiry}")
    st.write(f"Pickup Time: {time}")
    st.write("""

    Thank you for using our fruit selection app!
             We hope you enjoy your fruits.""")
    
st.balloons()
#st.snow()
st.toast("Your fruit selection is complete!",icon="🍓")
st.markdown('### Enjoy your fruits! 🍉🍓🍍🍌🍒')
st.info("For more information, visit our website.")
st.warning("Please make sure to pick up your fruits on time.")
st.error("Error: Unable to process your request at the moment.")
st.markdown('>Blockquote')

