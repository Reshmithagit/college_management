from django.shortcuts import render,redirect
from .models import Addcourse,Student,Teacher
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required(login_url='home')
def adminpanel(request):
    return render(request,'adminpanel.html')

@login_required(login_url='home')
def add_course(request):
    return render(request,'add_course.html')

@login_required(login_url='home')
def add_student(request):
    courses=Addcourse.objects.all()
    return render(request,'add_student.html',{'course':courses})
    
def signup(request):
    course=Addcourse.objects.all()
    return render(request,'signup.html',{'cs':course})

@login_required(login_url='home')
def courseadd(request):
    if request.method=='POST':
        coursename=request.POST['course_name']
        coursefee=request.POST['fee']
        add=Addcourse(coursename=coursename,coursefee=coursefee)
        add.save()
        return redirect('add_student')
    
@login_required(login_url='home')
def std_add(request):
    if request.method=='POST':
        sname=request.POST['name']
        add=request.POST['addr']
        age=request.POST['age']
        date=request.POST['date']
        sel=request.POST['sel']
        course1=Addcourse.objects.get(id=sel)
        std=Student(stdname=sname,Address=add,age=age,date=date,course=course1)
        std.save()
        return redirect('showstd_details')
    
@login_required(login_url='home')    
def showstd_details(request):
    std=Student.objects.all()
    return render(request,'showstd_details.html',{'st':std})

@login_required(login_url='home')
def edit(request,pk):
    std=Student.objects.get(id=pk)
    course=Addcourse.objects.all()
    return render(request,'edit.html',{'student':std,'cs':course})

@login_required(login_url='home')
def edit_details(request,pk):
    if request.method=='POST':
        stud=Student.objects.get(id=pk)
        stud.stdname=request.POST['sname']
        stud.Address=request.POST['addr']
        stud.age=request.POST['age']
        stud.date=request.POST['jdate']
        sel=request.POST['sel']
        fee=request.POST['fee']
        course1=Addcourse.objects.get(id=sel)
        course1.coursefee=fee
        course1.save()
        stud.course=course1
        stud.save()
        return redirect('showstd_details')
    return render(request,'edit.html')

@login_required(login_url='home')
def delete(request,pk):
    std=Student.objects.get(id=pk)
    std.delete()
    return redirect('showstd_details')

def reg(request):
    if request.method =='POST':
        fname=request.POST['std_name']
        lname=request.POST['lname']
        uname=request.POST['uname']
        pswd=request.POST['pass']
        cpswd=request.POST['cpass']
        email=request.POST['email']
        addr=request.POST['addr']
        age=request.POST['age']
        number=request.POST['cnum']
        sel=request.POST['sel']
        img=request.FILES.get('img')
        if pswd==cpswd: 
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('signup')
            else:
                 user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=uname,
                    password=pswd,
                    email=email)
                 user.save()
                 course2=Addcourse.objects.get(id=sel)
                 u=User.objects.get(id=user.id)
                 reg=Teacher(address=addr,age=age,contact=number,course=course2,img=img,user=u)
                 reg.save()
                 return redirect('home')
        else:
            messages.info(request,'password incorrect')
            return redirect('/')
        
        
def adminlogin(request):
     if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pswd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                # print('welcome')
                login(request,user)
                return redirect('adminpanel')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'welcome {username}')
                return redirect('th_home')
        else:
            messages.info(request,'invalid username& password')
            return redirect('home')
     return render(request,'home.html')

@login_required(login_url='home')
def logout1(request):
    auth.logout(request)
    return redirect('home')  
 
@login_required(login_url='home')
def showtchr(request):
        teacher=Teacher.objects.all()
        return render(request,'showtchr.html',{'th':teacher})

@login_required(login_url='home')
def delete_th(request,pk):
    te=Teacher.objects.get(user=pk)
    us=User.objects.get(id=pk)
    te.delete()
    us.delete()
    return redirect('showtchr')


@login_required(login_url='home')
def profile(request):
    if request.user.is_authenticated:
        current_user=request.user.id
        user1=Teacher.objects.get(user_id=current_user)
        return render(request,'profile.html',{'users':user1})
     
     

    #  return render(request,'profile.html')
@login_required(login_url='home')
def th_home(request):
    
    return render(request, 'th_home.html')


@login_required(login_url='home')
def th_edit(request):
    teacher = Teacher.objects.get(user=request.user)
    courses=Addcourse.objects.all()
    return render(request, 'th_edit.html', {'tea': teacher,'course':courses})

@login_required(login_url='home')
def edit_details1(request, pk):
    if request.method == 'POST':
        teacher = Teacher.objects.get(user=pk)
        user=User.objects.get(id=pk)
        user.first_name = request.POST['std_name']
        user.last_name = request.POST['lname']
        user.username = request.POST['uname']
        user.email = request.POST['email']
        teacher.address=request.POST['addr']
        teacher.age = request.POST['age']
        teacher.contact = request.POST['cnum']
        courseid = request.POST['sel']
        course=Addcourse.objects.get(id=courseid)
        teacher.course=course
        teacher.img = request.FILES.get('img')     
        teacher.save()  
        user.save()
        messages.success(request, 'Details updated successfully.')
        return redirect('profile')
    




