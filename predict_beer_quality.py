import tkinter as tk
from tkinter import messagebox
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the trained model
model = joblib.load(r'C:\Users\suraj\OneDrive\Desktop\7 sem\ML\naive_bayes_model.pkl')

# Initialize the scaler (ensure it’s the same scaler used during training)
scaler = StandardScaler()

# Define a function for prediction
def predict_quality():
    try:
        # Get user input values from entry widgets
        features = {
    
            'volatile acidity': float(entry_volatile_acidity.get()),
            'citric acid': float(entry_citric_acid.get()),
            'chlorides': float(entry_chlorides.get()),
            'density': float(entry_density.get()),
            'sulphates': float(entry_sulphates.get()),
            'alcohol': float(entry_alcohol.get())
        }
        
        # Convert to DataFrame
        input_data = pd.DataFrame([features])
        
        # Scale the input data
        input_scaled = scaler.fit_transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)
        
        # Display the prediction
        messagebox.showinfo("Prediction Result", f"Predicted Wine Quality: {prediction[0]}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Wine Quality Prediction")
root.geometry("400x500")

# Labels and Entry widgets for each feature
tk.Label(root, text="Fixed Acidity").pack()
entry_fixed_acidity = tk.Entry(root)
entry_fixed_acidity.pack()

tk.Label(root, text="Volatile Acidity").pack()
entry_volatile_acidity = tk.Entry(root)
entry_volatile_acidity.pack()

tk.Label(root, text="Citric Acid").pack()
entry_citric_acid = tk.Entry(root)
entry_citric_acid.pack()

tk.Label(root, text="Chlorides").pack()
entry_chlorides = tk.Entry(root)
entry_chlorides.pack()

tk.Label(root, text="Density").pack()
entry_density = tk.Entry(root)
entry_density.pack()

tk.Label(root, text="pH").pack()
entry_ph = tk.Entry(root)
entry_ph.pack()

tk.Label(root, text="Sulphates").pack()
entry_sulphates = tk.Entry(root)
entry_sulphates.pack()

tk.Label(root, text="Alcohol").pack()
entry_alcohol = tk.Entry(root)
entry_alcohol.pack()

# Button to trigger prediction
predict_button = tk.Button(root, text="Predict Quality", command=predict_quality)
predict_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()