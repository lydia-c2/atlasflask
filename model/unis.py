""" database dependencies to support sqliteDB examples """
from random import randrange
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


# Define the School class to manage actions in the 'university' table
class University(db.Model):
    __tablename__ = 'university' 

    # Define the School schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _school = db.Column(db.String(255), unique=False, nullable=False)
    _rate = db.Column(db.Text, unique=True, nullable=False)
    _stufac = db.Column(db.Text, unique=True, nullable=False)
    _majors = db.Column(db.Text, unique=True, nullable=False)
    # constructor of a School object, initializes the instance variables within object (self)
    def __init__(self, school, rate, stufac, majors):
        self._school = school    # variables with self prefix become part of the object, 
        self._rate = rate
        self._stufac = stufac
        self._majors

    # a name getter method, extracts name from object
    @property
    def school(self):
        return self._school
    
    # a setter function, allows name to be updated after initial object creation
    @school.setter
    def school(self, school):
        self._school = school
    
    def is_school(self, school):
        return self._school == school
    
    @property
    def rate(self):
        return self._rate
    
    @rate.setter
    def rate(self, rate):
        self._rate = rate

    @property
    def stufac(self):
        return self._stufac
    
    @stufac.setter
    def stufac(self, stufac):
        self._stufac = stufac

    @property
    def majors(self):
        return self._majors
    
    @majors.setter
    def majors(self, majors):
        self._majors = majors
        
    
    @property
    def __str__(self):
        return json.dumps(self.read())

    def create(self):
        try:
            # creates a person object from University(db.Model) class, passes initializers
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
            "rate": self.rate,
            "stufac": self.stufac,
            "majors": self.majors,
        }

    # CRUD update: updates review name, password, phone
    # returns self
    def update(self, school="", rate=""):
        """only updates values with length"""
        if len(rate) > 0:
            self.rate = rate
        if len(rate) > 0:
            self.rate = rate
        if len(school) > 0:
            self.school = school
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

def initUniversity():
    with app.app_context():
        """Create database and tables"""
        # db.init_app(app)
        db.create_all()
        """Tester data for table"""
        u1 = University(school='UCSD', rate='34%', stufac='19:1', majors='Biology, Cognitive Science, International studies')
        u2 = University(school='UCSC',rate='52%', stufac='18:1', majors='Computer Science, Psychology, Cell/Cellular and Molecular Biology')
        u3 = University(school='UCLA', rate='12%', stufac='17:1', majors='Sociology, Political Science and Government, and Econometrics and Quantitative Economics')
        u4 = University(school='UC Davis', rate='46%', stufac='20:1', majors='Research and Experimental Psychology, Management Sciences and Information Systems, Neuroscience and Neurobiology')
        u5 = University(school='UC Berkeley', rate='14.4%', stufac='18:1', majors='Cell/Cellular and Molecular Biology, Computer Science, and Econometrics and Quantitative Economics.')
        u6 = University(school='UC Riverside', rate='69%', stufac='22:1', majors='Business Administration and Management, Psychology, Biology/Biological Sciences')
        u7 = University(school='UC Merced', rate='89%', stufac='20:1', majors='Biology/Biological Sciences, Psychology, Business Administration and Management')
        u8 = University(school='UCSB', rate='26%', stufac='18:1', majors='Social Sciences, Biological and Biomedical Sciences, Mathematics and Statistics')
        u9 = University(school='UC Irvine', rate='41%', stufac='18:1', majors='Health-Related Knowledge and Skills, Psychology, Business, Management, Marketing, and Related Support Services')

        schools = [u1, u2, u3, u4, u5, u6, u7, u8, u9]

        """Builds sample school/note(s) data"""
        for school in schools:
            try:
                '''add a few 1 to 4 notes per school'''
                for num in range(randrange(1, 8)):
                    note = "#### " + school.school + " note " + str(num) + ". \n Generated by test data."
                '''add school/post data to table'''
                school.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {school.school}")