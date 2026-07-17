📊 Customer Shopping Behavior Analysis: End-to-End Data Analytics Project
📝 Overview
This repository contains a full-stack, corporate-level data analytics project that analyzes customer shopping behavior for a retail company. The goal of this project is to uncover purchasing trends, understand customer segmentation, and optimize sales strategies using a complete data analytics workflow.

This project covers the entire data lifecycle: from raw data manipulation in Python, database management and advanced querying in PostgreSQL, to interactive data visualization in Power BI.

🛠️ Tech Stack
Data Cleaning & EDA: Python (Pandas, SQLAlchemy, psycopg2)

Database: PostgreSQL (Also compatible with MySQL / MS SQL Server)

Data Analysis & Querying: SQL (CTEs, Window Functions, Subqueries, Aggregations)

Data Visualization: Power BI (DAX, Interactive Dashboards)

Reporting: Gamma AI (Client-ready presentation deck)

📂 Dataset Information
The dataset represents customer transactions and includes the following key information:

Demographics: Age, Gender, Location

Purchase Details: Item Purchased, Category, Purchase Amount (USD), Size, Color, Season

Customer Behavior: Review Rating, Subscription Status, Shipping Type, Discount Applied

History: Previous Purchases, Frequency of Purchases

🚀 Project Workflow
1. Data Cleaning & Feature Engineering (Python)
Handled missing values smartly (e.g., imputing missing review ratings using the median of their specific product category).

Standardized column names into snake_case for seamless SQL integration.

Engineered new features such as age_group and converted text-based shopping frequencies into numeric purchase_frequency_days.

Removed redundant columns to optimize database storage.

2. Database Integration (Python to SQL)
Established a connection between the Jupyter Notebook and a PostgreSQL database using SQLAlchemy.

Loaded the cleaned dataset directly into the database as a SQL table, mimicking real-world corporate data environments.

3. Advanced Data Analysis (SQL)
Executed complex SQL queries to answer critical business questions. Key techniques used include:

Subqueries: Found customers who used discounts but still spent more than the average purchase amount.

Window Functions (ROW_NUMBER): Ranked the top 3 best-selling products within each specific category.

CTEs & CASE Statements: Segmented customers into "New", "Returning", and "Loyal" categories based on their purchase history.

Aggregations: Analyzed revenue splits by gender, shipping type, and subscription status.

4. Interactive Dashboard (Power BI)
Connected Power BI directly to the PostgreSQL database.

Created custom DAX measures for KPIs like Total Customers, Average Purchase Amount, and Average Review Rating.

Built an interactive dashboard featuring dynamic charts (Revenue/Sales by Category and Age Group) and button slicers for easy filtering by stakeholders.

📊 Dashboard Preview
(Optional: Add a screenshot of your Power BI Dashboard here)
![Dashboard Preview](link_to_your_image.png)

💻 How to Run This Project
Clone the repository:

Bash
git clone https://github.com/Sachin-kumar540/customer-shopping-analysis.git
Install the required Python packages:

Bash
pip install pandas psycopg2 sqlalchemy
Update the database credentials in the Jupyter Notebook to match your local PostgreSQL/MySQL server.

Run the notebook to clean the data and push it to your database.

Open the .pbix file in Power BI, update the database connection settings, and refresh the data.

📁 Repository Structure
customer_shopping_behavior.csv - The raw dataset.

Data_Cleaning_and_Load.ipynb - Python notebook for cleaning and loading data.

Data_Analysis_Queries.sql - SQL scripts containing all the business questions and answers.

Customer_Behavior_Dashboard.pbix - The Power BI dashboard file.

Project_Presentation.pdf - AI-generated presentation deck for stakeholders.
