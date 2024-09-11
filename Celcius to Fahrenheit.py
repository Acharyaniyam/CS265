import os

def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    temperature = float(input("Enter temperature: "))
    unit = input("Enter unit (C/F): ").upper()

    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(temperature)
        print(f"{temperature} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(temperature)
        print(f"{temperature} Fahrenheit is equal to {celsius:.2f} Celsius.")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    # Read environment variable
    message = os.getenv("CUSTOM_MESSAGE")
    if message:
        print("Environment variable message:")
        print(message)

if __name__ == "__main__":
    main()
