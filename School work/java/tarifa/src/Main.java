import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int X = scan.nextInt();
        int N = scan.nextInt();
        int left = 0;
        int i = 0;
        while (i < N){
            left += X;
            int P = scan.nextInt();
            left -= P;
            i++;
        }
        left += X;
        System.out.println(left);
    }
}