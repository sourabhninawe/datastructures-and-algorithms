import java.util.Scanner;
/** 
 * @author Sourabh Ninawe
 */
class Pattern10{
    public void printPattern10(int n){
        for(int i=1;i<=n;i++){
            for(int j=1;j<i;j++){
                System.out.print(" ");
            }
            for(int k=1;k<=n-i+1;k++){
                System.out.print(k);
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        while(true){
            System.out.println("Enter the number of lines to print pattern 10 in integer and -1 to exit");
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            if(n<=0)
                break;
            else{
                Pattern10 p10 = new Pattern10();
                p10.printPattern10(n);
            }
        }
    }
}