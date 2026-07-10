import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
try:
    df = pd.read_csv("data/sales_data.csv")
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: sales_data.csv not found in the data folder.")
    exit()

# Create histogram
df["Total_Sales"].plot(kind="hist", bins=10)

plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")

plt.savefig("visualization/sales_histogram.png")

plt.show()