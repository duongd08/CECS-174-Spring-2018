package Java;
import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;

//This code is golden perfect to the point where it matches exactly with the example output.

//String name = "D. Duong";

public class Lab1 {

	public static void printguestNames(ArrayList<String> p) {
		// To sort an array list, use the method sort() from the Collections
		//framework
		
		
		
		
		//Enhanced for loop: Iterates through list p, assigns the variable
		//name to each element at every iteration.
		int i = 1;
		for(String name : p)
		{
			System.out.printf("%d. %s\n", i, name);
			i++;
		}

	}
	
	
	public static void main(String[] args) {
		ArrayList<String> guestNum =  new ArrayList<String>(); // Declaring an Array List of the names of the people.
		
		Scanner in = new Scanner(System.in); // Gets user input from keyboard. Mandatory Line to remember on top of head.
		
		System.out.println("Let's get this party started! Enter the date of your event:");
		String date = in.nextLine(); // Declaring the date as a string and input.
		System.out.println();
		
		System.out.println("Good.  Now, what would you like to call your event? ");
		String event = in.nextLine(); // Declaring the event as a string and input.
		System.out.println();
		
		System.out.println("What is the maximum amount of guests allowed? ");
		int maxGuests = Integer.parseInt(in.nextLine().trim()); // Converts the max number of people invited as a string into an integer.
		System.out.println();
		
		System.out.println("Thank you.  Please enter the name of each guest followed by ENTER.  When you are done, enter DONE."); // This line must before the while loop because if it stays, then this will repeat many times until the user puts "DONE". ONLY ONCE!
		String nameList; // Declaring nameList as a string, otherwise java will read it as a syntax error.
		System.out.println();
		
		do {
			
			System.out.print("Guest Name: ");
			nameList = in.nextLine(); // Input for names.
			
			
			//if(nameList.equals("DONE")) { // If the user inputs "DONE", then it is supposed to stop counting names. 
				//guestNum.remove("DONE"); //supposed to remove "DONE" from the guest list, not counting it as a name.
			//} THIS GOES INSIDE THE FIRST IF CONDITON!!!
			
			if(!nameList.equals("DONE")); { // If the user inputs anything other than "DONE", then it appends names onto the guest list, counting it as a name.
				guestNum.add(nameList);
				
			} if (nameList.equals("DONE")); // Nested If-Conditions in Java. If the user inputs "DONE", then it is supposed to stop counting names. 
			guestNum.remove("DONE"); // //Supposed to remove "DONE" from the guest list, not counting it as a name.
			
			
		} while(!nameList.equals("DONE"));
		
		System.out.println(); // Spacing Consistency.
		
		System.out.print("This is the information on your: ");
		System.out.println(event);
		System.out.println(); // The purpose of this line is to seperate the event from the date.
		
		System.out.print("Date: ");
		System.out.println(date);
		System.out.println(); // The purpose of this line is to seperate the date from the maxGuests.
		
		
		System.out.print("The Max Num. of Guests: ");
		System.out.println(maxGuests);
		System.out.println(); // The purpose of this line is to seperate the maxGuests from the guest list.
		
		System.out.print("Current Num. of Guests: ");
		System.out.println(guestNum.size()); // .size lets you know how long the length of the guest list.
		System.out.println(); // The purpose of this line is to seperate the guest list from the entire list of names.
		
		System.out.println("Current Guests: ");
		System.out.println(); // Spacing consistency.
		printguestNames(guestNum); // Calls method: public static void printguestNames(ArrayList<String> p)
		
		System.out.println(); // Spacing consistency.
		System.out.println("Have a fun party!\n");
		
		
		
				

	}

}
