<!-- LIBRARY OF ALEXANDRIA -->


<!-- HOW TO RUN THE PROJECT -->

when you first load the project there will be a few things to install, namly SQLalchemy and flask.
simply copy the next few lines to the terminal to install them.

pip install flask
pip install sqlalchemy 

after that the project should run smoothly just run main.py

<!-- PROJECT PURPOSE AND STRUCTURE -->

this project purpose is to manage a library using a database, namely sqlite using sqlalchemy (in the ORM method).
it has the fuctions of:
 adding a book, customer and a loan 
 viewing all customers' books and loans in the database
 removing or returning them
 seeing a specific book or customer
 seeing all overdue loans

it has three tables with a class each, namely book customer and loan. They are structured as follow:

book_table       id
                 name
                 auther
                 published year
                 type

customer_table   id
                 name
                 city
                 age

loan_table       loan_id
                 book_id
                 customer_id
                 loan_date
                 return_date

the three classes are BOOK CUSTOMER and LOAN respectively.

all of the classes are stored in database folder and are connected to library.db

there are three folders in templates, namely book_folder customer_folder and loan_folder that have the various html pages that the flask uses, they are connected to three other files namely book_bluprint, customer_bluprint and loan_bluprint, and all of them are connected via blueprint to the main.py.

the project will start with one customer, book and loan already in the database (using the function the_first in each db) 
the purpose of it being that the project uses date and datetime functions to get it's parematers for loan , and because of that there will be no overdue loans to show.    

there is an additional python file named checker, it's purpose is to verify the various functions of the db and it can be used as a unit test if needed.



<!-- ABOUT THIS PROJECT -->

this assignment was the first serious project that I have worked on and it took me over 50 hours to make it happen.
it was quite a ride and a lot of blood, effort and tears went into the making of it and the learning of the various moudles it uses.
it's not perfect by any means, and there are a lot of rough edges but i'm pretty proud of what came out in the end.
so enjoy viewing it as well.

project by: Ariel Mizrachi
date of completion: 26-04-22