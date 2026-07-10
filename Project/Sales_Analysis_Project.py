import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
try:
    df = pd.read_csv("data/sales_data.csv")
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: sales_data.csv not found.")
    exit()

# Group data by Product
product_sales = df.groupby("Product")["Total_Sales"].sum()

# Create bar chart
product_sales.plot(kind="bar", color="skyblue")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()

# Save chart
plt.savefig("visualization/product_sales.png")

# Display chart
plt.show()