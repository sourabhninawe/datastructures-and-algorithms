import java.util.Scanner;
/** 
 * @author Sourabh Ninawe
 */
class Pattern4{
    public void printPattern4(int n){
        for(int i=1;i<=n;i++){
            for(int j=1;j<=i;j++){
                System.out.print(i);
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        while(true){
            System.out.println("Enter the number of lines to print pattern 4 in integer and -1 to exit");
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            if(n<=0)
                break;
            else{
                Pattern4 p4 = new Pattern4();
                p4.printPattern4(n);
            }
        }
    }
}