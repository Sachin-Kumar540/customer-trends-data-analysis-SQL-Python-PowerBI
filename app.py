import streamlit as st
import pandas as pd
import plotly.express as px

# Setup layout for a wider, more attractive dashboard
st.set_page_config(page_title="Customer Behavior Dashboard", layout="wide")

# Custom styled banner for the title
st.markdown("""
    <div style="background-color:#072F5F;padding:15px;border-radius:10px;margin-bottom:20px;">
    <h1 style="color:white;text-align:center;margin:0;">Customer Shopping Behavior</h1>
    </div>
""", unsafe_allow_html=True)

# Cache your exact data cleaning function
@st.cache_data
def load_and_clean_data():
    df = pd.read_csv('customer_shopping_behavior (1).csv') 
    
    # Imputing missing values
    df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
    
    # Renaming columns
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})
    
    # Feature Extraction: Age Group
    labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
    df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)
    
    # Feature Extraction: Purchase Frequency mapping
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

raw_df = load_and_clean_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Dashboard")

# Dynamic filters based strictly on your dataframe columns
selected_sub = st.sidebar.selectbox("Subscription Status", ['All'] + list(raw_df['subscription_status'].unique()))
selected_gender = st.sidebar.selectbox("Gender", ['All'] + list(raw_df['gender'].unique()))
selected_category = st.sidebar.multiselect("Category", raw_df['category'].unique(), default=raw_df['category'].unique())

# Apply filters to the data
df = raw_df.copy()
if selected_sub != 'All':
    df = df[df['subscription_status'] == selected_sub]
if selected_gender != 'All':
    df = df[df['gender'] == selected_gender]
if selected_category:
    df = df[df['category'].isin(selected_category)]

# --- TOP KPI METRICS ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", f"{len(df):,}")
col2.metric("Average Purchase", f"${df['purchase_amount'].mean():.2f}")
col3.metric("Average Rating", f"{df['review_rating'].mean():.2f}")

st.divider()

# --- DASHBOARD VISUALIZATIONS ---
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("Revenue by Category")
    rev_cat = df.groupby('category')['purchase_amount'].sum().reset_index()
    fig_bar = px.bar(rev_cat, x='category', y='purchase_amount', color_discrete_sequence=['#125B9A'])
    st.plotly_chart(fig_bar, use_container_width=True)

with row1_col2:
    st.subheader("Customers by Subscription")
    sub_counts = df['subscription_status'].value_counts().reset_index()
    fig_donut = px.pie(sub_counts, names='subscription_status', values='count', hole=0.5, color_discrete_sequence=['#FF69B4', '#4B0082'])
    st.plotly_chart(fig_donut, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("Sales by Age Group")
    sales_age = df['age_group'].value_counts().reset_index()
    fig_bar_h = px.bar(sales_age, x='count', y='age_group', orientation='h', color_discrete_sequence=['#00C9A7'])
    st.plotly_chart(fig_bar_h, use_container_width=True)

with row2_col2:
    st.subheader("Top 5 Locations by Revenue")
    rev_loc = df.groupby('location')['purchase_amount'].sum().nlargest(5).reset_index()
    fig_loc = px.bar(rev_loc, x='purchase_amount', y='location', orientation='h', color_discrete_sequence=['#FF9671'])
    st.plotly_chart(fig_loc, use_container_width=True)

st.divider()

# --- BEHIND THE SCENES: DATA PROCESSING ---
st.markdown("## Technical Data Processing")
st.markdown("This section details the data cleaning and feature engineering executed via Python (Pandas) prior to visualization.")

st.markdown("### 1. Dataset Overview (Post-Cleaning)")
st.write("Summary Statistics:")
st.dataframe(df.describe(include='all'))

st.markdown("### 2. Cleaned Data Sample")
st.dataframe(df.head(10))

st.markdown("### 3. Engineered Features")
st.write("Mapping Categorical Age and Purchase Frequency into actionable analytical groups:")
st.dataframe(df[['age', 'age_group', 'frequency_of_purchases', 'purchase_frequency_days']].head(10))
