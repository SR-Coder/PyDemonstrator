from django.db import models
from datetime import datetime, timedelta
import re

# Create Validators here
# create Managers here
# *****************************************************
# *** This is a basic validatior that will work for ***
# *** any registration form.  *************************
# *****************************************************
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        # First name errors
        if len(postData['fName'])<2:
            errors['fName']="First name must be greater than two characters"
        # Last name errors
        if len(postData['lName'])<2:
            errors['lName']="Last name must be greater than two characters"
        # Email regex that ensures a valid email is inserted
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['eMailr']):    # test whether a field matches the pattern            
            errors['eMailr'] = "Invalid email address!"
        # checks to make sure that the email is unique
        user = User.objects.filter(email = postData['eMailr'])
        if user:
            errors['eMailr'] = "There is already an account associated with this address"
        
# ****************************************************
# *** This is the birthday validator age must be   ***
# *** set in seconds.... which is a pain. ************
# ****************************************************
        # if postData['bDay'] =="":
        #     errors['bDay']="enter a valid birthday"
        # else:
        #     now = datetime.now()
        #     birthdate = postData['bDay']
        #     birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        #     daysDiff = now - birthdate
        #     type(daysDiff)
        #     delta = daysDiff.total_seconds()
        #     delta = int(delta)
        #     print('*'*100)
        #     print(daysDiff)
        #     print(delta)
        #     print('*'*100)
        #     if delta < 409968000:
        #         errors['bDay']="You must be 13 years old to register"
# ****************************************************

        # checks to see if the password matches the regex
        pw = postData['pWordr']
        if not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', pw):
            errors['pReg']="Password must be letters, numbers, and symbols"
        # check to see if the password matches the check password 
        if postData['pWordr'] != postData['chkPword']:
            errors['chkPword'] = "Passwords do not match!" 
        return errors

    def login_validator(self, postData):
        errors={}
        # Email regex that ensures a valid email is inserted
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['eMail']):    # test whether a field matches the pattern            
            errors['eMail'] = "Invalid email address!"
        if postData['eMail'] == "":
            errors['eMail'] = "Please enter a valid email!"
        if postData['pWord'] == "":
            errors['pWord'] = "Please enter a valid password!"
        return errors




# Create your models here.
class User(models.Model):
    fName = models.CharField(max_length=25)
    lName = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    age = models.DateField()
    accessLevel = models.IntegerField()
    active = models.BooleanField()
    confirmKey = models.CharField(max_length=255) # This will be a key sent by email to compare and set the confirmed flag
    confirmed = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()