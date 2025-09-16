
# Author: Sourabh Ninawe
class Pattern1:
    def print_pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print('*', end='')
            print()
    
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Enter the number of lines to print pattern 1 (integer, 0 or negative to exit): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if n <= 0:
            break
        else:
            p1 = Pattern1()
            p1.print_pattern1(n)
