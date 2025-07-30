import pickle
import pandas as pd
import streamlit as st
model1=pickle.load(open("HousePrice.pkl","rb"))

def mydeploy():
    st.title("House Price Prediction")
    area=st.number_input("Enter Area")
    bedrooms=st.number_input("Enter Bedroom You Need")
    age=st.number_input("Enter How Old House You Looking For")
    pred=st.button("Predict Price")
    if pred:
        df=pd.DataFrame({"area":[area],"bedrooms":[bedrooms],"age":[age]})
        x=model1.predict(df)
        st.write("The Price of House:",x[0])
        
mydeploy()    