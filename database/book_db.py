from sqlalchemy import  Column ,String  ,Integer ,select 
from sqlalchemy.orm import Session ,relationship
from database import Base ,engine
from database import LOAN


# table books
class BOOK(Base):
    __tablename__ = "book_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    author = Column(String)
    published_year = Column(Integer)
    type = Column(Integer)
    book_loan = relationship('LOAN',cascade='all,delete')
    
        
    def __repr__(self):
        return f"book(id={self.id!r}, name={self.name!r}, author={self.author!r}, published_year={self.published_year!r}, type={self.type!r})"

    # add book
    @staticmethod
    def add_book(name ,author ,published_year ,type):
        with Session(engine) as session:

            book = BOOK(
                        # id 
                        name = name,
                        author = author,
                        published_year = published_year,
                        type = type,
                    )            
            session.add_all([book])
            session.commit()

     # adding the first book to the data base    
    @staticmethod
    def the_first():
        with Session(engine) as session:

           if session.query(BOOK).count() == 0:
               book = BOOK(
                        # id 
                        name = 'The book that never was',
                        author = 'Aliases',
                        published_year = 2023,
                        type = 1,
                        )  
               session.add_all([book])
               session.commit()  
        

    # print specific or all (return a list)
    @staticmethod
    def print_all(query=''):
        with Session(engine) as session:

            # opening a list for trasner
            book_list = []
            if query != '':
                stmt = select(BOOK).where(BOOK.name.in_([query]))
            else:    
                stmt = select(BOOK)

            for book in session.scalars(stmt):
                book_list.append({'id':book.id ,'name' :book.name ,'auther':book.author ,'published_year':book.published_year ,'type':book.type})
                print(str(book))
            return book_list

    # delete a book
    @staticmethod
    def delete_book(id):
        with Session(engine) as session:

            del_target = select(BOOK).where(BOOK.id.in_([id]))
            for book in session.scalars(del_target):
                     session.delete(book)

            session.commit()


# print all available books (return a list)
    def available_books(self ):
        with Session(engine) as session:

            # opening a list for trasner
            book_list = []
            loans = select(LOAN.book_id)
            chk_books = select(BOOK).where(BOOK.id.not_in(loans))
            

            for book in session.scalars(chk_books):
                book_list.append({'id':book.id ,'name' :book.name ,'auther':book.author ,'published_year':book.published_year ,'type':book.type})
                print(str(book))
            return book_list
 

    



    