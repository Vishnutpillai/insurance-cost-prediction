import streamlit as st
import pickle
import numpy as np

#Load Model  and Columns
model=pickle.load(open('Best_model.pkl','rb'))
columns=pickle.load(open('Column_order.pkl','rb'))

st.set_page_config(page_title='Insurance Predictor')

st.title('Insurance Cost Prediction')
st.write('Enter the details below:')

#Input fields
age=st.slider('Age',18,100,25)
bmi=st.slider('Medical BMI',10.0,50.0,25.0)
children=st.slider('Children',0,5,0)

sex=st.selectbox('Sex',['Male','Female'])
smoker=st.selectbox('Smoker',['Yes','No'])
region=st.selectbox('Region',['Northeast','Northwest','Southeast','Southwest'])

#Convert input into dataframe format
input_dict={
    'age': age,
    'bmi': bmi,
    'children': children,
    'sex': 1 if sex == 'Male' else 0,
    'smoker': 1 if smoker == 'Yes' else 0,
    'region_northwest': 1 if region == 'Northwest' else 0,
    'region_southeast': 1 if region == 'Southeast' else 0,
    'region_southwest': 1 if region == 'Southwest' else 0
}

#Ensure correct order
input_data=[input_dict.get(col,0) for col in columns ]
input_array=np.array([input_data])

#Prediction
if st.button('Predict'):
    prediction=model.predict(input_array)
    st.success(f'Estimated Insurance Cost: ${prediction[0]:,.2f}')