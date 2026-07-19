import streamlit as st
import pandas as pd

# Set the title and layout of the web app
st.set_page_config(page_title="Customer Shopping Behavior", layout="wide")
st.title("Customer Shopping Behavior Analysis")

# Cache the data loading and cleaning process for better performance
@st.cache_data
def load_and_clean_data():
    df = pd.read_csv('customer_shopping_behavior (1).csv') 

    # Imputing missing values in Review Rating column
    df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
    
    # Renaming columns for better readability
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ','_')
    df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})
    
    # Create a new column age_group
    labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
    df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)
    
    # Create new column purchase_frequency_days
    frequency_mapping = {
        'Fortnightly': 14,
        'Weekly': 7,
        'Monthly': 30,
        'Quarterly': 90,
        'Bi-Weekly': 14,
        'Annually': 365,
        'Every 3 Months': 90
    }
    df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
    
    # Drop redundant column
    df = df.drop('promo_code_used', axis=1)
    
    return df

# Run the function to load data
raw_df = load_and_clean_data()

# --- 1. SIDEBAR FILTERS (Must come before displaying data) ---
st.sidebar.header("Dashboard Filters")
selected_gender = st.sidebar.selectbox("Select Gender", ['All', 'Male', 'Female'])

# Apply the filter to a working dataframe
if selected_gender != 'All':
    df = raw_df[raw_df['gender'] == selected_gender]
else:
    df = raw_df

# --- 2. KPI METRICS ---
st.markdown("### Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric(label="Total Customers", value=len(df))
col2.metric(label="Average Purchase", value=f"${df['purchase_amount'].mean():.2f}")
col3.metric(label="Top Category", value=df['category'].mode()[0])

st.divider()

# --- 3. CHARTS ---
st.markdown("### Purchases by Category")
category_counts = df['category'].value_counts()
st.bar_chart(category_counts)

st.divider()

# --- 4. DATA TABLES ---
st.markdown("### Dataset Overview")
st.write("Summary Statistics:")
st.dataframe(df.describe(include='all'))

st.markdown("### Cleaned Data Sample")
st.dataframe(df.head(10))
