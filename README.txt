I. AUTHOR
---------------
09140794 Saloni

II. FILES 
---------------
* src = Source folder
	__init__.py 			method to initialize Python packages
	seater.py				file implementig the algorithm for counting seats
*data folder
	input_assign3.txt		input text file for testing the algorithm
*  tests folder
	test.py					test file for testing the correctness of your algorithm
main.py 					main method calling the class seater
README.txt					document explaining the scope of the project

III. PROJECT
---------------
The project aims to create an algorithm that is capable to take into account the number of people sitting in
a room with a maximal capacity of 1 million seats. The algorithm succeeds to do it by creating a double array, 
which represent a 2D grid composed by 1000 rows and 1000 columns.
This creates a system of coordinate, where each corner of the whole seats are: 
                      (0, 0), (0, 999), (999, 999) and (999, 0).
Attendees are supposed to sit only in defined square area with specific coordinates.

The algorithm is set for assigning to each value or seat of the array: the value False (= empty).
The algorithm is designed to carry out 4 different functions that help it to count how many people are sat in the room. 
These functions are:
	1) occupy, which takes the coordinates of the square being occupied and set each value or seat contained in that
		square as True (=occupied)
	2) empty,to which are assigned the coordinates of the square of seats to be emptied. Therefore, the values 
		contained in that square are turned as False (= empty)
	3) toggle, which takes the coordinate of a particular area and if the seats are:
			- empty, it will turn them occupied by using the occupy function;
			- occupy, it will turn them empty by using the empty function.
	4) number_occupied, which count all the seats in the array that are True (= occupied) 
		
IV. RESULT
----------------
The number of nice string: 400410

V. TEST
----------------
Initially it is tested if the pattern matching is parsing the line correctly --> RESULT: OK!
Then the number_occupy function is tested and it works correctly. The number_occupy function is used to test if the
function empty, occupy, and toogle works fine. All these test run successfully!  


