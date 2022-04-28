from flask import  Blueprint, render_template ,request
import database
from database.customer_db import  CUSTOMER

customer = Blueprint('customer',__name__,url_prefix='/customer')

customer_narker =CUSTOMER()
customer_narker.the_first()

# main page of customer 
@customer.route('/customer_main')
def customer_main(): 
     return render_template ('customer_folder/customer_main.html')


# add a customer
@customer.route('/customer_add', methods=['GET', 'POST'])
def customer_add():

     # sending request to the user 
     if request.method == 'POST':
          name = request.form['name']
          city = request.form['city']
          age = request.form['age']

          # adding the customer
          customer_narker.add_customer(name ,city ,age)

          # getting all the customers for display
          customer_list=customer_narker.print_all()
          msg = f'we added the customer {customer}'
          return render_template ('customer_folder/customer_search_and_delete.html', customer_list =customer_list,msg = msg)
     
     return render_template('customer_folder/customer_add.html')



@customer.route('/customer_search_and_delete')
def customer_search_and_delete(): 
     customer_list=customer_narker.print_all() 
     return render_template ('customer_folder/customer_search_and_delete.html' , customer_list =customer_list,msg = '')



@customer.route('/view_specific_customer', methods=['GET', 'POST'])
def view_specific_customer(): 

     if request.method == 'POST':
          customer = request.form['name']
          customer_list=customer_narker.print_all(customer)
          if len(customer_list) == 0:
               msg = f'we could not find anything sorry'
               return render_template ('customer_folder/customer_search_and_delete.html', customer_list =customer_list,msg = msg)

          msg = f'this is what we found'
          return render_template ('customer_folder/customer_search_and_delete.html', customer_list =customer_list,msg = msg)

     return render_template ('customer_folder/view_specific_customer.html')  


@customer.route('/customer_del')
def customer_delete(): 

     # get the id and customer name in get method and delete
     id=request.args.get('id')
     name=request.args.get('name')
     customer_narker.delete_customer(id)

     # show the new list
     msg = f'we deleted the customer {name} (id {id})'
     customer_list=customer_narker.print_all() 
     return render_template ('customer_folder/customer_search_and_delete.html' , customer_list =customer_list,msg = msg)