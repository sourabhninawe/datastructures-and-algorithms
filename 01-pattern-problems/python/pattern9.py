
# Author: Sourabh Ninawe
class pattern9:
    def print_pattern9_method1(self, n):
        print("pattern9:Method1")
        for i in range(1, n+1):
            for j in range(1, n-i+1):
                print(" ", end='')
            for k in range(1,i+1):
                print(k, end='')
            print()

    #shorter implementation
    def print_pattern9_method2(self, n):
        print("pattern9:Method2")
        for i in range(1, n+1):
            print(' '*(n-i) + ''.join(str(k) for k in range(1, i+1)))

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of lines to print pattern 9 (integer, 0 or negative to exit): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if n <= 0:
            break
        else:
            p9 = pattern9()
            p9.print_pattern9_method1(n)
            p9.print_pattern9_method2(n)
