
# Author: Sourabh Ninawe
class pattern6:
    def print_pattern6_method1(self, n):
        print("pattern6:Method1")
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print(j, end='')
            print()

    #shorter implementation
    def print_pattern6_method2(self, n):
        print("pattern6:Method2")
        for i in range(n, 0, -1):
            print(''.join(str(j) for j in range(1,i+1)))

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of lines to print pattern 6 (integer, 0 or negative to exit): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if n <= 0:
            break
        else:
            p6 = pattern6()
            p6.print_pattern6_method1(n)
            p6.print_pattern6_method2(n)
