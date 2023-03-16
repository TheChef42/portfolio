/*
This code is an example of how to use the regex package to do input validation in Java.
Documentation used for this example is from here:
https://www.w3schools.com/java/java_regex.asp
https://regexlib.com/Default.aspx
https://www.regular-expressions.info/quickstart.html
https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html#allow-list-regular-expression-examples
https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html

Test:
https://regex101.com/
*/

import java.util.regex.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        //email test
        Pattern pattern = Pattern.compile("^\\w+@[a-zA-Z_]+?\\.[a-zA-Z]{2,3}$", Pattern.CASE_INSENSITIVE);
        System.out.println("Test email: ");
        Matcher matcher = pattern.matcher(scan.next());
        boolean matchFound = matcher.find();
        if(matchFound) {
            System.out.println("Match found");
        } else {
            System.out.println("Match not found");
        }
        //Danish CPR test
        pattern = Pattern.compile("((((0[1-9]|[12][0-9]|3[01])(0[13578]|10|12)(\\d{2}))|(([0][1-9]|[12][0-9]|30)(0[469]|11)(\\d{2}))|((0[1-9]|1[0-9]|2[0-8])(02)(\\d{2}))|((29)(02)(0(0|4|8)))|((29)(02)([2468][048]))|((29)(02)([13579][26])))[- ]?\\d{4})", Pattern.CASE_INSENSITIVE);
        System.out.println("Test cpr number: ");
        matcher = pattern.matcher(scan.next());
        matchFound = matcher.find();
        if(matchFound) {
            System.out.println("Match found");
        } else {
            System.out.println("Match not found");
        }
        // name test
        pattern = Pattern.compile("^[a-z ,.'-]+$", Pattern.CASE_INSENSITIVE);
        System.out.println("Test name: ");
        matcher = pattern.matcher(scan.next());
        matchFound = matcher.find();
        if(matchFound) {
            System.out.println("Match found");
        } else {
            System.out.println("Match not found");
        }
    }
}