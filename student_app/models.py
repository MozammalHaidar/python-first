from django.db import models

# Create your models here.
class Hobby(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Result(models.Model):
    marks = models.FloatField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject.name

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
    hobby = models.OneToOneField(Hobby,on_delete=models.CASCADE,null=True)
    subject = models.ManyToManyField(Subject)
    result = models.ManyToManyField(Result)

    def __str__(self):
        return f'{self.name}"s profile'



