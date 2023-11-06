def filter_numbers(expression, numbers):
    for number in numbers:
        x, y = divmod(number, 10)
        if eval(expression.replace("x", str(x)).replace("y", str(y))):
            print(x, y)

def main():
    expression = "x==y*3"
    numbers = [62, 5, 9, 3]
    filter_numbers(expression, numbers)
main()