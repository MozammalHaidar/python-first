from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Student,Hobby
from django.db.models import Q
import os

# Create your views here.
def myFnc(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES.get('file')
        email = request.POST['email']
        roll = request.POST['roll']
        age = request.POST['age']
        religion = request.POST.get('religion')
        gender = request.POST.get('gender')
        is_Bangladeshi = request.POST.get('is_Bangladeshi')
        date_of_birth = request.POST.get('date_of_birth')
        hobby = request.POST['hobby']
        stu_hobbey = Hobby.objects.create(name=hobby)
        stu_hobbey.save()
        student = Student(name=name,email=email,image=image,roll=roll,age=age,religion=religion,gender=gender,is_Bangladeshi=is_Bangladeshi,date_of_birth=date_of_birth,hobby=stu_hobbey)
        student.save()
        return redirect(home)
            
    return render(request,'add-student.html')

def secFnc(request):
    all_student = Student.objects.all()  
    return render(request,'first.html',locals())

def main(request):
    all_stdudent = Student.objects.all()

    if request.method == 'GET':
        data = request.GET.get('src')
        if data:
            all_stdudent = Student.objects.filter(Q(name__icontains = data) | Q(email__icontains = data))
            print(all_stdudent)

    return render(request, 'main.html',{'stu': all_stdudent})


# def delete_prof(request, prime_id):
#     all_stdudent = Student.objects.get(prime_id=prime_id)
#     if all_stdudent.image != 'def.png':
#         os.remove(all_stdudent.image.path)
#     all_stdudent.delete()

def home (request):
    all_student = Student.objects.all()
    return render (request,'main.html',{'stu':all_student})
def delete_proof(request, prime_id):
    student = get_object_or_404(Student, prime_id=prime_id)

    # Optional: Delete the associated image if it's not the default image
    if student.image and student.image.name != "def.png":
        image_path = student.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
    
    student.delete()
    return redirect('main') 
def update_proof(request,prime_id):
    student= Student.objects.get(prime_id=prime_id)
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES.get('file')
        email = request.POST['email']
        roll = request.POST['roll']
        age = request.POST['age']
        religion = request.POST.get('religion')
        gender = request.POST.get('gender')
        is_Bangladeshi = request.POST.get('is_Bangladeshi')
        date_of_birth = request.POST.get('date_of_birth')
        hobby = request.POST['hobby']
        if student.image and student.image.name != "def.png":
            image_path = student.image.path
            if os.path.exists(image_path):
               os.remove(image_path)

        stu_hobbey = Hobby.objects.create(name=hobby)
        stu_hobbey.save()
        student.name=name
        student.email=email
        student.image=image
        student.roll=roll
        student.age=age
        student.religion=religion
        student.gender=gender
        student.is_Bangladeshi=is_Bangladeshi
        student.date_of_birth=date_of_birth
        student.hobby=stu_hobbey
        student.save()
        return redirect(home)
    return render (request, 'update.html',{'stu':student})
