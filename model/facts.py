""" database dependencies to support sqliteDB examples """
from random import randrange
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


# Define the Review class to manage actions in the 'reviews' table
class Review(db.Model):
    __tablename__ = 'reviews' 

    # Define the Review schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _school = db.Column(db.String(255), unique=False, nullable=False)
    _fact = db.Column(db.Text, unique=True, nullable=False)

    # constructor of a Review object, initializes the instance variables within object (self)
    def __init__(self, school, review):
        self._school = school    # variables with self prefix become part of the object, 
        self._fact = "fact"

    # a name getter method, extracts name from object
    @property
    def school(self):
        return self._school
    
    # a setter function, allows name to be updated after initial object creation
    @school.setter
    def school(self, school):
        self._school = school
    
    @property
    def fact(self):
        return self._fact
    
    @fact.setter
    def fact(self, fact):
        self.fact = fact
        
    def is_fact(self, fact):
        return self._fact == fact
    
    @property
    def __str__(self):
        return json.dumps(self.read())

    def create(self):
        try:
            # creates a person object from Review(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Reviews table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "school": self.school,
            "fact": self.fact
        }

    # CRUD update: updates review name, password, phone
    # returns self
    def update(self, school="", fact=""):
        """only updates values with length"""
        if len(fact) > 0:
            self.review = fact
        if len(fact) > 0:
            self.review = Review
        if len(school) > 0:
            self.school = school
        if len(school) > 0:
            self.school = school
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

"""Database Creation and Testing """

def initReviews():
    with app.app_context():
        """Create database and tables"""
        # db.init_app(app)
        db.create_all()
        """Tester data for table"""
        u1 = fact(school='UCSD', 'There are 220 thousand Eucalyptus trees on campus' )
        u2 = fact(school='UCB', 'The name for Berkeleys bear is Oski')
        u3 = fact(school'UCLA', 'UCLA launched the internet in 1969 to Stanford')
        u4 = fact(school='UCI', 'There are concerts, festivals, movie screenings, comedy nights, and many other special activities throughout the year.')
        u5 = fact(school='UCSB', 'There are 7 bikeways on campus')
        u6 = fact(school='UCD', 'Aggies is a reference to their agricultural beginnings')
        u7 = fact(school='UCSC', 'The mascot is a banana slug')
        u8 = fact(school='UCR', 'One of the top 50 green colleges in America')
        u9 = fact(school='UCM', 'Their nickname is the Golden Bobcats')

        facts = [u1, u2, u3, u4, u5, u6, u7, u8, u9]

        """Builds sample reviews/note(s) data"""
        for fact in facts:
            try:
                '''add a few 1 to 4 notes per review'''
                for num in range(randrange(1, 4)):
                    note = "#### " + fact.school + " note " + str(num) + ". \n Generated by test data."
                '''add review/post data to table'''
                fact.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {fact.fact}")