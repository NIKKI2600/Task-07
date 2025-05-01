# Task-07
# Sales Data Analysis

This project processes sales data using SQLite and Python. The data is loaded from an Excel file, stored in a SQLite database, and then analyzed using SQL queries and Pandas.

The database file, `sales_data.db`, contains a `sales` table with the following columns:
- `Order ID`
- `Quantity`
- `Product Name`
- `Sales`
- `Order Date`
- `City`

After loading the data, SQL queries summarize total quantity sold and revenue for each product. The summary includes:
- Product names
- Total quantity sold
- Total revenue generated per product

The final step visualizes the revenue distribution using a bar chart. The chart is saved as `sales_chart.png` and provides a clear breakdown of revenue across products.
