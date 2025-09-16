import java.util.Scanner;
/** 
 * @author Sourabh Ninawe
 */
class Pattern3{
    public void printPattern3(int n){
        for(int i=1;i<=n;i++){
            for(int j=1;j<=i;j++){
                System.out.print(j);
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        while(true){
            System.out.println("Enter the number of lines to print pattern 1 in integer and -1 to exit");
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            if(n<=0)
                break;
            else{
                Pattern3 p3 = new Pattern3();
                p3.printPattern3(n);
            }
        }
    }
}