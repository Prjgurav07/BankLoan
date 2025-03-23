import streamlit as st
import numpy as np
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit app
st.title('Loan Approval Prediction')
st.write('Enter the details below to check your loan approval status.')

# Input fields
customer_age = st.number_input('Customer Age', min_value=18, max_value=100, step=1)
family_member = st.number_input('Family Member', min_value=0, step=1)
income = st.number_input('Income', min_value=0.0, step=100.0)
loan_amount = st.number_input('Loan Amount', min_value=0.0, step=100.0)
cibil_score = st.number_input('Cibil Score', min_value=300, max_value=900, step=1)
tenure = st.number_input('Tenure (in months)', min_value=6, step=6)

gender = st.selectbox('Gender', ['Male', 'Female'])
married = st.selectbox('Married', ['Yes', 'No'])
education = st.selectbox('Education', ['Yes', 'No'])
self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
previous_loan_taken = st.selectbox('Previous Loan Taken', ['Yes', 'No'])
property_area = st.selectbox('Property Area', ['Urban', 'Semiurban', 'Rural'])
customer_bandwidth = st.selectbox('Customer Bandwidth', ['Good', 'Bad'])

# Mapping categorical data to numerical
gender = 1 if gender == 'Male' else 0
married = 1 if married == 'Yes' else 0
education = 1 if education == 'Yes' else 0
self_employed = 1 if self_employed == 'Yes' else 0
previous_loan_taken = 1 if previous_loan_taken == 'Yes' else 0
property_area = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}[property_area]
customer_bandwidth = 1 if customer_bandwidth == 'Good' else 0

# Predict button
if st.button('Predict'):
    try:
        features = [customer_age, family_member, income, loan_amount, cibil_score, tenure, 
                    gender, married, education, self_employed, previous_loan_taken, property_area, customer_bandwidth]
        final_features = np.array(features).reshape(1, -1)
        prediction = model.predict(final_features)

        if prediction == 1:
            st.error('Loan is Rejected')
        else:
            st.success('Loan is Approved')
    except Exception as e:
        st.error(f"Error: {e}")
