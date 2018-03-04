import urllib.request
import json
import urllib.parse

class User(object):

    def __init__(self, uname, pwd, name, bday, weight, height, gender, bfat, bio, email):
        self.uname = uname
        self.pwd = pwd
        self.name = name
        self.bday = bday
        self.weight = weight
        self.height = height
        self.gender = gender
        self.bfat = bfat
        self.bio = bio
        self.email = email

    def create_Account(self, uname, pwd):
        
