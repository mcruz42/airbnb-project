import streamlit as st
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title = "Predictions", 
                   page_icon = "💲")

# Title and description
st.markdown(
    """
    <h2 style = "text-align: center; color: #69503c;">Predictions 💲</h2>
    <p style = "text-align: center; font-size: 18px; color: #1c2d8f;">
    Please fill in the form below to get the predicted price of your chosen features.
    </p>
    """,
    unsafe_allow_html = True
)

# Subtitle with a descriptive message
st.markdown(
    """
    <h3 style="text-align: center; color: #2b50aa;">Discover Your Price</h3>
    <p style="text-align: center; color: #6c757d; font-size: 1.1rem;">
    Based on the details you provided, we predicted the Airbnb price.
    </p>
    <hr style="border: 1px solid #ccc;">
    """,
    unsafe_allow_html=True,
)

def predictions(reg_model):
    # Model prediction with confidence intervals
    alpha = 0.1  # 90% confidence level
    prediction, intervals = reg_model.predict(st.session_state.user_encoded_df, alpha=alpha)
    pred_value = prediction[0]

    # Display prediction results
    # st.metric(label="Predicted Price", value=f"${pred_value * 100:.2f}")
    st.metric(label="Predicted Price (with 90% confidence)", value=f"${pred_value:.2f}")

# Ensure inputs are available
if 'user_encoded_df' not in st.session_state:
    st.warning("Please complete the form on the 'Preferences' page to view your price prediction")

# Ensure inputs are available
if 'user_encoded_df' in st.session_state:
    model = st.selectbox("Select your prediction model", ["XGBoost (recommended)", "Random Forest", "Decision Tree"])

    if model == "Decision Tree":
    # Load the trained model and dataset
        with open('dt_airbnb.pickle', 'rb') as model_file:        
            reg_model = pickle.load(model_file)
            predictions(reg_model)
            
    if model == "Random Forest":
    # Load the trained model and dataset
        with open('rf_airbnb.pickle', 'rb') as model_file:
            reg_model = pickle.load(model_file)
            predictions(reg_model)

    if model == "XGBoost (recommended)":
        # Load the trained model and dataset
        with open('xg_ml1.pickle', 'rb') as model_file:        
            reg_model = pickle.load(model_file)
            predictions(reg_model)


# default_df = pd.read_csv('California_airbnb_cleaned.csv')
# # Dropping null values
# default_df.dropna(inplace=True)

# # Prepare user input data
# user_data = {
#     'GRE Score': st.session_state['gre_score'],
#     'TOEFL Score': st.session_state['toefl_score'],
#     'University Rating': st.session_state['univ_rating'],
#     'SOP': st.session_state['sop'],
#     'LOR': st.session_state['lor'],
#     'CGPA': st.session_state['cgpa'],
#     'Research': st.session_state['research']
# }
# user_df = pd.DataFrame([user_data])

# # Combine user data with default dataset for dummy encoding
# encode_df = default_df.drop(columns=["neighbourhood_cleansed", "longitude", "latitude", "price"])

# # Ensure the order of columns in user data is in the same order as that of original data
# user_df = user_df[encode_df.columns]

# # Concatenate two dataframes together along rows (axis = 0)
# encode_df = pd.concat([encode_df, user_df], axis = 0)
# encode_dummy_df = pd.get_dummies(encode_df).tail(1)

# Model prediction with confidence intervals
# alpha = 0.1  # 90% confidence level
# prediction, intervals = reg_model.predict(st.session_state.user_encoded_df, alpha=alpha)
# pred_value = prediction[0]
# lower_limit = max(0, intervals[:, 0][0][0])
# upper_limit = min(1, intervals[:, 1][0][0])

# # Display prediction results
# st.metric(label="Predicted Price", value=f"{pred_value * 100:.2f}%")
# st.write("With a 90% confidence interval:")
# st.write(f"**Confidence Interval**: [{lower_limit * 100:.2f}%, {upper_limit * 100:.2f}%]")