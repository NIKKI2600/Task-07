#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()


# In[5]:


excel_file = "C:/Users/nikhi/OneDrive/Desktop/SALES.db.xlsx"
df_excel = pd.read_excel(excel_file)


# In[6]:


# Step 2: Create SQLite database and load data
db_file = "sales_data.db"
conn = sqlite3.connect(db_file)
df_excel.to_sql('sales', conn, if_exists='replace', index=False)
print(" Data loaded into SQLite database.")


# In[7]:


print(" Excel columns:", df_excel.columns.tolist())


# In[12]:


# Connect to the database again
conn = sqlite3.connect('Sales_data.db')
cursor = conn.cursor()

# Create the table with the correct columns
cursor.execute('''
CREATE TABLE IF NOT EXISTS Sales (
    order_id INTEGER,
    quantity INTEGER,
    product_name TEXT,
    sales REAL,
    order_date TEXT,
    city TEXT
)
''')

# Commit and close connection
conn.commit()
conn.close()


# In[14]:


import sqlite3

# Reopen connection
conn = sqlite3.connect("sales_data.db")

# Now this will work
columns_info = pd.read_sql_query("PRAGMA table_info(sales);", conn)
print("Columns in the SQLite table:\n", columns_info)


# In[15]:


# Step 4: Run SQL query with correct column names
query = """
SELECT [Product Name] AS product, 
       SUM(Quantity) AS total_qty, 
       SUM(Sales) AS revenue
FROM sales
GROUP BY [Product Name]
"""
df_summary = pd.read_sql_query(query, conn)


# In[16]:


#Step 5: Print results
print("\n Basic Sales Summary:")
print(df_summary)


# In[18]:


# Step 6: Plot bar chart
plt.figure(figsize=(10,6))
df_summary.plot(kind='bar', x='product', y='revenue', legend=False)
plt.ylabel("Revenue")
plt.title("Revenue by Product")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()


# In[19]:


conn.close()

