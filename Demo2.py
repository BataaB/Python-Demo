def is_numeric(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

numbers = [1, 2.5, 3, 4.5, 5]

for num in numbers:
    # print(f"{num} is{"" if is_numeric(num) else " not"} numeric.")
    print(f"{num} is numeric: {is_numeric(num)}")