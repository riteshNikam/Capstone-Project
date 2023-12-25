import streamlit 
import pickle
import numpy as np 
import pandas as pd
import os

model_path = os.path.join(os.path.dirname(__file__), 'best_model.pkl')

# Importing model

model = pickle.load(open(model_path, 'rb'))

streamlit.title('Car Price Predictor')


streamlit.sidebar.title('Fill data to predict selling price')

# Handling brand

brand_name = ['Ambassador', 'Audi', 'BMW', 'Chevrolet', 'Daewoo', 'Datsun', 'Fiat',
       'Force', 'Ford', 'Honda', 'Hyundai', 'Isuzu', 'Jaguar', 'Jeep', 'Kia',
       'Land', 'MG', 'Mahindra', 'Maruti', 'Mercedes-Benz', 'Mitsubishi',
       'Nissan', 'OpelCorsa', 'Renault', 'Skoda', 'Tata', 'Toyota',
       'Volkswagen', 'Volvo']

brand_coded_features = ['brand_' + i for i in brand_name]

input_brand = {}

# for brand in brand_coded_features:
#     input_brand[brand] = streamlit.sidebar.selectbox(f'Select {brand}', [0, 1])

brand = streamlit.sidebar.selectbox('Select Car Brand', brand_name)

for b in brand_coded_features:
    if b == ('brand_' + brand):
        input_brand[b] = 1
    else:
        input_brand[b] = 0


# year
year = streamlit.sidebar.slider('Select year' , 1992, 2020, step = 1)

# km Driven
km_driven = streamlit.sidebar.slider('Distance traveller', 0, 300000, step = 1)

# Fuel
fuel = streamlit.sidebar.selectbox('Select Fuel Type', ['CNG', 'Diesel', 'Electric', 'LPG', 'Petrol'])

# Seller Type
seller_type = streamlit.sidebar.selectbox('Select Seller Type', ['Dealer', 'Individual', 'Trustmark Dealer'])

# Transmission
transmission = streamlit.sidebar.selectbox('Select Transmission Type', ['Automatic', 'Manual'])

# Ownership type
owner = streamlit.sidebar.selectbox('Select Ownership Type', ['First Owner', 'Forth & Above Owner', 'Second Owner', 'Test Drive Owner', 'Third Owner'])







if streamlit.button('Predict Selling Price of Cars'):
    user_input = {}


    # handling year 

    user_input['year'] = year

    # handling km_driven

    user_input['km_driven'] = km_driven

    # handling fuel 

    # 'CNG', 'Diesel', 'Electric', 'LPG', 'Petrol'

    if fuel == 'CNG':
        fuel = 0
    elif fuel == 'Diesel':
        fuel = 1
    elif fuel == 'Electric':
        fuel = 2
    elif fuel == 'LPG':
        fuel = 3
    elif fuel == 'Petrol':
        fuel = 4

    user_input['fuel'] = fuel

    # handling seller_type

    # 'Dealer', 'Individual', 'Trustmark Dealer'

    if seller_type == 'Dealer':
        seller_type = 0
    elif seller_type == 'Individual':
        seller_type = 1
    elif seller_type == 'Trustmark Dealer':
        seller_type = 2

    user_input['seller_type'] = seller_type

    # handling transmission

    # 'Automatic', 'Manual'

    if transmission == 'Automatic':
        transmission = 0
    elif transmission == 'Manual':
        transmission = 1

    user_input['transmission'] = transmission

    # handling owner

    # 'First Owner', 'Forth & Above Owner', 'Second Owner', 
    # 'Test Drive Owner', 'Third Owner'

    if owner == 'First Owner':
        owner = 0
    elif owner == 'Forth & Above Owner':
        owner = 1
    elif owner == 'Second Owner':
        owner = 2
    elif owner == 'Test Drive Owner':
        owner = 3
    elif owner == 'Third Owner':
        owner = 4

    user_input['owner'] = owner


    user_input.update(input_brand)

    test = pd.DataFrame(user_input, [0])

    streamlit.success(f'Selling Price of Car : {round(model.predict(test)[0], 2)}')