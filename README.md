# ACME_schedule
## About
This code was developed as a solution to the recruitment process exercise fos IOET.
It is a program writen in Python 3.x

## Problematic
The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

## Objetive
Output a table containing pairs of employees and how often they have coincided in the office

## Conditions
Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data.

Example:

        RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
        ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

Lenguage:  It’s important to notice that you can use any programming language you want but you can not use any external library to solve the exercise.

## Solution
### Description
The solution is a simple script that reads, structures, and parses the input data. Finally the result is printed to the console.


### Structure
The program have 4 files:
* main.py: runs the program
* functions.py: have all the necessary functions to manage data
* person.py: contains the constructor a methods for the Persons objects.
* test.py: Runs the tests to check the correct functionality of the functions and methods defined in the functions and person files


### Run

#### Requirements
* Python 3.x installed
* Download the program from the GiHub [repository](https://github.com/lucrohatsch/ACME_schedule/archive/refs/heads/master.zip)

#### Instructions
* Open the Consol/CMD/Terminal
* Navegate to the program directory
* Run the main.py file.

        python main.py

Always it's posible to modify the input file whith your own dataset 

### Example

#### INPUT

        RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
        ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
        ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

#### OUTPUT

        Employees pair     -> Days
        RENE - ASTRID      -> 2 
        RENE - ANDRES      -> 2
        ASTRID - ANDRES    -> 3