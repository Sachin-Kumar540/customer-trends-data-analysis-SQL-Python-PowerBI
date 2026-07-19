import streamlit as st
import pandas as pd

# Set the title of the web app
st.title("Customer Shopping Behavior Analysis")

# Cache the data loading and cleaning process for better performance
@st.cache_data
def load_and_clean_data():
    # Load the data 
    # Note: Ensure the filename exactly matches the one in your GitHub repository
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

# Run the function
df = load_and_clean_data()

# --- DISPLAYING THE DATA ON THE WEB APP ---

st.header("1. Dataset Overview")
st.write("Summary Statistics:")
st.write(df.describe(include='all'))

st.write("Missing Values:")
st.write(df.isnull().sum())

st.header("2. Cleaned Data Sample")
st.dataframe(df.head(10))

st.header("3. Engineered Features")
st.write("Age Groups and Purchase Frequency mapping:")
st.dataframe(df[['age', 'age_group', 'frequency_of_purchases', 'purchase_frequency_days']].head(10))