from django.shortcuts import render, HttpResponse, render_to_response, redirect, HttpResponseRedirect
from .forms import LoginForm, CVForm
from .models import Profile
import datetime
from django.core.urlresolvers import reverse
import os
from gmail import GMail, Message

# Create your views here.


def Login(request):

    UserDB = Profile.objects.all()
    Login_form = LoginForm(request.POST)

    if request.method == 'POST':
        #print(request.POST.get("Username"))
        #print(request.POST.get("Password"))


        userinfo = Profile.objects.get(Username=request.POST.get("Username"))

        context = {'LoginForm': Login_form,

                   }

        print(userinfo.Username)

        if LoginForm.is_valid:

            if UserDB.filter(Username=request.POST.get("Username")) \
                    and UserDB.filter(Password=request.POST.get("Password")):

                return redirect("/%s/cvform" %userinfo.Username)

            else:

                context = {'LoginForm': LoginForm, 'Message': 'Username or Password was wrong or not founded! '
                                                              'Please try again or register new account.'}
                return render(request, 'LoginPage.html', context)

    context = {'LoginForm': LoginForm}
    return render(request, 'LoginPage.html', context)


def NewUser(request):

    if request.method == 'POST':
        Login_form = LoginForm(request.POST)

        if LoginForm.is_valid:
            try:
                FirstName = request.POST.get("FirstName")
                LastName = request.POST.get("LastName")
                Username = request.POST.get("Username")
                Password = request.POST.get("Password")
                Date = datetime.datetime.now()
                new_user = Profile(FirstName=FirstName, LastName=LastName, Username=Username, Password=Password, Date=Date)
                new_user.save()

                context = {"Profile": Profile, "Login_form": Login_form}

                return render(request, 'NewUserPage.html', context)
            except NameError as e:
                context = {"Profile": Profile, "Login_form": Login_form, "message": e}

                return render(request, 'NewUser_error_page.html', context)

    else:
        Login_form = LoginForm

        context = {"Profile": Profile, "Login_form": Login_form}
        return render(request, 'NewUserPage.html', context)


def BaseForm(request, userinfo):
    CV_Form = CVForm(request.POST, request.FILES)
    UserDB = Profile.objects.all()
    User = UserDB.get(Username=userinfo)
    FullName = User.FirstName + " " + User.LastName

    if request.method == 'POST':

        # Profile Info

        User.Position = request.POST.get("Position")
        User.Address = request.POST.get("Address")
        User.Email = request.POST.get("Email")
        User.Tel = request.POST.get("Tel")

        if request.FILES.get("Photo"):
            User.Photo = request.FILES.get("Photo")
            User.Photo.name = User.Username + ".jpeg"
            User.PhotoName = User.Username + ".jpeg"
            print(User.PhotoName)

        else:
            User.Photo = User.Photo

        if request.POST.get("Photo-clear"):
            try:
                #print(User.Photo)
                os.remove(User.Photo.__str__())

                User.Photo = ""
            except:
                print("File not founded!")

        User.LinkedIn = request.POST.get("LinkedIn")

        # Education Info

        User.Date_01 = request.POST.get("Date_01")
        User.Study_Place_1 = request.POST.get("Study_Place_1")
        User.Degree_1 = request.POST.get("Degree_1")

        User.Date_02 = request.POST.get("Date_02")
        User.Study_Place_2 = request.POST.get("Study_Place_2")
        User.Degree_2 = request.POST.get("Degree_2")

        User.Date_03 = request.POST.get("Date_03")
        User.Study_Place_3 = request.POST.get("Study_Place_3")
        User.Degree_3 = request.POST.get("Degree_3")

        User.Date_04 = request.POST.get("Date_04")
        User.Study_Place_4 = request.POST.get("Study_Place_4")
        User.Degree_4 = request.POST.get("Degree_4")

        # Work Experience Info

        User.WorkDate1 = request.POST.get("WorkDate1")
        User.Work1 = request.POST.get("Work1")
        User.Position1 = request.POST.get("Position1")

        User.WorkDate2 = request.POST.get("WorkDate2")
        User.Work2 = request.POST.get("Work2")
        User.Position2 = request.POST.get("Position2")

        User.WorkDate3 = request.POST.get("WorkDate3")
        User.Work3 = request.POST.get("Work3")
        User.Position3 = request.POST.get("Position3")

        User.WorkDate4 = request.POST.get("WorkDate4")
        User.Work4 = request.POST.get("Work4")
        User.Position4 = request.POST.get("Position4")

        User.WorkDate5 = request.POST.get("WorkDate5")
        User.Work5 = request.POST.get("Work5")
        User.Position5 = request.POST.get("Position5")

        User.WorkDate6 = request.POST.get("WorkDate6")
        User.Work6 = request.POST.get("Work6")
        User.Position6 = request.POST.get("Position6")


        # Skills Info

        User.Skill_1 = request.POST.get("Skill_1")
        User.Skill_2 = request.POST.get("Skill_2")
        User.Skill_3 = request.POST.get("Skill_3")
        User.Skill_4 = request.POST.get("Skill_4")
        User.Skill_5 = request.POST.get("Skill_5")
        User.Skill_6 = request.POST.get("Skill_6")
        User.Skill_7 = request.POST.get("Skill_7")
        User.Skill_8 = request.POST.get("Skill_8")
        User.Skill_9 = request.POST.get("Skill_9")
        User.Skill_10 = request.POST.get("Skill_10")
        User.Skill_11 = request.POST.get("Skill_11")
        User.Skill_12 = request.POST.get("Skill_12")
        User.Skill_13 = request.POST.get("Skill_13")
        User.Skill_14 = request.POST.get("Skill_14")
        User.Skill_15 = request.POST.get("Skill_15")
        User.Skill_16 = request.POST.get("Skill_16")
        User.Skill_17 = request.POST.get("Skill_17")
        User.Skill_18 = request.POST.get("Skill_18")
        User.Skill_19 = request.POST.get("Skill_19")
        User.Skill_20 = request.POST.get("Skill_20")
        User.Skill_21 = request.POST.get("Skill_21")
        User.Skill_22 = request.POST.get("Skill_22")
        User.Skill_23 = request.POST.get("Skill_23")
        User.Skill_24 = request.POST.get("Skill_24")
        User.Skill_25 = request.POST.get("Skill_25")
        User.Skill_26 = request.POST.get("Skill_26")
        User.Skill_27 = request.POST.get("Skill_27")
        User.Skill_28 = request.POST.get("Skill_28")
        User.Skill_29 = request.POST.get("Skill_29")
        User.Skill_30 = request.POST.get("Skill_30")

        # Language Info

        User.Language_1 = request.POST.get("Language_1")
        User.Language_1_Quality = request.POST.get("Language_1_Quality")

        User.Language_2 = request.POST.get("Language_2")
        User.Language_2_Quality = request.POST.get("Language_2_Quality")

        User.Language_3 = request.POST.get("Language_3")
        User.Language_3_Quality = request.POST.get("Language_3_Quality")

        User.Language_4 = request.POST.get("Language_4")
        User.Language_4_Quality = request.POST.get("Language_4_Quality")

        User.Language_5 = request.POST.get("Language_5")
        User.Language_5_Quality = request.POST.get("Language_5_Quality")

        # Certificates Info

        User.Certificate_1 = request.POST.get("Certificate_1")
        User.Certificate_2 = request.POST.get("Certificate_2")
        User.Certificate_3 = request.POST.get("Certificate_3")
        User.Certificate_4 = request.POST.get("Certificate_4")
        User.Certificate_5 = request.POST.get("Certificate_5")
        User.Certificate_6 = request.POST.get("Certificate_6")
        User.Certificate_7 = request.POST.get("Certificate_7")
        User.Certificate_8 = request.POST.get("Certificate_8")
        User.Certificate_9 = request.POST.get("Certificate_9")
        User.Certificate_10 = request.POST.get("Certificate_10")

        User.save()

        contex = {"userinfo": Profile.objects.get(Username=userinfo), "CV_Form": CV_Form, "FullName": FullName}
        return render(request, 'CVForm.html', contex)
    else:
        contex = {"userinfo": Profile.objects.get(Username=userinfo), "CV_Form": CV_Form, "FullName": FullName}
        return render(request, 'CVForm.html', contex)


def Preview(request, userinfo):
    UserDB = Profile.objects.all()
    User = UserDB.get(Username=userinfo)
    FullName = User.FirstName + " " + User.LastName

    contex = {"userinfo": Profile.objects.get(Username=userinfo), "FullName": FullName}

    return render(request, 'index.html', contex)



def contact(request):

    return render(request, 'contact.html')

def send_mail(request):
    if request.method == "POST":

        Name = request.POST.get("Name")
        From = request.POST.get("Email")
        message = request.POST.get("Message")

        if '@' in From:

            gmail = GMail('<PythonCVSite@gmail.com>', '123456789F!')
            msg = Message('Test Message', to='<jkarimov@azerfon.az>',
                          text='You received mail from %s \n\n Email: %s \n\n' % (Name, From) + message)
            gmail.send(msg)
            return render(request, 'contactthanks.html')
        else:
            return render(request, 'error.html')

    return render(request, 'contactthanks.html')

def error(request):
    return render(request, 'error.html')


import pdfkit
from django.http import HttpResponse

def pdf(request, userinfo):
    from cv_portal.settings import STATIC_URL

    UserDB = Profile.objects.all()
    User = UserDB.get(Username=userinfo)


    options = {
        'page-size': 'Letter',

        'margin-top': '0.1cm',
        'margin-right': '0.1cm',
        'margin-bottom': '0.1cm',
        'margin-left': '0.1cm',
        'encoding': "UTF-8",
        'no-outline': None,
        'quiet': '',
        'no-pdf-compression': None,
        'enable-forms': None,


           }

    try:

        pdfkit.from_url("http://127.0.0.1:8000/%s/preview" %User.Username, "D:\\My_resume.pdf", options=options)
        return HttpResponse("Your resume file was saved to D drive as My_resume.pdf.")

    except OSError as PermissionError:
        return HttpResponse (PermissionError)