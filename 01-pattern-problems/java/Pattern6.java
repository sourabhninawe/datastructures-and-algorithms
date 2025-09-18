import java.util.Scanner;
/** 
 * @author Sourabh Ninawe
 */
class Pattern6{
    public void printPattern6(int n){
        for(int i=n;i>=1;i--){
            for(int j=1;j<=i;j++){
                System.out.print(j);
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        while(true){
            System.out.println("Enter the number of lines to print pattern 6 in integer and -1 to exit");
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            if(n<=0)
                break;
            else{
                Pattern6 p6 = new Pattern6();
                p6.printPattern6(n);
            }
        }
    }
}