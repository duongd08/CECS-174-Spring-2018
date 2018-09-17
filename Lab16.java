import java.util.Scanner;

//Daniel Duong and Matthew Machado

public class Lab16 {

	public static boolean isPrime(int num) {

		if (num % 2 == 0) {
			return false;
		}
		for (int i = 3; i <= Math.sqrt(num); i += 1) {
			
		

			if (num % i == 0) {
				return false;
				
			}
		}

		return true;

	}

	public static void main(String[] args) {
		int[] nums = new int [5];
		Scanner input = new Scanner (System.in);
		System.out.println("Please enter 5 integers: ");
		for (int i = 0; i < 5 ; i++) {
			nums[i] = input.nextInt();
		}
			
		for (int n = 0; n < 5 ; n++) {
			if (isPrime(nums[n])) {
				System.out.println(nums[n] + " is prime");
			}
					
		}
	}
		
}
