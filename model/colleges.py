""" database dependencies to support sqliteDB examples """
from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash



## INPUTTED WORKOUT CLASS


class Colleges(db.Model):
    __tablename__ = 'Colleges'

    # Define the workout schema
    id = db.Column(db.Integer, primary_key=True)
    _uid = db.Column(db.String(255), unique=True, nullable=False)
    _college = db.Column(db.Text, unique=False, nullable=False)
    _cityName = db.Column(db.Text, unique=False, nullable=False)
    _rate = db.Column(db.String, unique=False, nullable=False)
    _area = db.Column(db.String, unique=False, nullable=False)
    _stufac = db.Column(db.String, unique=False, nullable=False)
    _majors = db.Column(db.Text, unique=False, nullable=False)

    

    # Constructor of a Inputworkout object, initializes of instance variables within object
    def __init__(self, id, uid, college, cityName, rate, area, stufac, majors):
        self.userID = id
        self._uid = uid
        self.college = college
        self.cityName = cityName
        self.rate = rate
        self.area = area
        self.stufac = stufac
        self.majors = majors


    @property
    def uid(self):
        return self._uid
    
    
    @uid.setter
    def uid(self, uid):
        self._uid = uid
        
    def is_uid(self, uid):
        return self._uid == uid


    @property
    def college(self):
        return self._college
    
    # a setter function, allows exercise name to be updated after initial object creation
    @college.setter
    def college(self, college):
        self._exerciseType = college


    @property
    def cityName(self):
        return self._cityName
    
    @cityName.setter
    def sets(self, cityName):
        self._cityName = cityName


    @property
    def rate(self):
        return self._rate
    
    
    @rate.setter
    def reps(self, rate):
        self._rate = rate

    @property
    def area(self):
        return self._area
    
    
    @area.setter
    def reps(self, area):
        self._area = area

    @property
    def stufac(self):
        return self._stufac
    
    
    @stufac.setter
    def reps(self, stufac):
        self._stufac = stufac

    @property
    def majors(self):
        return self._majors
    
    
    @majors.setter
    def reps(self, majors):
        self._majors = majors

    
    # CRUD create, adds a new record to the Collegesp table
    def create(self):
        try:
            # creates a workout object from College(db.Model) 
            db.session.add(self)  
            db.session.commit()  
            return self
        except IntegrityError:
            db.session.remove()
            return None

  
    def read(self):
        
        return {
            "id": self.id,
            "uid": self.uid,
            "college": self.college,
            "city": self.cityName,
            "rate": self.rate,
            "area": self.area,
            "stufac": self.stufac,
            "majors": self.majors
        }
    
    def update(self,rate=""):
        """only updates values with length"""
        if len(rate) > 0:
            self.rate = rate
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
    

def initColleges():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table"""
        i1 = Colleges(college='USCD', id='ucsd', uid='ucsd1', city='San Diego', rate='34%', area='urban', stufac='19:1', majors='Biology, Cognitive Science, International studies')
        i2 = Colleges(college='UCSC', id='ucsc', uid='ucsc1', city='Santa Cruz', rate='52%', area='suburban', stufac='18:1', majors='Computer Science, Psychology, Cell/Cellular and Molecular Biology')
        i3 = Colleges(college='UCLA', id='ucla', uid='ucla1', city='Los Angeles', rate='12%', area='urban', stufac='17:1', majors='Sociology, Political Science and Government, and Econometrics and Quantitative Economics')
        i4 = Colleges(college='UC Davis', id='ucdavis', uid='ucdavis1', city='LA', rate='46%', area='suburban', stufac='20:1', majors='Research and Experimental Psychology, Management Sciences and Information Systems, Neuroscience and Neurobiology')
        i5 = Colleges(college='UC Berkeley', id='ucb', uid='ucb1', city='Berkeley', rate='14.4%', area='', stufac='18:1', majors='Cell/Cellular and Molecular Biology, Computer Science, and Econometrics and Quantitative Economics.')
        i6 = Colleges(college='UC Riverside', id='ucr', uid='ucr1', city='Riverside', rate='69%', area='', stufac='22:1', majors='Business Administration and Management, Psychology, Biology/Biological Sciences')
        i7 = Colleges(college='UC Merced', id='ucm', uid='ucm1', city='Merced', rate='89%', area='', stufac='20:1', majors='Biology/Biological Sciences, Psychology, Business Administration and Management')
        i8 = Colleges(college='UCSB', id='ucsb', uid='ucsb1', city='Santa Barbara', rate='26%', area='college town', stufac='18:1', majors='Social Sciences, Biological and Biomedical Sciences, Mathematics and Statistics')
        i9 = Colleges(college='UC Irvine', id='uci', uid='uci1', city='Irvine', rate='41%', area='', stufac='18:1', majors='Health-Related Knowledge and Skills, Psychology, Business, Management, Marketing, and Related Support Services')
        
        colleges = [i1, i2, i3, i4, i5, i6, i7, i8, i9]

       # """Builds sample college/note(s) data"""
        for college in colleges:
            try:
                '''add a few 1 to 4 notes per user'''
                for num in range(randrange(1, 9)):
                #  note = "#### " + user.college + " note " + str(num) + ". \n Generated by test data."
                    '''add inputted workout data to table'''
                college.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"ERROR {Colleges.id}")
