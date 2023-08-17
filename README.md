# Revenue Enhancement: Optimizing Sales Strategies through Regional and Customer Analysis with Python and Excel
## Introduction
In this analysis, I utilized Python to delve into sales data from diverse regions, extracting valuable insights on product category performance, growth opportunities, and targeted sales strategies. Excel was employed for data visualization, creating informative graphs and charts that enhance the understanding of the data.


## Guiding Questions
-	Which regions have the highest sales?
-	Which regions have the lowest sales?
-	Which product category had the highest sales across all regions?
-	How do monthly sales patterns of products vary throughout the year?
-	How is the sales distribution among different customer segments?
-	What is the distribution of order priorities and their corresponding sales percentages?
-	Which shipping mode is mostly used and what percentage of total sales does it account for?

## Tools Used
Microsoft Excel, Jupyter Notebook, Python

## Analysis
```ruby
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
```


## Dashboard
### link to dashboard
https://1drv.ms/x/s!Ah_OiE5H4-WSgRsK5v2_fT5K07Pz?e=MBWftD
![Screenshot 2023-07-07 114058](https://github.com/Kadiis/Sales-Analysis/assets/106782819/1b22cc2d-6a5e-46c2-844b-6126b6b390e4)



## Findings
-	Europe and Asia Pacific had the highest sales per region with total sales of $2,728,601 and $2,533,843 respectively.
-	Africa had the lowest sales per region with a total sale of $652,922.
-	Technology products have the highest sales in all regions except LATAM, where Furniture has the highest sales.	
-	The month of November consistently showed higher sales across all three categories, while February consistently displayed lower sales across all three categories throughout the years.
-	The Consumer segment consistently generated the highest sales across all three years, followed by the corporate segment, and then the home Office segment.
-	Most orders have medium priority, which accounts for 58% of total sales.
-	The most used shipping mode is Standard Class, which accounts for 60% of total sales.

## Recommendations
#####  1. Focus on Europe and Asia Pacific: 
Since these regions have the highest sales, it would be beneficial to allocate more resources and marketing efforts towards these areas. Identify the factors contributing to the high sales in these regions and leverage them to further increase market penetration and sales.
##### 2. Explore opportunities in Africa: 
While Africa has the lowest sales currently, it represents an untapped market with potential for growth. Conduct market research to understand the reasons behind the low sales and identify strategies to overcome challenges. Consider adapting products or services to meet the specific needs and preferences of the African market.
##### 3. Tailor product offerings: 
Recognize the difference in sales trends between LATAM and other regions. In LATAM, furniture has the highest sales while technology products dominate in other regions. Adjust the product offerings in each region to align with customer preferences and market demands. This may involve diversifying the product range or customizing existing products to cater to specific regional needs.
##### 4.Leverage high sales months: 
November consistently show higher sales across all categories. Capitalize on this trend by launching new marketing campaigns, offering promotions, or introducing new product lines during these months. Allocate resources strategically to maximize sales during this period.
##### 5.	Prioritize the Consumer segment: 
The Consumer segment consistently generates the highest sales. Allocate resources and marketing efforts to further strengthen relationships with consumers, identify their needs and preferences, and continuously innovate to meet their demands. Develop loyalty programs and personalized marketing strategies to enhance customer retention and increase sales.
##### 6.	Optimize order fulfillment: 
Since most orders have medium priority, streamline the order fulfillment process to ensure timely delivery and customer satisfaction. Evaluate and improve internal processes, logistics, and supply chain management to fulfill orders efficiently. Additionally, consider incentivizing customers to opt for higher priority orders, potentially increasing overall sales.
##### 7.	Enhance shipping options: 
With Standard Class being the most used shipping mode, optimize the logistics network to ensure efficient and cost-effective delivery. However, consider diversifying shipping options by offering faster delivery services or additional shipping features, such as package tracking or expedited shipping, to cater to customers who value speed and convenience. This can attract new customers and potentially increase sales.
