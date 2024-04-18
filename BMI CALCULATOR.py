import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class BMI_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.weight_label = tk.Label(root, text="Weight (kg):")
        self.weight_label.grid(row=0, column=0, padx=5, pady=5)

        self.weight_entry = tk.Entry(root)
        self.weight_entry.grid(row=0, column=1, padx=5, pady=5)

        self.height_label = tk.Label(root, text="Height (cm):")
        self.height_label.grid(row=1, column=0, padx=5, pady=5)

        self.height_entry = tk.Entry(root)
        self.height_entry.grid(row=1, column=1, padx=5, pady=5)

        self.calculate_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.history_button = tk.Button(root, text="View History", command=self.view_history)
        self.history_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get()) / 100  # convert cm to meters
            bmi = weight / (height ** 2)
            category = self.classify_bmi(bmi)
            self.result_label.config(text=f"Your BMI is: {bmi:.2f} ({category})")
            self.save_to_history(weight, height, bmi, category)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for weight and height.")

    def classify_bmi(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def save_to_history(self, weight, height, bmi, category):
        with open("bmi_history.txt", "a") as file:
            file.write(f"Weight: {weight} kg, Height: {height} m, BMI: {bmi:.2f}, Category: {category}\n")

    def view_history(self):
        try:
            with open("bmi_history.txt", "r") as file:
                history = file.read()
            messagebox.showinfo("BMI History", history)
        except FileNotFoundError:
            messagebox.showinfo("BMI History", "No history available.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()
