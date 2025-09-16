
# Author: Sourabh Ninawe
class Pattern2:
    def print_pattern2_method1(self, n):
        print("Pattern2:Method1")
        for i in range(n):
            for j in range(i+1):
                print('*', end='')
            print()

    #shorter implementation
    def print_pattern2_method2(self, n):
        print("Pattern2:Method2")
        for i in range(1, n+1):
            print('*' * i)

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of lines to print pattern 2 (integer, 0 or negative to exit): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if n <= 0:
            break
        else:
            p2 = Pattern2()
            p2.print_pattern2_method1(n)
            p2.print_pattern2_method2(n)
