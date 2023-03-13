import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        while (true) {
            int n = scan.nextInt();
            if (n == -1) {
                break;
            }
            int time = 0;
            int distance = 0;
            for (int i = 0; i < n; i++) {
                int s = scan.nextInt();
                int t = scan.nextInt();

                time = t - time;

                distance += (time * s);
                time = t;
            }
            System.out.println(distance + " miles");
        }
    }
}