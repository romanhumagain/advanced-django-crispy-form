from django.db import models
from multiselectfield import MultiSelectField

STATUS = (
  ('Pending' ,'Pending'),
  ('Approved' , 'Approved'),
  ('Disapproved' , 'Disapproved')
)

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
]
FRAMEWORKS = (
    ('django', 'Django'),
    ('flask', 'Flask'),
    ('spring', 'Spring Boot'),
    ('express', 'Express.js'),
    ('rails', 'Ruby on Rails'),
    ('other', 'Other')
)

LANGUAGES = (
    ('python', 'Python'),
    ('java', 'Java'),
    ('javascript', 'JavaScript'),
    ('csharp', 'C#'),
    ('ruby', 'Ruby'),
    ('other', 'Other')
)

DATABASES = (
    ('postgresql', 'PostgreSQL'),
    ('mysql', 'MySQL'),
    ('mongodb', 'MongoDB'),
    ('sqlite', 'SQLite'),
    ('oracle', 'Oracle'),
    ('other', 'Other')
)

LIBRARIES = (
    ('pandas', 'Pandas'),
    ('numpy', 'NumPy'),
    ('react', 'React'),
    ('lodash', 'Lodash'),
    ('matplotlib', 'Matplotlib'),
    ('other', 'Other')
)


# Create your models here.
class Candidate(models.Model):
  firstname = models.CharField(max_length=50)
  lastname = models.CharField(max_length=50)
  age = models.IntegerField(null=True, blank=True)
  job = models.CharField(max_length=5)
  phone = models.CharField(max_length=20 , null=True, blank=True)
  email = models.EmailField()
  file = models.FileField(upload_to='candidate_files')
  photo = models.ImageField(upload_to='candidate_photo')
  experience = models.BooleanField(null=True)
  gender = models.CharField(max_length=10)
  salary = models.CharField(max_length=100)
  message = models.TextField()
  created_at = models.TimeField(auto_now_add= True)
  status = models.CharField(max_length=50 , choices = STATUS , default= 'Pending')
  
  # ======= Not Working Multiselectfield due to some installation problem ========== #
  ''' 
  frameworks = MultiSelectField(choices = FRAMEWORKS )
  languages =  MultiSelectField(choices = LANGUAGES)
  database =   MultiSelectField(choices = DATABASES)
  libraries =  MultiSelectField(choices = LIBRARIES)
  '''
  
  
  # Captialize the First name and Last name
  def clean(self):
    super().clean()
    self.firstname = self.firstname.capitalize()
    self.lastname = self.lastname.capitalize()
    
    
  def __str__(self) -> str:
    return f'{self.firstname} {self.lastname}'