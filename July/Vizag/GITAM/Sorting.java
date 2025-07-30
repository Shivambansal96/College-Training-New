class Sorting {
    public static void main(String[] args) {
        String b = "101101";

        int res = 0, powOf2 = 1;

        for(int i = b.length()-1; i >= 0; i--) {
            if(b.charAt(i) == '1') {
                res = res + powOf2;
            }
            powOf2 = powOf2 * 2;
        }

        System.out.println(res);

    }
}
