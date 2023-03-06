import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String[] in = new String[5];
        int[] out = new int[5];

        for (int i =0; i<5; i++){
            in[i] = scan.next();
        }
        int k = 0;
        for (int i = 0; i <5; i++){
            if(in[i].contains("FBI")){
                System.out.print(i+1 + "\t");
                k = 1;
            }
        }
        if (k != 1){
            System.out.print("HE GOT AWAY!");
        }
    }
}