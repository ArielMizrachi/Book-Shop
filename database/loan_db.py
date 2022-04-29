from sqlalchemy import  Column  ,Integer, create_engine ,select ,ForeignKey
from sqlalchemy.orm import declarative_base  ,Session
from datetime import date , timedelta ,datetime
from database import Base ,engine

# table loan (note:delete the loan if the book or id is deleted)
class LOAN(Base):
    __tablename__ = "loan_table"
    loan_id = Column(Integer, primary_key=True)
    book_id = Column(ForeignKey('book_table.id'))
    customer_id = Column(ForeignKey('customer_table.id'))
    loan_date = Column(Integer)
    return_date = Column(Integer)


    def __repr__(self):
        return f"loan(loan_id={self.loan_id!r} ,book_id={self.book_id!r}, customer_id={self.customer_id!r}, loan_date={self.loan_date!r}, return_date={self.return_date!r})"

    # add loan
    @staticmethod
    def add_loan(book_id ,customer_id ,type):
        with Session(engine) as session:

            # preparing the date and type for addition to the data base
            if type == 1: days=10
            if type == 2: days=5
            if type == 3: days=2
            data_string = date.today() + timedelta(days=days)

            loan = LOAN(
                        # id 
                        book_id = book_id,
                        customer_id = customer_id,
                        loan_date = date.today().strftime('%d-%m-%Y'),
                        return_date = data_string.strftime('%d-%m-%Y')
                        )  

            session.add_all([loan])
            session.commit()


    # adding the first loan to the data base
    @staticmethod
    def the_first():
        with Session(engine) as session:

           if session.query(LOAN).count() == 0:
               loan = LOAN(
                        # id 
                        book_id = 1,
                        customer_id = 1,
                        loan_date = '20-05-1997',
                        return_date = '30-05-1997'
                        )  
               session.add_all([loan])
               session.commit()   
                    

    # print  all (return a list)
    @staticmethod
    def print_all():
        with Session(engine) as session:

            # opening a list for trasner
            loan_list = []
            stmt = select(LOAN)

            for loan in session.scalars(stmt):
                loan_list.append({'loan_id':loan.loan_id ,'book_id':loan.book_id ,'customer_id' :loan.customer_id ,'loan_date':loan.loan_date ,'return_date':loan.return_date})
                print(str(loan))
            return loan_list

    # delete a loan
    @staticmethod
    def delete_loan(id):
        with Session(engine) as session:

            del_target = select(LOAN).where(LOAN.loan_id.in_([id]))
            for loan in session.scalars(del_target):
                     session.delete(loan)

            session.commit()

    # checking if there are overdue books
    @staticmethod
    def overdue():
        with Session(engine) as session:

            # opening a list for trasner
            overdue_list = []
            stmt = select(LOAN)
            today_chk= date.today().strftime('%d-%m-%Y')
            today_chk = datetime.strptime(today_chk, '%d-%m-%Y')

            for loan in session.scalars(stmt):

                day_of_return = datetime.strptime(loan.return_date, '%d-%m-%Y')

                if day_of_return < today_chk:
                    overdue_list.append({'loan_id':loan.loan_id ,'book_id':loan.book_id ,'customer_id' :loan.customer_id ,'loan_date':loan.loan_date ,'return_date':loan.return_date})
                    print(str(loan))

            return overdue_list

  

