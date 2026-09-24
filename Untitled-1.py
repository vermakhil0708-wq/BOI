def add(a, b):
    return a + b

def main():
    try:
        x = float(input("Enter first number: ").strip())
        y = float(input("Enter second number: ").strip())
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    result = add(x, y)
    print(f"The sum of {x} and {y} is {result}")

if __name__ == "__main__":
    main()