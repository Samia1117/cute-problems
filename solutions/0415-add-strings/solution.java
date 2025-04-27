class Solution {
    public String addStrings(String num1, String num2) {

        int carry = 0;
        StringBuilder sb = new StringBuilder();

        int m = num1.length() - 1;
        int n = num2.length() - 1;

        while (m >= 0 && n >= 0) {
            int d1 = Integer.valueOf(Character.toString(num1.charAt(m)));
            int d2 = Integer.valueOf(Character.toString(num2.charAt(n)));

            int sum = d1 + d2 + carry;
            // System.out.println("Sum = " + sum);
            int remainder = sum % 10;
            // System.out.println("Remainder = " + remainder);
            sb.append(remainder);
            carry = sum / 10;

            m--;
            n--;
        }

        while (m >= 0) {
            int sum = Integer.valueOf(Character.toString(num1.charAt(m))) + carry;
            int remainder = sum % 10;
            sb.append(remainder); 
            carry = sum / 10;
            m--;
        }

        while (n >= 0) {
            int sum = Integer.valueOf(Character.toString(num2.charAt(n))) + carry;
            int remainder = sum % 10;
            sb.append(remainder); 
            carry = sum / 10;
            n--;
        }

        if (carry != 0) {
            sb.append(carry);
        }

        return sb.reverse().toString();
    }
}
