import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle as pkl

with open('model.pkl','rb') as f:
    model = pkl.load(f)


st.sidebar.title("Side Bar")
option = st.sidebar.radio("Analysis", ["Home","Anylysis","Visualization","Predictoin"])

def home():
    abc = st.text_input("Enter Name: ")
    if abc:
        st.write(f"Hello {abc}")


    shravani = st.number_input("Enter age: ",1)
    if shravani:
        st.write(f"your age is {shravani}")


def analysis():
    file = st.file_uploader("Choose a file", type = ["csv"])
    c = st.button('Analyse')

    if c:
        if file:
            df = pd.read_csv(file)
        else:
            df = pd.read_csv("feeds.csv")
        # st.markdown(df)
        st.write(df)
        st.write(df.describe())


def visualization():
    file = st.file_uploader("Choose a file", type = ["csv"])
    if file:
        df = pd.read_csv(file)
        st.write(df.columns)
        i = st.selectbox("Select a column", df.columns)
        fig, ax = plt.subplots()
        ax.plot(df[i])
        st.pyplot(fig)

    # # c = st.button('Visualization')
    # # if c:
    # if file:
    #     df = pd.read_csv(file)
    #     st.write(df.columns)
    #         # choice = st.text_input("select One column: ")
    #         # st.write(df[choice])
    # else:
    #     df = pd.read_csv("feeds.csv")
    #     st.write(df.columns)
    #         # choice = st.text_input("select One column: ")
    #         # st.write(df[choice])

    #     cho = st.text_input("select One column: ")
    #     b = st.button("clicke to visualiz")
    #     if b:
    #         st.write(df[cho])
    #         print(cho)



def prediction():
    year = st.number_input("Year: ")
    state = st.number_input("State: ")
    total = st.number_input("Total: ")
    TminusU = st.number_input("T minus U: ")
    type = st.number_input("type: ")
    user_input = [[year, state, total, TminusU, type]]
    b = st.button("Predict")

    if b:
        st.write(model.predict(user_input))

    # st.write(dt.predict(user_input))


if option == "Home":
    home()
elif option == "Anylysis":
    analysis()
elif option == "Visualization":
    visualization()
elif option == "Predictoin":
    prediction()