import java.util.Scanner;
/** 
 * @author Sourabh Ninawe
 */
class Pattern1{
    public void printPattern1(int n){
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                System.out.print("*");
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
                Pattern1 p1 = new Pattern1();
                p1.printPattern1(n);
            }
        }
        
        
    }
}