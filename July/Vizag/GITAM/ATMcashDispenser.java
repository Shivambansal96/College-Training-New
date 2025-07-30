import java.util.Scanner;

class ATMcashDispenser {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the amount you want to withdraw = ");
        int amount = sc.nextInt();

        if(amount <= 0) {
            System.out.println("Amount should be greater than 0.");
            return;
        }

        int[] notes = {2000, 500, 200, 100, 50, 20, 10, 5, 2, 1};

        int totalNotes = 0;

        for(int i = 0; i < notes.length; i++) {
            int count = amount / notes[i];

            if(count > 0) {
                System.out.println(notes[i] + ": " + count);
                totalNotes += count;
                amount -= (notes[i] * count);
            }
        }

        System.out.println("Total notes withdrawn = " + totalNotes);


    }

}