import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title = "Model Insights", 
                   page_icon = "📊")

# Page title
st.markdown(
    """
    <h2 style="text-align: center; color: #4a4a4a;">Model Insights 📊</h2>
    """,
    unsafe_allow_html=True,
)

# Subtitle with a descriptive message
st.markdown(
    """
    <h3 style="text-align: center; color: #2b50aa;">Learn more about each model</h3>
    <hr style="border: 1px solid #ccc;">
    """,
    unsafe_allow_html=True,
)
st.write("View insights to help you better understand the factors influencing the prediction.")

ml_choice = st.selectbox("Choose your predicition model", ["Decision Tree", "Random Forest", "XGBoost"])

if ml_choice == "Decision Tree":
    # Showing additional items in tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Feature Importance", 
                            "Histogram of Residuals", 
                            "Predicted Vs. Actual", 
                            "Coverage Plot"])
    with tab1:
        st.write("### Feature Importance")
        st.image('dt_feature_imp.svg')
        st.caption("Relative importance of features in prediction.")
    with tab2:
        st.write("### Histogram of Residuals")
        st.image('dt_residual_plot.svg')
        st.caption("Distribution of residuals to evaluate prediction quality.")
    with tab3:
        st.write("### Plot of Predicted Vs. Actual")
        st.image('dt_pred_vs_actual.svg')
        st.caption("Visual comparison of predicted and actual values.")
    with tab4:
        st.write("### Coverage Plot")
        st.image('dt_coverage.svg')
        st.caption("Range of predictions with confidence intervals.")

if ml_choice == "Random Forest":
    # Showing additional items in tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Feature Importance", 
                            "Histogram of Residuals", 
                            "Predicted Vs. Actual", 
                            "Coverage Plot"])
    with tab1:
        st.write("### Feature Importance")
        st.image('rf_feature_imp.svg')
        st.caption("Relative importance of features in prediction.")
    with tab2:
        st.write("### Histogram of Residuals")
        st.image('rf_residual_plot.svg')
        st.caption("Distribution of residuals to evaluate prediction quality.")
    with tab3:
        st.write("### Plot of Predicted Vs. Actual")
        st.image('rf_pred_vs_actual.svg')
        st.caption("Visual comparison of predicted and actual values.")
    with tab4:
        st.write("### Coverage Plot")
        st.image('rf_coverage.svg')
        st.caption("Range of predictions with confidence intervals.")

if ml_choice == "XGBoost":
    # Showing additional items in tabs
    tab1, tab2, tab3, tab4 = st.tabs(["Feature Importance", 
                            "Histogram of Residuals", 
                            "Predicted Vs. Actual", 
                            "Coverage Plot"])
    with tab1:
        st.write("### Feature Importance")
        st.image('xg_feat_imp.svg')
        st.caption("Relative importance of features in prediction.")
    with tab2:
        st.write("### Histogram of Residuals")
        st.image('xg_residuals.svg')
        st.caption("Distribution of residuals to evaluate prediction quality.")
    with tab3:
        st.write("### Plot of Predicted Vs. Actual")
        st.image('xg_pred_actual.svg')
        st.caption("Visual comparison of predicted and actual values.")
    with tab4:
        st.write("### Coverage Plot")
        st.image('xg_coverage.svg')
        st.caption("Range of predictions with confidence intervals.")
