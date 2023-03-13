import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        int T = scan.nextInt();
        int counter = 0;

        for (int i = 0; i < n; i++){
            int task = scan.nextInt();
            if (T - task < 0){
                break;
            } else if (T-task == 0) {
                counter++;
                break;
            }
            T = T-task;
            counter++;
        }
        System.out.println(counter);
    }
}