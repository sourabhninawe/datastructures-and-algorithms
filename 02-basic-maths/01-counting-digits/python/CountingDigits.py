import math

class CountingDigits:
    def count_digits_method1(self, n):
        count = 0
        while n > 0:
            count += 1
            n //= 10  # Integer division
        return count

    def count_digits_method2(self, n):
        if n == 0:
            return 1
        return int(math.floor(math.log10(n))) + 1
    
def main():
    c = CountingDigits()
    print("Enter the number whose digits have to be calculated and enter 0 or a negative number to exit")
    num = int(input())
    while num > 0:
        print("Method 1 number of digits calculated:")
        print(c.count_digits_method1(num))
        print("Method 2 number of digits calculated:")
        print(c.count_digits_method2(num))
        print("Enter the number whose digits have to be calculated and enter 0 or a negative number to exit")
        num = int(input())

if __name__ == "__main__":
    main()