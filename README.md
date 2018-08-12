# Lab 03 (Due Week 03, Sunday, 11:59 pm) (12 marks)

# Aim

1.  Understand the importance of requirements engineering and create requirements specifications based on UML use-cases.

# Lab instructions

This lab must be completed during your lab session and for this lab, you are expected to work in **groups of two**. For the odd-numbered classes, one group of three may be permitted.

## Task 1: Requirements Analysis (10 marks)

AffordableRentals is a company specialising in car rentals to customers. The company would like to develop a web-based car rental system to enable customers to rent cars online prior to their scheduled pick-up date and time. This software development project has been contracted to a software consultancy firm who has completed the requirements gathering and developed the following high-level problem statement. For the purposes of this lab, the scope of the system is limited to the following functionality.

1.  A car rental is a vehicle that can be used temporarily for a fee during a specified period.
    
2.  The cars that can be rented from AffordableRentals are grouped into small, medium, large and premium cars.
    
3.  A customer should be able to specify search criteria and view available cars that match the search criteria. The search criteria should include age, preferred pick-up and drop-off locations.
    
4.  The search result should include details of the car type and price for each day of car rental.
    
5.  From the displayed search results, the customer can select a car and proceed with booking the car.
    
6.  During the booking process, the customer is required to specify additional details such as:
    

	-   name of the customer and age;
    
	-   licence number;
    
	-   the rental period in number of days;
    
	-   option to purchase an insurance cover; and
    
	-   email-address.
    

7.  Insurance is provided by an external company, QBEI Insurances.
    
8.  Once the booking details have been provided by the customer, a net price is computed and displayed to the customer.
    
9.  The customer proceeds with the booking by providing credit card details for payment. The company uses an external credit card system to handle payments.
    
10.  Once the payment has been confirmed, an email is sent to the customer confirming the booking.
    
11.  The online system must permit staff of AffordableRentals to log in to the system with a username and password.
    
12.  Admin staff, once logged in, will be able to enter new car information into the system.
    
13.  For each car, the system will hold the following pieces of information: vehicle-type (small, medium, large, premium), make, model, year and registration.
    
14.  Managers, once logged in, will be able to generate weekly reports that show a log of cars rented during the week.
    

**Your task is to:**

1.  Identify the system actors and goals.  **(1 mark)**
    
2.  Draw a use-case diagram to model the behaviour of the online rental system. The model should include the actors, the use cases, the relation between the use cases and the actors and the relation between the use cases. _(Refer to the lecture slide 'Use Case Diagram: Device Control' to help you with this task.)_  **(5 marks)** 

3.  Define a detailed use-case specification for the main use-case of a customer renting a car.  **(4 marks)**

	Use the template provided in the lecture to define this specification. It must include:

	-   _Use-case name_;
	    
	-   _Brief description_;
	    
	-   _Initiating Actor_;
	    
	-   _Actor’s goal_;
	    
	-   _Participating actors_;
	    
	-   _Flow of events **only** for the Main Success usage scenario_.
   
  ****For the purposes of this lab, you don’t need to define the pre-condition, post-condition and the alternate usage scenarios.****

  *(Refer to the lecture slide "Use Case 1: Unlock" to help you with this task.)*

To obtain marks for the above task, you must draw the use-case diagram using an appropriate modelling tool such as [draw.io](http://draw.io/), but it is not necessary. The use-case specification can be typed up.
**All artefacts must be uploaded to GitHub by the due-date.**

## Bonus Task: Python Exercises (2 marks)

This lab uses the `pytest` package and some plugins to test the programming exercises.

You will need to install these packages in order to run the tests. To do this, you will use a  *virtual environment* which is essentially a nice way to use Python libraries by project. Please read  [Virtual Environments in Python](https://webcms3.cse.unsw.edu.au/COMP1531/18s2/resources/19969) for more information.

The below commands will set up your  _virtual environment_:

```bash
virtualenv --python=python3 venv # Create the venv folder in the current directory.
. venv/bin/activate # Activate the virtual environment.
pip3 install -r requirements.txt # Install dependencies in the virtual environment.
```

The process to import the starter code for the bonus task is the same as last week. Go to  [GitHub](https://cgi.cse.unsw.edu.au/~cs1531/github/run.cgi/login), select  **lab03**  and click  **Import**.

**Extended numberGuesser (2 Marks)**

Write a simple command line guessing game. A list of random numbers is generated for you. You need to write your program in a file called `numberGuesser.py`.

The user will guess a number, and if the number *is* in the list, that number is removed. Otherwise, the program will reveal whether the closest number in the list is higher or lower than their guess. The game ends when the user quits early (by pressing `q`) or the user has guessed all the numbers in the list.

If the user has guessed all the numbers in the list, the program should print out `Congratulations! You won!`. The message `Thanks for playing! See you soon.` is printed at the end of the game.

Your program should work like this:
```
Numbers are between 0 and 10 inclusive.
There are 3 values left. Guess: 5
You found 5! It was in the list.
There are 2 values left. Guess: 4
The closest to 4 is lower.
There are 2 values left. Guess: 3
The closest to 3 is lower.
There are 2 values left. Guess: 2
You found 2! It was in the list.
There are 1 values left. Guess: 6
The closest to 6 is higher.
There are 1 values left. Guess: 7
You found 7! It was in the list.
Congratulations! You won!
Thanks for playing! See you soon.
```

You will need to complete the `run_game`, `handle_guess` and `find_closest` functions.

- `run_game` should keep asking for guesses from the user until the game is over, and handle guesses appropriately.
- `handle_guess` should return a new list with the guessed number removed if it is in the list.
- `find_closest` should return the closest number in the list to the guess.

The output of your program should work as shown in the example above.


## Testing

Similar to the last lab, you will use the `pytest` package to test your program. You can run the tests by simply running

```bash
python3 -m pytest
```

Results for saer:
python extension is passing all tests except for test_cheater.






