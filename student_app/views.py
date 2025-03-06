from django.shortcuts import render
from .models import Student

# Create your views here.
def myFnc(request):
    if request.method == 'POST':
        name = request.POST['name']
        img = request.FILES.get('file')
        email = request.POST['email']
        roll = request.POST['roll']
        age = request.POST['age']
        religion = request.POST['religion']
        gender = request.POST['gender']
        is_Bangladeshi = request.POST['is_Bangladeshi']
        date_of_birth = request.POST['date_of_birth']
        save_in_db = Student(name=name,email=email,image=img,roll=roll,age=age,religion=religion,gender=gender,is_Bangladeshi=is_Bangladeshi,date_of_birth=date_of_birth)
        save_in_db.save()
            
    return render(request,'index.html')

def secFnc(request):
    all_student = Student.objects.all()  
    return render(request,'first.html',locals())


