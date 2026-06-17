import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load stock data
df = pd.read_csv("data/stock_data.csv")

# Select only Date and Close columns
df = df[["Date", "Close"]]

# Convert Date into number format
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = df["Date"].map(pd.Timestamp.toordinal)

# Features and Target
X = df[["Date"]]
y = df["Close"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = model.score(X_test, y_test)

print("Model Accuracy:", round(accuracy, 2))

# Graph
plt.figure(figsize=(10, 5))
plt.scatter(y_test, predictions, color="blue")
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Stock Price Prediction")
plt.show()
