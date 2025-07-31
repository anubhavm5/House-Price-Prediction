import pickle
import pandas as pd
import streamlit as st
model1=pickle.load(open("HousePrice.pkl","rb"))

def mydeploy():
    st.title("House Price Prediction")
    area=st.number_input("Enter Area",min_value=0,step=100)
    bedrooms=st.number_input("Enter Bedroom You Need",min_value=1,max_value=7,step=1)
    age=st.number_input("Enter How Old House You Looking For",min_value=1,max_value=50,step=1)
    pred=st.button("Predict Price")
    if pred:
        df=pd.DataFrame({"area":[area],"bedrooms":[bedrooms],"age":[age]})
        x=model1.predict(df)
        st.write("The Price of House:",x[0])
        
mydeploy()    
