import java.util.Scanner;
/** 
 * @author Sourabh Ninawe
 */
class Pattern5{
    public void printPattern5(int n){
        for(int i=n;i>=1;i--){
            for(int j=i;j>=1;j--){
                System.out.print("*");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        while(true){
            System.out.println("Enter the number of lines to print pattern 5 in integer and -1 to exit");
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            if(n<=0)
                break;
            else{
                Pattern5 p5 = new Pattern5();
                p5.printPattern5(n);
            }
        }
    }
}