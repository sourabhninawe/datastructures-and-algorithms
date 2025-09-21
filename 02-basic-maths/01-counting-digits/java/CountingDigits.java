import java.util.Scanner;
import java.lang.Math;
public class CountingDigits{

    public int countDigitsMethod1(int n){
        int count=0;
        while(n>0){
            count++;
            n/=10;
        }
        return count;
    }

    public int countDigitsMethod2(int n){
        if (n == 0) {
            return 1;
        }
        return (int) Math.floor(Math.log10(n)) + 1;
    }

    public static void main(String args[]){
        CountingDigits c = new CountingDigits();
        System.out.println("Enter the numer whose digits have to be calculated and enter 0 or a negative number to exit");
        int num = new Scanner(System.in).nextInt();
        while(num>0){
            System.out.println("Method 1 number of digits calculated:");
            System.out.println(c.countDigitsMethod1(num));
            System.out.println("Method 2 number of digits calculated:");
            System.out.println(c.countDigitsMethod2(num));
            System.out.println("Enter the numer whose digits have to be calculated and enter 0 or a negative number to exit");
            num = new Scanner(System.in).nextInt();
        }
    }
}