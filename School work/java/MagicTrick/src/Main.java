import java.util.*;
import java.util.stream.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String str = scan.next();
        int count;
        int trigger = 0;
        char[] ch = str.toCharArray();

        for(int i = 0; i <ch.length; i++) {
            count = 1;
            for(int j = i+1; j <ch.length; j++) {
                if(ch[i] == ch[j] && ch[i] != ' ') {
                    count++;
                    //Set string[j] to 0 to avoid printing visited character
                    ch[j] = '0';
                }
            }
            //A character is considered as duplicate if count is greater than 1
            if(count > 1 && ch[i] != '0') {
                trigger = 1;
                break;
            }
        }
        if (trigger == 1){
            System.out.println(0);
        }else {
            System.out.println(1);
        }
    }
}