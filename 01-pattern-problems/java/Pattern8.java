import java.util.Scanner;
/** 
 * @author Sourabh Ninawe
 */
class Pattern8{
    public void printPattern8(int n){
        for(int i=n;i>=1;i--){
            for(int j=0;j<n-i;j++){
                System.out.print(" ");
            }
            for(int k=1;k<=i;k++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        while(true){
            System.out.println("Enter the number of lines to print pattern 8 in integer and -1 to exit");
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            if(n<=0)
                break;
            else{
                Pattern8 p8 = new Pattern8();
                p8.printPattern8(n);
            }
        }
    }
}