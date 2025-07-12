# BMI Calculator - Oasis Infobyte Python Internship

def calculate_bmi():
    print("=== BMI Calculator ===")
    
    try:
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))
        
        bmi = weight / (height ** 2)
        print(f"\nYour BMI is: {bmi:.2f}")
        
        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            print("Category: Overweight")
        else:
            print("Category: Obese")
    
    except ValueError:
        print("Please enter valid numbers.")

# Run the function
calculate_bmi()
