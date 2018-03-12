from .calc import calculator

def main():
    left = input('Give me a left: ')

    right = input('Give me a right: ')

    results = calculator(int(left), int(right))
    print(results)
