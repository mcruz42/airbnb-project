# Import libraries
import streamlit as st
import pandas as pd
import pickle
import sklearn
import warnings
import xgboost as xgb
warnings.filterwarnings('ignore')

st.set_page_config(page_title = "Preferences", 
                   page_icon = "✍️")


# Title and description
st.markdown(
    """
    <h2 style = "text-align: center; color: #69503c;">Your Preference Form ✍️</h2>
    <p style = "text-align: center; font-size: 18px; color: #1c2d8f;">
    Please fill in the form below to get the predicted price of your chosen features.
    </p>
    """,
    unsafe_allow_html = True
)
st.image('airbnb.webp', use_column_width = True)

st.info('Please fill in the form below to get the predicted price of your chosen features.', icon= "ℹ️")

#to check if button clicked
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True


# Load the default dataset
default_df = pd.read_csv('California_airbnb_cleaned.csv')
# default_df = default_df.dropna(inplace=True)


property_type_list = default_df['property_type'].unique().tolist()
region_list = default_df['Region'].unique().tolist()


with st.form('user_inputs_form'):
        
    st.header("Enter your preferred rental features here:")
   
    region = st.selectbox('Choose what region you are interested in:', options=region_list)    
    
    property_type = st.selectbox('Choose what property type you are interested in:', options= property_type_list)    
    accomodates = st.number_input('Number to accomodate: ', min_value=1, max_value=16, value=4, step=1)    
    beds = st.number_input('Number of beds: ', min_value=1, max_value=25, value=3, step=1)  
    bathrooms = st.number_input('Number of bathrooms: ', min_value=0, max_value=20, value=4, step=1)   
    minimum_nights = st.number_input('Minimum number of nights: ', min_value=1, max_value=1124, value=5, step=1)
    maximum_nights = st.number_input('Maximum number of nights: ', min_value=1, max_value=1123, value=10, step=1)
    instant_bookable = st.radio('Listing is available to book instantly? ', options=['Yes','No'])

    host_is_superhost = st.radio('Would you like a super host? ', options=['Yes','No'])
    host_total_listings_count = st.number_input('Average number of Host listings: ', min_value=1, max_value=1443, value=1, step=1)
    host_identity_verified = st.radio('Would you like a verified host? ', options=['Yes','No'])
    number_of_reviews_ltm = st.number_input('Number of reviews on listing: ', min_value=0, max_value=772, value=1, step=1)
    reviews_scores_rating = st.number_input('Rating Score of listing: ', min_value=0.0, max_value=5.0, value=4.0, step=0.25)
    
    city = 'los-angeles'

    submit_button = st.form_submit_button("Submit Form Data", on_click=click_button)


if st.session_state.clicked:
    
    st.success("Inputs saved! Navigate to the 'Predictions' page to see your results.")

    #Encode the inputs for model prediction
    encode_df = default_df.copy()
    encode_df = encode_df.drop(columns=['neighbourhood_cleansed','latitude','longitude','price'])



    # Combine the list of user data as a row to default_df
    encode_df.loc[len(encode_df)] = [host_is_superhost, host_total_listings_count, host_identity_verified, property_type, accomodates,
                                     beds, minimum_nights,maximum_nights,number_of_reviews_ltm, reviews_scores_rating, instant_bookable,
                                     city,region,bathrooms]

    encode_df['host_is_superhost'] = encode_df['host_is_superhost'].replace(['Yes','No'],[1.0,0.0])
    encode_df['host_identity_verified'] = encode_df['host_identity_verified'].replace(['Yes','No'],[1.0,0.0])
    encode_df['instant_bookable'] = encode_df['instant_bookable'].replace(['Yes','No'],[1.0,0.0])

    st.write(encode_df.tail(1))
    # # Create dummies for encode_df
    encode_dummy_df = pd.get_dummies(encode_df)

    # Extract encoded user data
    user_encoded_df = encode_dummy_df.tail(1)
    st.session_state["user_encoded_df"] = user_encoded_df
