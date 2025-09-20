
# Author: Sourabh Ninawe
class pattern7:
    def print_pattern7_method1(self, n):
        print("pattern7:Method1")
        for i in range(1, n+1):
            for j in range(1, n-i+1):
                print(" ", end='')
            for k in range(1,i+1):
                print("*", end='')
            print()

    #shorter implementation
    def print_pattern7_method2(self, n):
        print("pattern7:Method2")
        for i in range(1, n+1):
            print(' ' * (n - i) + '*' * i)

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of lines to print pattern 7 (integer, 0 or negative to exit): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if n <= 0:
            break
        else:
            p7 = pattern7()
            p7.print_pattern7_method1(n)
            p7.print_pattern7_method2(n)
