import java.util.*;

public class egypt {
    public static void main(String args[])  {
        int i = 0;
        Scanner scan = new Scanner(System.in);
            while (i < 1000) {
                int in[] = new int[3];
                in[0] = scan.nextInt();
                in[1] = scan.nextInt();
                in[2] = scan.nextInt();
                if (in[0] == 0 && in[1] == 0 && in[2] == 0) {
                    break;
                }
                Arrays.sort(in);
                int c = in[2] * in[2];
                int ab = (in[1] * in[1] + in[0] * in[0]);
                if (c == ab) {
                    System.out.println("right");
                } else {
                    System.out.println("wrong");
                } i++;
            }
        }
    }

