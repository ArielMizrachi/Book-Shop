from sqlalchemy import  Column ,String  ,Integer, select 
from sqlalchemy.orm import Session ,relationship
from database import Base ,engine


# table customer
class CUSTOMER(Base):
    __tablename__ = "customer_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    city = Column(String)
    age = Column(Integer)
    customer_loan = relationship('LOAN',cascade='all,delete')
    


    def __repr__(self):
        return f"customer(id={self.id!r}, name={self.name!r}, city={self.city!r}, age={self.age!r})"

    # add book
    @staticmethod
    def add_customer(name ,city ,age ):
        with Session(engine) as session:

            customer = CUSTOMER(
                        # id 
                        name = name,
                        city = city,
                        age = age,
                      
                          )  

            session.add_all([customer])
            session.commit()

    # adding the first customer to the data base
    @staticmethod
    def the_first():
        with Session(engine) as session:

           if session.query(CUSTOMER).count() == 0:
               customer = CUSTOMER(
                        # id 
                        name = 'joe',
                        city = 'washington',
                        age = 18,
                        )  
               session.add_all([customer])
               session.commit()  

    # print specific or all (return a list)
    @staticmethod
    def print_all( query=''):
        with Session(engine) as session:

            # opening a list for trasner
            customer_list = []
            if query != '':
                stmt = select(CUSTOMER).where(CUSTOMER.name.in_([query]))
            else:    
                stmt = select(CUSTOMER)

            for customer in session.scalars(stmt):
                customer_list.append({'id':customer.id ,'name' :customer.name ,'city':customer.city ,'age':customer.age})
                print(str(customer))
            return customer_list

    # delete a customer
    @staticmethod
    def delete_customer(id):
        with Session(engine) as session:

            del_target = select(CUSTOMER).where(CUSTOMER.id.in_([id]))
            for customer in session.scalars(del_target):
                     session.delete(customer)

            session.commit()

   
