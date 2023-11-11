import streamlit as st
import pickle
import numpy as np
import pandas as pd

location_mapping = {
    "Kesarapalli":10,
    "Auto Nagar":12,
    "Poranki": 8,
    "Kankipadu": 5,
    "Benz Circle": 0,
    "Gannavaram": 2,
    "Rajarajeswari Peta": 9,
    "Gunadala": 4,
    "Gollapudi": 3,
    "Enikepadu": 1,
    "Vidhyadharpuram": 11,
    "Penamaluru": 7,
    "Payakapuram": 6
}
status_mapping = {'New': 0, 'Ready to move': 1, 'Resale': 2, 'Under Construction': 3}
facing_mapping = {'East': 0,'North': 2,'NorthEast': 3,'NorthWest': 4,'South': 5,'SouthEast': 6,'SouthWest': 7,'West': 8, 'None':1}
type_mapping = {'Apartment': 0,'Independent Floor': 1,'Independent House': 2,'Residential Plot': 3,'Studio Apartment': 4,'Villa': 5}

with open("House.pkl",'rb')as  f:
    model = pickle.load(f)

def predict(bed,bath,Loc,size,status,facing,Type):
    selected_location = location_mapping[Loc]
    selected_status = status_mapping[status]
    selected_facing = facing_mapping[facing]
    selected_type = type_mapping[Type]
    data = np.array([[bed,bath,selected_location,size,selected_status,selected_facing,selected_type]])
    res = model.predict(data)[0]
    # print(f'house price predicted {res}')
    return res

if __name__=="__main__":
    st.title("House Price Prediction")
    col1,col2 = st.columns([1,1])
    bed= col1.slider("Enter No.of Bedrooms",max_value = 10,min_value = 0,value=2)
    bath = col2.slider("Enter No.of Bathrooms",max_value = 10,min_value = 0,value=2)
    Loc = col1.selectbox(
    "Select Location",
    (location_mapping.keys()),
    index=None,
    placeholder="Select Location",
    )
    size = col1.number_input("Enter Sqft",step=500,placeholder="Enter Sqft")
    status = col2.selectbox(
    "Select Status",
    (status_mapping.keys()),
    index=None,
    placeholder="Select Status",
    )
    facing = col2.selectbox(
    "Select Facing",
    (facing_mapping.keys()),
    index=None,
    placeholder="Select Facing",
    )
    Type = st.selectbox(
    "Select Type",
    (type_mapping.keys()),
    index=None,
    placeholder="Select Type",
    )


    if st.button('Predict',type="primary"):
        a=round(predict(bed,bath,Loc,size,status,facing,Type),2)    
        st.title(f'Predicted Price: {a} Lakhs')
