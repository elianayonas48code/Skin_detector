import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("HAM10000_metadata.csv")

print(data.head())
print(data["dx"].value_counts())

data["dx"].value_counts().plot(kind="bar")

plt.title("Skin Disease Class Distribution")
plt.xlabel("Skin Disease")
plt.ylabel("Number of Images")
plt.show()
