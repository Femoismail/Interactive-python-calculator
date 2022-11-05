Interactive python calculator

This calculator offers 5 operations and takes 2 inputs per operation selected.

Operation 1 - Addition
Operation 2 - Subtraction
Operation 3 - Division
Operation 4 - Multiplication
Operation 5 – Quit program

In order to run the program, copy code and paste in visual studio code and click run.

The first sequence of the program that will appear after you click run will be the options menu.

Please choose 1 of the 5 options from the menu. 

I have implemented a while loop for 3 sections:

Firstly, the user will be prompted to select one of the five operations [1,2,3,4, Q] 
a)	If the user types an option that is not [1,2,3,4, Q] or is left blank, the options menu will continue to appear until an option is correctly selected.
If the user types the correct option [1,2,3,4], the next sequence of the program will appear. The program will then display the option chosen, and will prompt you to enter your first number (first number can take float type inputs).

Secondly, using a while loop with a try and except function for the first number:
a)	For all incorrect inputs (that is, blanks or non-number type specifications) entered, the user will be prompted to enter a number. 
b)	Once the correct input is added, the program will move to the next sequence, that will prompt the user to enter the second number (second number can take float type inputs).

Thirdly: using a while loop with a try and except function for the second number, the format explained above for the first number will be repeated. 


Once the user has correctly selected the second number, the operation selected will be executed, and the result will be displayed in float format.

The option Menu will then reappear for the user to continue using the calculator program.

If you wish to exit the program, please enter q or Q.


