# prompt: create a diet chart for thyroid patients for 10 patients

import pandas as pd
import matplotlib.pyplot as plt
# Create a sample diet plan for thyroid patients
sample_diet_plan = {
  "Breakfast": "Oatmeal with berries and nuts",
  "Lunch": "Grilled chicken salad with quinoa",
  "Dinner": "Baked salmon with roasted vegetables",
  "Snacks": "Fruits, vegetables, yogurt, nuts"
}

# Create a data set of thyroid patients
data = {
  "Patient ID": list(range(1, 11)),
  "Age": [25, 30, 40, 50, 60, 70, 80, 90, 100, 110],
  "Gender": ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F"],
  "Weight (kg)": [60, 70, 80, 90, 100, 110, 120, 130, 140, 150],
  "Height (cm)": [160, 170, 180, 190, 200, 210, 220, 230, 240, 250],
  "Diet Plan": ["Low-carb", "Low-fat", "Mediterranean", "Vegetarian", "Paleo", "Low-carb", "Low-fat", "Mediterranean", "Vegetarian", "Paleo"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print the sample diet plan
print("Sample Diet Plan for Thyroid Patients:\n")
for meal, option in sample_diet_plan.items():
    print(f"{meal}: {option}")

# Calculate the percentage of patients on each diet plan
diet_counts = df["Diet Plan"].value_counts()
diet_percentages = diet_counts / len(df) * 100

# Create a pie chart
plt.figure(figsize=(10, 7))
plt.pie(diet_percentages, labels=diet_counts.index, autopct="%1.1f%%")
plt.title("Diet Chart for Thyroid Patients (n=%d)" % len(df))
plt.show()
