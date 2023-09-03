from django.db import models

STATUS = (
  ('Pending' ,'Pending'),
  ('Approved' , 'Approved'),
  ('Disapproved' , 'Disapproved')
)

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
]

# Create your models here.
class Candidate(models.Model):
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  age = models.IntegerField(null=True, blank=True)
  job = models.CharField(max_length=5)
  phone = models.CharField(max_length=20 , null=True, blank=True)
  email = models.EmailField()
  experience = models.BooleanField(null=True)
  gender = models.CharField(max_length=10)
  salary = models.CharField(max_length=100)
  message = models.TextField()
  created_at = models.TimeField(auto_now_add= True)
  status = models.CharField(max_length=50 , choices = STATUS , default= 'Pending')
  
  # Captialize the First name and Last name
  def clean(self):
    super().clean()
    self.firstname = self.firstname.capitalize()
    self.lastname = self.lastname.capitalize()
    
    
  def __str__(self) -> str:
    return f'{self.firstname} {self.lastname}'