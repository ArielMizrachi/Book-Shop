from flask import  Blueprint, render_template ,request
import database
from database.book_db import  BOOK

book = Blueprint('book',__name__,url_prefix='/book')

book_narker =BOOK()
book_narker.the_first()

# main page of book 
@book.route('/book_main')
def book_main(): 
     return render_template ('book_folder/book_main.html')


# add a book
@book.route('/book_add', methods=['GET', 'POST'])
def book_add():

     # sending request to the user 
     if request.method == 'POST':
          book = request.form['name']
          author = request.form['author']
          published_year= request.form['published_year']
          type= request.form['type']

          # adding the book
          book_narker.add_book(book,author,published_year,type)

          # getting all the books for display
          book_list=book_narker.print_all()
          msg = f'we added the book {book}'
          return render_template ('book_folder/book_search_and_delete.html', book_list =book_list,msg = msg)
     
     return render_template('book_folder/book_add.html')



@book.route('/book_search_and_delete')
def book_search_and_delete(): 
     book_list=book_narker.print_all() 
     return render_template ('book_folder/book_search_and_delete.html' , book_list =book_list,msg = '')



@book.route('/view_specific_book', methods=['GET', 'POST'])
def view_specific_book(): 

     if request.method == 'POST':
          book = request.form['name']
          book_list=book_narker.print_all(book)
          if len(book_list) == 0:
               msg = f'we could not find anything sorry'
               return render_template ('book_folder/book_search_and_delete.html', book_list =book_list,msg = msg)

          msg = f'this is what we found'
          return render_template ('book_folder/book_search_and_delete.html', book_list =book_list,msg = msg)

     return render_template ('book_folder/view_specific_book.html')  


@book.route('/book_del')
def book_delete(): 

     # get the id and book name in get method and delete
     id=request.args.get('id')
     name=request.args.get('name')
     book_narker.delete_book(id)

     # show the new list
     msg = f'we deleted the book {name} (id {id})'
     book_list=book_narker.print_all() 
     return render_template ('book_folder/book_search_and_delete.html' , book_list =book_list,msg = msg)