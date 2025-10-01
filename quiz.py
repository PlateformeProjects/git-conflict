def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def main():
    x = 5
    y = 10
    print("Add:", add_numbers(x, y))
    print("Multiply:", multiply_numbers(x, y))
    result = add_numbers(x, y) * 3  # <- conflict
    print("Result:", result)

if __name__ == "__main__":
    main()
