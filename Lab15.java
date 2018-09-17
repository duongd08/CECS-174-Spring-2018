import java.util.Scanner;

// Daniel Duong and Matthew Machado

public class Lab15 {

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in); // Imports Java Scanner

		System.out.println("How far is the target? "); // Input for target distance
		double theirdistance = input.nextDouble();
		boolean hit_target = true;
		
		
		while (hit_target) {		
		System.out.println("How many kg of gunpowder? "); // Input for gunpowder
		double theirgunpowder = input.nextDouble();
		
		System.out.println("Enter the angle: "); // Input for angle
		double theirangle = input.nextDouble();


		double acceleration = 9.8; // Variables from lines 16 to line 37

		double theta = (Math.PI / 180) * theirangle;

		double velocity = 10 * theirgunpowder;

		double velocity_height = (velocity * Math.sin(theta));

		double velocity_ground = (velocity * Math.cos(theta));

		double apex = (velocity_height / acceleration);

		double time = (2 * apex);

		double total_distance = (velocity_ground * time);
		
		double remainder = (theirdistance - total_distance);
		

			
			if (theirdistance - total_distance > 1) { // distance landed past target
				
			
			System.out.printf("Your shot landed: %.2f short of the target\n", Math.abs(remainder));
			
			}
		
			else if (total_distance - theirdistance > 1) { // distance landed before target
			
				System.out.printf("Your shot landed: %.2f past the target\n", Math.abs(remainder));
			
			}
			
			else {
				System.out.println("Your shot hit the target!");
				hit_target = false; // Set loop = false to keep loop running til hits target
				
			
			}
			
		
			
		
			}
		}
	
		
		
	
	}


