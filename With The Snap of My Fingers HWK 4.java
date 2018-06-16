package with_snap_of_my_fingers;

import java.util.Scanner;

// Name = D. Duong

public class final_hw {

	public static int calculateNameScore(String names) { // Creates a function, which is called Methods
															// calculateNameScore. Returns an integer.

		int total = 0; // Sets int total = 0
		for (int i = 0; i < names.length(); i++) { // For loop meant to count character length
			char z = names.charAt(i); // use z here.

			if (Character.isLetter(z)) { // Built in function for is.Letter checks ignores any non letter characters such as apostrophes, spaces, etc.
				int value = (int) z;
				total += z;

			}
		}

		//System.out.println(total); // Testing purposes only.
		return total; // Beware: return goes after the iteration of a for loop because if you use
						// return in the 1st ending brace, then it will end it there.

	}

	public static boolean isWinner(String status) {
		int total = calculateNameScore(status); // Calls calculateNameScore

		int character = status.length(); // set character = the length of status

		if ((total / character)  % 2 == 0) { // Conditions for determining if a user name is a winner or not based on Friday's Formula. Length of 0 = Winner.
			return true;
		}

		else { // If leftover, then name is a loser.
			return false;
		}

	}

	public static String getName() { // Takes no parameters at all
		Scanner input = new Scanner(System.in); // Constructs a scanner
		System.out.println("Please enter your name: "); // Part 1 of user input
		String name = input.nextLine(); // Part 2 of user input - Asks user to "Enter their name: "

		while (name.length() == 0) { // Validation when a user inputs a blank string
			System.out.println("Please enter your name: "); // Part 1 of user input.
			name = input.nextLine(); // Part 2 of user input - Asks user to "Enter their name: "

		}

		return name; // Don't put return name in while loop because it will mess with getName(); and ruin the output of the function.

	}

	public static void main(String[] args) { // Main Method
		//calculateNameScore("T'Challa"); // Testing Purposes Only
		//calculateNameScore("Melvin Lax"); // Testing Purposes Only
		//calculateNameScore("Bo Fu"); // Testing Purposes Only
		//calculateNameScore("Nebula"); // Testing Purposes Only
		//calculateNameScore("Neal Terrell"); // Testing Purposes Only
		//calculateNameScore("Donald Trump"); // Testing Purposes Only
		String name = getName(); // Call getName into main Method. Set String name equal to the function getName();
		
		
		while (! (name.equals("quit"))) {
			boolean character = isWinner(name); //Call isWinner as a boolean variable. // When calling a function, you must understand what type of data being sent. we want to determine if name is winner or not.	
			if ((character == true)) { // Person wins ...
			System.out.println("Congratulations, " + name + ". " + "You win! "); // equivalent to python form of printing
		 }

			else  { // Else person loses, ...
				System.out.println("Sorry, " + name +  ". " + "You have to go now."); // equivalent to python form of printing
		 
		 }
			
		 name = getName(); // Call for user input in the loop after the else.
		 

	}

}

}


