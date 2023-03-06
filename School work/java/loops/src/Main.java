import java.util.Arrays;
import java.util.Objects;
import java.util.Scanner;

import static java.lang.Math.sqrt;

public class Main {
    public static void main(String[] args) {
        int array[] = {1,2,3,4,5};
        for (int i = 0; i < array.length; i++){
            System.out.println(array[i]);
        }
        String s[] = {"1. Change password", "2. Calculate root", "3. Log out"};
        login(s);
    }
    public static void login(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = "password";
        while(true){
            String in = "";
            System.out.print("Input your password: ");
            in = scan.next();
            if (Objects.equals(in, s)) {
                System.out.println("Access granted");
                System.out.println("Choose an option: " + Arrays.toString(args));
                int choice = scan.nextInt();
                switch (choice) {
                    case 1 -> {
                        s = changePassword(scan);
                        System.out.println("The new password is: " + s);
                    }
                    case 2 -> {
                        System.out.println("2. Calculate root, input a double, that you want to find the sqrt of:");
                        System.out.println(calculateRoot(scan.nextDouble()));
                    }
                    case 3 -> {
                        System.out.println("3. Logout goodbye, or are we ending ;).");
                    }
                }
            } else {
                System.out.println("Access denied");
                break;
            }
        }
    }

    private static String changePassword(Scanner args) {
        System.out.print("Please input a new password: ");
        return args.next();
    }
    public static double calculateRoot(double args) {
        return sqrt(args);
    }

}