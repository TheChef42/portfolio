import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int L = scan.nextInt();
        int D = scan.nextInt();
        int X = scan.nextInt();
        int N = 0;
        int M = 0;
        for(int i = L;i <= D; i++) {
            N = 0;
            int ii = i;
            while (ii!= 0) {
                N = N + ii % 10;
                ii = ii/10;
            }
            if (N == X){
                N = i;
                break;
            }
        }
        for(int i = D;i >= L; i--){
            M = 0;
            int ii = i;
            while (ii!= 0) {
                M = M + ii % 10;
                ii = ii/10;
            }
            if (M == X){
                M = i;
                break;
            }
        }
        System.out.println(N);
        System.out.println(M);
    }
}