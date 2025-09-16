
# Author: Sourabh Ninawe
class pattern5:
    def print_pattern5_method1(self, n):
        print("pattern5:Method1")
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print("*", end='')
            print()

    #shorter implementation
    def print_pattern5_method2(self, n):
        print("pattern5:Method2")
        for i in range(n, 0, -1):
            print('*' * i)

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of lines to print pattern 5 (integer, 0 or negative to exit): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if n <= 0:
            break
        else:
            p3 = pattern5()
            p3.print_pattern5_method1(n)
            p3.print_pattern5_method2(n)
