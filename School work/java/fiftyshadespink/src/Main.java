import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int counter = 0;
        for (int i = 0; i < N; i++) {
            String txt = scan.next();
            txt = txt.toLowerCase();
            if (txt.contains("pink") || txt.contains("rose")) {
                counter++;
            }
        }
        if (counter > 0) {
            System.out.println(counter);
        } else {
            System.out.println("I must watch Star Wars with my daughter");
        }
    }
}