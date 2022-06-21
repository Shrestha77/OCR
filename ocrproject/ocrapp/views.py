from django.shortcuts import render
from django.shortcuts import render
import base64

import numpy as np
import pytesseract
from django.contrib import messages
from PIL import Image

from ocrapp.models import User
from ocrapp.form import UserLoginForm, UserRegisterForm

# Create your views here.
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Path to tesseract.exe
)


def register(request):
    urf = UserRegisterForm
    template = 'users/create.html'
    context = {'form': urf}
    if request.method == "POST":
        user = User()
        user.first_name = request.POST.get('first_name')
        user.middle_name = request.POST.get('middle_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.contact = request.POST.get('contact')
        user.password = request.POST.get('password')
        user.save()

        context.setdefault('success', "Registered Sucessful!")
        return render(request, template, context)
    else:
        return render(request, template, context)


def user_login(request):
    form = UserLoginForm
    if request.method == "POST":
        try:
            users = User.objects.get(email=request.POST.get('email'))
            if request.POST.get('password') == users.password:
                template = "dashboard.html"
                request.session['session_email'] = users.email

                if request.session.has_key('session_email'):
                    context = {'success_msg': 'Welcome ' +
                               request.session['session_email']}
                    return render(request, template, context)
                else:
                    context = {'form': form, 'error_msg': 'Acess forbidden'}
                    template = "users/login.html"
                    return render(request, template, context)
            else:
                context = {'form': form,
                           'error_msg': 'Invalid Email or Password'}
                template = "users/login.html"
                return render(request, template, context)
        except:
            context = {'form': form, 'error_msg': 'Not registered yet'}
            template = "users/login.html"
            return render(request, template, context)
    else:
        context = {'form': form, }
        template = "users/login.html"
        return render(request, template, context)


def user_dashboard(request):
    if request.session.has_key('session_email'):
        template = "dashboard.html"
        context = {'success_msg': 'Welcome ' +
                   request.session['session_email']}
        return render(request, template, context)
    else:
        form = UserLoginForm
        context = {'form': form, 'error_msg': 'Acess forbidden'}
        template = "users/login.html"
        return render(request, template, context)


def ocrhomepage(request):
    if request.session.has_key('session_email'):
        template = "ocr.html"
        if request.method == "POST":
            try:
                image = request.FILES["imagefile"]
                # encode image to base64 string
                image_base64 = base64.b64encode(image.read()).decode("utf-8")
            except:
                context = {'messages': 'Image not selected or uploaded'}
                return render(request, template, context)

            img = np.array(Image.open(image))
            text = pytesseract.image_to_string(img)
            context = {"ocr": text, "image": image_base64}
            return render(request, template, context)

        return render(request, template)
    else:
        form = UserLoginForm
        context = {'form': form, 'error_msg': 'Acess forbidden'}
        template = "users/login.html"
        return render(request, template, context)


def user_logout(request):
    if request.session.has_key('session_email'):
        del request.session['session_email']
        form = UserLoginForm
        context = {'form': form, 'error_msg': 'You have logout successfuly'}
        template = "users/login.html"
        return render(request, template, context)
    else:
        form = UserLoginForm
        context = {'form': form, 'error_msg': 'Please login'}
        template = "users/login.html"
        return render(request, template, context)
