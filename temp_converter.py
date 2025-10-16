def get_temp_scale():
    while True:
        temp = input("Is your temperature in Celsius or Fahrenheit? ").strip().lower()
        if temp in ("celsius", "c"):
            return "celsius"
        elif temp in ("fahrenheit", "f"):
            return "fahrenheit"
        else:
            print("Invalid input! Please enter 'Celsius' or 'Fahrenheit'.")

def main():
    scale = get_temp_scale()
    if scale == "celsius":
        try:
            temp_c = float(input("Enter your temperature in Celsius: "))
            temp_f = (temp_c * 9/5) + 32
            print(f"Your converted temperature is {temp_f:.2f} Fahrenheit.")
        except ValueError:
            print("Invalid temperature value.")
    else:
        try:
            temp_f = float(input("Enter your temperature in Fahrenheit: "))
            temp_c = (temp_f - 32) * 5/9
            print(f"Your converted temperature is {temp_c:.2f} Celsius.")
        except ValueError:
            print("Invalid temperature value.")

if __name__ == "__main__":
    main()