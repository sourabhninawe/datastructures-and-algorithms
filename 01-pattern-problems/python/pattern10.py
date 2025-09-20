
# Author: Sourabh Ninawe
class pattern10:
    def print_pattern10_method1(self, n):
        print("pattern10:Method1")
        for i in range(1, n+1):
            for j in range(1, i):
                print(" ", end='')
            for k in range(1,n-i+2):
                print(k, end='')
            print()

    #shorter implementation
    def print_pattern10_method2(self, n):
        print("pattern10:Method2")
        for i in range(1, n+1):
            print(' '*(i-1) + ''.join(str(k) for k in range(1, n-i+2)))

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of lines to print pattern 10 (integer, 0 or negative to exit): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if n <= 0:
            break
        else:
            p10 = pattern10()
            p10.print_pattern10_method1(n)
            p10.print_pattern10_method2(n)
