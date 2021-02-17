from django.shortcuts import render,redirect
from django.http import HttpResponse
from App2.models import Student,Registration,UserProfile
from App2.forms import StudentForm,RegisterForm
from django.contrib import messages
from DjangoProject import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User


#Create your views here.
def static(request):
    return HttpResponse("<h1>Hi This app 2</h1>")
def index(request):
    return render(request,'index.html')
def hometown(request):
    return HttpResponse("Django/App2")

# def Student(request):
#     details={'Name':'Ganga','Pin':'19555A0501','Branch':'CSE'}
#     return render(request,'StudentInfo.html',{'details':details})
def sendValue(request,num):
    mul=[]
    for i in range(1,11):
        mul.append(i*num)
    return render(request,'StudentInfo.html',{'value':mul,'num':num})
def sample(request):
    return render(request,'sample.html')



def register(request):
    if(request.method=='POST'):
        Name=request.POST.get('FullName')
        Pin=request.POST.get('RollNo')
        email=request.POST.get('EmailId')
        phoneno=request.POST.get('MobileNo')
        dob=request.POST.get('Date_Of_Birth')
        gender=request.POST.get('Gender')
        Address=request.POST.get('Address')

        
        Student.objects.create(FullName=Name,RollNo=Pin,EmailId=email,MobileNo=phoneno,Date_Of_Birth=dob,Gender=gender,Address=Address)
        # context = {'Name':Name,'Pinno':Pin,'mail':email,'PhoneNo':phoneno,'DOB':dob,'Gender':gender,'Address':Address}
        # return render(request,'result.html',context)
    return render(request,'register.html')

def display_details(request):
    data=Student.objects.all()
    return render(request,"result.html",{'data':data})
def update_details(request,id):
    data=Student.objects.get(id=id)
    if(request.method=='POST'):
        Name=request.POST.get('FullName')
        Pin=request.POST.get('RollNo')
        email=request.POST.get('EmailId')
        phoneno=request.POST.get('MobileNo')
        dob=request.POST.get('Date_Of_Birth')
        gender=request.POST.get('Gender')
        Address=request.POST.get('Address')

        data.FullName=Name
        data.RollNo=Pin
        data.EmailId=email
        data.MobileNo=phoneno
        data.Date_Of_Birth=dob
        data.Gender=gender
        data.Address=Address
        data.save()
        return redirect('details')
    return render(request,'update.html',{'data':data})
def delete_details(request,id):
    Student.objects.get(id=id).delete()
    return redirect('details')
def signup(request):
    if request.method=='POST':
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,"SignUp completed")
            return redirect('signup')

    form=StudentForm()
    return render(request,"signup.html",{'form':form})

def registration(request):
    if(request.method=='POST'):
        Name=request.POST.get('uname')
        Password=request.POST.get('pwsd')
        Email=request.POST.get('email')
        Image=request.FILES['image']

        Registration.objects.create(Username=Name,Password=Password,Email=Email,Image=Image)

        sub ='reg welcome message'
        body = 'username'+Name+'Password'+Password
        reciever = Email
        sender = settings.EMAIL_HOST_USER
        send_mail(sub,body,sender,[reciever])

        return redirect('showData')
        
    return render(request,'registration.html')
def showData(request):
    data = Registration.objects.all()
    return render(request,'ShowData.html',{'objs':data})


def signupForm(request):
    if request.method=='POST':
        sform = RegisterForm(request.POST)
        if sform.is_valid:
            sform.save()
            return HttpResponse("successfully registerd")
    else:
        sform = RegisterForm()
        return render(request,'signupform.html',{'sform':sform})

def profile(request):
    user= User.objects.get(id=request.user.id)
    pro = UserProfile.objects.get(user=user)
    return render(request,'profile.html',{'user':user,'pro':pro})