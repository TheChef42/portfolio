import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int X,Y,N;
        X = scan.nextInt();
        Y = scan.nextInt();
        N = scan.nextInt();
        for (int i = 1; i <= N; i++){
            if(i%X ==0 && i%Y == 0){
                System.out.println("FizzBuzz");
            } else if (i%X ==0) {
                System.out.println("Fizz");
            } else if (i%Y==0) {
                System.out.println("Buzz");
            } else {
                System.out.println(i);
            }
        }
    }
}