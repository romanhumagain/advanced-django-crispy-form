from django import forms
from App.models import Candidate
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator

# EVERY LETTERS TO LOWER CASE
class Lowercase(forms.CharField):
  def to_python(self, value):
    return value.lower()
  
# EVERY LETTERS TO UPPER CASE
class Uppercase(forms.CharField):
  def to_python(self, value):
    return value.upper()
  

class CandidateForm(forms.ModelForm):
  
  # VALIDATIONS
  alpha_validator =  RegexValidator(
    regex = r'^[a-zA-Z]+$', 
    message='Only alphabetic characters are allowed.')
  
  email_validator = RegexValidator(
    regex=r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',
    message="Enter a valid email address."
  )
  age_validator = RegexValidator(
    regex=r'^[0-9]+$',
    message="Only numbers are allowed."
  )
  phone_validator = RegexValidator(
    regex=r'^[0-9]+$',
    message="Only numbers are allowed."
  )
  
  # FIELDS
  firstname = forms.CharField(
    label="First Name", min_length=3 , max_length=50,
    validators=[alpha_validator],
    widget=forms.TextInput(attrs={'placeholder':"First Name",
                                  'style':'text-transform:capitalize'})
    
  )
  
  lastname = forms.CharField(
    label="Last Name", min_length=3 , max_length=50,
    validators=[alpha_validator],
    widget=forms.TextInput(attrs={'placeholder':"Last Name",
                                  'style':'text-transform:capitalize'})
  )
  
  job = Uppercase(
    label="Job Code",
    min_length=5,
    max_length=5, 
    widget= forms.TextInput(attrs={'placeholder':'Example: FR-22',
                                   'style':'text-transform:uppercase'})
  )
  
  email = Lowercase(
    label='Email Address' , min_length=6,
    validators=[email_validator],
    widget=forms.TextInput(attrs={'placeholder':'Email',
                                  'style':'text-transform:lowercase'})
  )
  phone = forms.CharField(
    required=True,
    validators=[phone_validator],
    widget=forms.TextInput(
      attrs={'placeholder':"Phone number "}
    )
  )
  
  age = forms.IntegerField(
    required=True, 
    validators=[MinValueValidator(1), MaxValueValidator(150)],
    widget=forms.NumberInput(attrs={'placeholder':'Age', 'min': '1', 'max': '150'})
)

  
  experience = forms.BooleanField(
    label='I have a experience',
    required=False
  )
  
  message = forms.CharField(
    required=False,
    label="About You", min_length=10 , max_length=1000,
    widget=forms.Textarea(attrs={'placeholder':"Write about you.", 'rows':9})
  )
  
  
  file = forms.FileField(
    label="Resume",
    widget = forms.ClearableFileInput(
      attrs={
        'style':'font-size:16px'
      }
    )
  )
  photo = forms.ImageField(
    label= "Photo",
    widget = forms.ClearableFileInput(
      attrs={
        'style':'font-size:16px'
      }
    )
  )
  
  
  class Meta:
    model = Candidate
    exclude = ['created_at' , 'status']
    
    SALARY = (
      ('','Salary Expectation (Month)'),
      ('Between ($3000 and $4000)','Between ($3000 and $4000)'),
      ('Between ($4000 and $5000)','Between ($4000 and $5000)'),
      ('Between ($5000 and $6000)','Between ($5000 and $6000)'),
      ('Between ($6000 and $7000)','Between ($6000 and $7000)'),
      ('Between ($7000 and $8000)','Between ($7000 and $8000)'),
    )
    
    GENDER = [
      ('M', 'Male'),
      ('F' , 'Female')
    ]
    
    widgets = {
      'salary':forms.Select(
        choices=SALARY,
        attrs={
          'class':'form-control',
        }
      ),
      
      'gender':forms.RadioSelect(
        choices=GENDER,
        attrs={
          'class':'btn-check'
        }
      ),  
    }
    
  def clean_email(self):
    email = self.cleaned_data.get('email')
    print("clean_email method is called!")  # Print statement for debugging
    if Candidate.objects.filter(email=email).exists():
        raise forms.ValidationError(f"Denied! {email} is already registered.")
    return email
  
  def clean_age(self):
    age = self.cleaned_data.get('age')
    if age < 18 or age > 60:
        raise forms.ValidationError("Please ensure your age is between 18 and 60 to proceed.")
    return age
  
  def clean_job(self):
    job = self.cleaned_data.get('job')
    if job == "FR-22" or job == "BE-36" or job == "FU-69":
      return job
    else:
      raise forms.ValidationError("Please ensure valid job code to proceed.")
    
  # ====== To Concatenate the F-name and L-name ======== #
  def name(obj):
    return "%s %s" % (obj.firstname, obj.lastname)


        
    