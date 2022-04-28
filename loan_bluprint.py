from flask import  Blueprint, render_template ,request
import database
from database.customer_db import CUSTOMER
from database.loan_db import  LOAN

loan = Blueprint('loan',__name__,url_prefix='/loan')

customer_marker=CUSTOMER()
loan_marker =LOAN()
loan_marker.the_first()

# main page of loan 
@loan.route('/loan_main')
def loan_main(): 
     return render_template ('loan_folder/loan_main.html')


# add_loan(self ,book_id ,customer_id ,type):
# add a loan
@loan.route('/loan_choose_book')
def loan_choose_book():

     # making a list of avilable books
     book_list = loan_marker.available_books()
     if len(book_list) == 0:
          msg = 'no avilable books sorry'
          return render_template ('loan_folder/loan_choose_book.html' , book_list =book_list,msg =msg)

     return render_template ('loan_folder/loan_choose_book.html' , book_list =book_list,msg ='')
    

@loan.route('/loan_choose_customer')
def loan_choose_customer(): 

     # get the id and type
     id=request.args.get('id')
     type = request.args.get('type')

     # make a new customer list
     customer_list=customer_marker.print_all()
     if len(customer_list) == 0:
          msg = 'no avilable  customers'
          return render_template ('loan_folder/loan_choose_customer.html' , customer_list =customer_list,id=id,type=type,msg=msg)

     return render_template ('loan_folder/loan_choose_customer.html' , customer_list =customer_list,id=id,type=type,msg='')

@loan.route('/loan_add')
def add_loan(): 
          #adding a loan  
         book_id=request.args.get('book_id')
         type=request.args.get('type')
         customer_id=request.args.get('customer_id')
         loan_marker.add_loan(book_id,customer_id,int(type))

         #make a list for printing
         loan_list=loan_marker.print_all() 
         return render_template ('loan_folder/loan_search_and_return.html' , loan_list =loan_list,msg = '')


@loan.route('/loan_search_and_return')
def loan_search_and_return(): 
     loan_list=loan_marker.print_all() 
     if len(loan_list) == 0:
          msg='no one is loaning right now'
          return render_template ('loan_folder/loan_search_and_return.html' , loan_list =loan_list,msg = msg)

     return render_template ('loan_folder/loan_search_and_return.html' , loan_list =loan_list,msg = '')



@loan.route('/loan_return')
def loan_return(): 

     # get the id and loan name in get method and return
     id=request.args.get('id')
     loan_marker.delete_loan(id)

     # show the new list
     msg = f'we returnd the loan number {id}'
     loan_list=loan_marker.print_all() 
     return render_template ('loan_folder/loan_search_and_return.html' , loan_list =loan_list,msg = msg)




@loan.route('/view_late_loans')
def loan_late(): 
     loan_list=loan_marker.overdue()
     if len(loan_list) == 0:
          msg='everything is here'
          return render_template ('loan_folder/view_late_loans.html' , loan_list =loan_list,msg = msg)

     return render_template ('loan_folder/view_late_loans.html' , loan_list =loan_list,msg = '')