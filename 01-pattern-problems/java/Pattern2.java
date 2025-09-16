import java.util.Scanner;
/** 
 * @author Sourabh Ninawe
 */
class Pattern2{
    public void printPattern2(int n){
        for(int i=0;i<n;i++){
            for(int j=0;j<=i;j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        while(true){
            System.out.println("Enter the number of lines to print pattern 2 in integer and -1 to exit");
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            if(n<=0)
                break;
            else{
                Pattern2 p2 = new Pattern2();
                p2.printPattern2(n);
            }
        }
    }
}