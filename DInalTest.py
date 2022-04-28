from multiprocessing import AuthenticationError
import database
from sqlalchemy import select ,delete 
from sqlalchemy.orm import Session


def print_all_db():
    # print all db
    with Session(database.engine) as session:
        for author in session.scalars(select(database.BOOK)):
            print(author)

        for book in session.scalars(select(database.CUSTOMER)):
            print(book)

        for book in session.scalars(select(database.LOAN)):
            print(book)


def insert_book(name,author,published_year,type):
    """insert book"""
    with Session(database.engine) as session:
        book = database.BOOK(
                            name=name,
                            author=author,
                            published_year=published_year,
                            type = type
                            
                         )

        session.add_all([book])
        session.commit()

def insert_customer(name,city,age):
    """insert customer"""
    with Session(database.engine) as session:
        customer = database.CUSTOMER(
                            name=name,
                            city=city,
                            age=age,
                            
                         )

        session.add_all([customer])
        session.commit()

def insert_loan(book_id,customer_id,loan_date,return_date):
    """insert loan"""
    with Session(database.engine) as session:
        loan = database.LOAN(
                            book_id=book_id,
                            customer_id=customer_id,
                            loan_date = loan_date,
                            return_date=return_date
                            
                         )

        session.add_all([loan])
        session.commit()

def delete_author(book_id):
    """delete author"""
    with Session(database.engine) as session:
        del_target = select(database.BOOK).where(database.BOOK.id.in_([book_id]))
        for book in session.scalars(del_target):
            session.delete(book)
        session.commit()

if __name__ == '__main__':
    database.Base.metadata.create_all(database.engine)

    # insert_book('harry','potter',1997,2)
    # insert_customer('joe','rishon',12)
    # insert_loan(1,1,'12.01.98','12.02.29')

    # BOOK CHECK ***********************

    # database.BOOK.the_first()
    # database.BOOK.add_book('harry','potter',1997,2)
    # database.BOOK.print_all()
    # database.BOOK.print_all('harry')
    # database.BOOK.delete_book(2)
    # print_all_db() 
    # delete_author(1)

    # BOOK CHECK ***********************

    # CUSTOMOR CHECK ************************
    
    # database.CUSTOMER.the_first()
    # database.CUSTOMER.add_customer('jo','kensas',12)
    # database.CUSTOMER.print_all()
    # database.CUSTOMER.print_all('jo')
    # database.CUSTOMER.delete_customer(2)

     # CUSTOMOR CHECK ************************

    # LOAN CHECK ********************

    # database.LOAN.the_first()
    # database.LOAN.add_loan(8,3,3) 

    # database.LOAN.print_all()

    # database.LOAN.delete_loan(2)

    # database.LOAN.overdue()

     # LOAN CHECK ********************


    database.BOOK.delete_book(1)

    print_all_db() 