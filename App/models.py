from email.policy import default
from secrets import choice
from django.db import models

# 1) PREVENT DUPLICATED EMAILS
class Registered_email(models.Model):
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.email

# 2) SUPPORT
class Support(models.Model):

    PERSON = {
        ('Employee', 'Employee'),
        ('Candidate', 'Candidate'),
    }

    OPTION = {
        ('I lost my account', 'I lost my account'),
        ('My password does not work', 'My password does not work'),
        ('Update resume', 'Update resume'),
        ('Others', 'Others'),
    }

    SITUATION = {
        ('Done', 'Done'),
        ('Pending', 'Pending'),
    }

    terms = models.BooleanField("took responsability", default=False)
    message = models.TextField()
    person = models.CharField(max_length=50, choices=PERSON)
    option = models.CharField(max_length=50, choices=OPTION)
    email = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending')

    def __str__(self):
        return self.person


# 3) MESSAGE
class Message(models.Model):
    SITUATION = {
        ('Done', 'Done'),
        ('Pending', 'Pending'),
    }

    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending')