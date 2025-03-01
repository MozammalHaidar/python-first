from django.db import models

# Create your models here.

class Student(models.Model):

    GENDER = [
    ("Male","Male"),
    ("Female","Female"),
    ("Others","Others"),      
    ]

    RELIGION = [
    ("Islam","Islam"),
    ("Hindu","Hindu"),
    ("Christian","Christian"),
    ("Buddha","Buddha"),
    ("Atheist","Atheist"),
    ]

    prime_id = models.AutoField(primary_key=True,unique=True,editable=False,blank=False,null=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    image = models.ImageField(upload_to='images/',default = "def.png",blank=True)
    age = models.PositiveIntegerField()
    roll = models.IntegerField()
    religion = models.CharField(choices=RELIGION,max_length=50)
    gender = models.CharField(choices=GENDER,max_length=50)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=50)
    is_Bangladeshi = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)

    def _str_(self):
        return f'{self.name}"s profile'



