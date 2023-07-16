#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


# In[2]:


files = [file for file in os.listdir(r"C:\Users\kadir\Downloads\Sales Analysis")]
for file in files:
    print(file)


# In[3]:


path = r"C:\Users\kadir\Downloads\Sales Analysis"
all_data = []  # Create an empty list to store the DataFrames
for file in files:
    current_df = pd.read_csv(path + "/" + file)
    all_data.append(current_df)  # Append each DataFrame to the list

combined_data = pd.concat(all_data)  # Concatenate all the DataFrames in the list
combined_data.shape


# ## Data Cleaning

# In[4]:


# Check for duplicates
duplicates = combined_data.duplicated()

# Display the DataFrame with a new column indicating duplicates
combined_data['IsDuplicate'] = duplicates

# Display the DataFrame
print(combined_data)


# In[5]:


rows_with_missing = combined_data[combined_data.isnull().any(axis=1)]
print(rows_with_missing)


# In[6]:


missing_columns = combined_data.isnull().sum()
print(missing_columns)


# In[7]:


combined_data.dtypes


# In[8]:


combined_data['Sales'].unique()


# In[9]:


# Remove dollar signs and commas, then convert to float
combined_data['Sales'] = combined_data['Sales'].replace({'\$': '', ',': ''}, regex=True).astype(float)


# In[10]:


print(combined_data)


# ##  Analysis

# In[11]:


# Which regions have the highest sales?
highest_sales_regions = combined_data.groupby('Market')['Sales'].sum().nlargest(1)
print("Regions with the highest sales:")
print(highest_sales_regions)


# In[12]:


# Which regions have the lowest sales?
regions_lowest_sales = combined_data.groupby('Market')['Sales'].sum().nsmallest(1)
print("\nRegions with the lowest sales:")
print(regions_lowest_sales)


# In[13]:


# Which product category had the highest sales across all regions?
category_highest_sales = combined_data.groupby('Category')['Sales'].sum().idxmax()
print(f"\nProduct category with the highest sales across all regions: {category_highest_sales}")


# In[14]:


# Convert the 'Order Date' column to datetime format
combined_data['Order Date'] = pd.to_datetime(combined_data['Order Date'], format='%d/%m/%Y')

# Filter data for each year
combined_data_2020 = combined_data[combined_data['Order Date'].dt.year == 2020]
combined_data_2021 = combined_data[combined_data['Order Date'].dt.year == 2021]
combined_data_2022 = combined_data[combined_data['Order Date'].dt.year == 2022]

# Calculate monthly sales for each year
monthly_sales_2020 = combined_data_2020.groupby(combined_data_2020['Order Date'].dt.month)['Sales'].sum()
monthly_sales_2021 = combined_data_2021.groupby(combined_data_2021['Order Date'].dt.month)['Sales'].sum()
monthly_sales_2022 = combined_data_2022.groupby(combined_data_2022['Order Date'].dt.month)['Sales'].sum()

# Plotting the monthly sales for each year
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales_2020.index, monthly_sales_2020.values, label='2020', marker='o')
plt.plot(monthly_sales_2021.index, monthly_sales_2021.values, label='2021', marker='o')
plt.plot(monthly_sales_2022.index, monthly_sales_2022.values, label='2022', marker='o')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales Patterns (2020, 2021, 2022)')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.grid(True)
plt.show()


# In[15]:


# How is the sales distribution among different customer segments?
segment_sales_distribution = combined_data.groupby('Segment')['Sales'].sum()
print("\nSales distribution among different customer segments:")
print(segment_sales_distribution)


# In[16]:


# What is the distribution of order priorities and their corresponding sales percentages?
order_priority_distribution = combined_data.groupby('Order Priority')['Sales'].sum()
total_sales = combined_data['Sales'].sum()
order_priority_sales_percent = (order_priority_distribution / total_sales) * 100
print("\nDistribution of order priorities and their corresponding sales percentages:")
print(order_priority_sales_percent)


# In[17]:


# Which shipping mode is mostly used and what percentage of total sales does it account for?
shipping_mode_total_sales = combined_data.groupby('Ship Mode')['Sales'].sum()
total_sales = combined_data['Sales'].sum()
shipping_mode_sales_percent = (shipping_mode_total_sales / total_sales) * 100
print("\nSales percentage for each shipping mode:")
print(shipping_mode_sales_percent)

