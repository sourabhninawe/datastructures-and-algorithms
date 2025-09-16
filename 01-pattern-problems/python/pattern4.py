
# Author: Sourabh Ninawe
class pattern4:
    def print_pattern4_method1(self, n):
        print("pattern4:Method1")
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(i, end='')
            print()

    #shorter implementation
    def print_pattern4_method2(self, n):
        print("pattern4:Method2")
        for i in range(1, n+1):
            print(str(i)*i)

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of lines to print pattern 4 (integer, 0 or negative to exit): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if n <= 0:
            break
        else:
            p3 = pattern4()
            p3.print_pattern4_method1(n)
            p3.print_pattern4_method2(n)
