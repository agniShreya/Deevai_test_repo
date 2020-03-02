# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, HttpResponse,\
    render_to_response

# Create your views here.
#import MySQLdb
import sqlite3
from django.views.generic import FormView
from django.views.generic import UpdateView
#from AddressBookApp.forms import UserProfileForm
from django.views import View
from django.shortcuts import get_object_or_404
from AddressBookApp.models import AddressBookApplication
from AddressBookApp.forms import AddressBookForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
#from django.views.generic import AddressbookView
from django.http import HttpResponse
from django.shortcuts import redirect
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template.context_processors import request
from AddressBookApp.forms import UpdateAddressBookForm
from AddressBookApp.forms import SignUpForm
from AddressBookApp.forms import UpdateProfile

class SignUp(View):
    
    def get(self,request):
       try:
        form = SignUpForm()
        return render(request, "signup.html", {'form':form })
       except:
        return render(request, 'error.html')
    
    def post(self,request):
        if request.method == 'POST':  
         form = SignUpForm(request.POST)
         if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, "login.html")
         else:
            form = SignUpForm()
            return render(request, "signup.html", {'form':form })
            
        
        



class LoginView(View):
    
    def get(self, request):
      try:
        return render(request, "login.html")
      except:
        return render(request, 'error.html')

    def post(self, request):
      try:
        formData = request.POST.copy()
        usernameui=request.POST['username']
        passwordui=request.POST['password']
        userExist = User.objects.filter(username=usernameui).exists()
        m = User.objects.get(username=usernameui)
        if userExist == False:
            return render(request, "login.html",{'error':'You are not an authorized User'})
        else:
            print("else")
            user = authenticate(username=usernameui, password=passwordui)
            if user is not None:
                request.session['user_id'] =  m.id
                return render(request, 'index.html' , {'username': m })
            else:
                return render(request, "login.html",{'error':'Please enter correct password'})
        return render(request, "index.html")
      except:
         return render(request, 'error.html')

class LogoutView(View):
    
    def get(self, request):
        request.session.flush()
        return render(request, "logout.html")
    
      


class AddressBook(View):

  
  def get(self, request):
   try:
    return render(request, 'index.html', {})
   except:
    return render(request, 'error.html')
    #return HttpResponse("Hello, world. You're at the polls index.")
  def post(self, request):
   try:
    if request.method == 'POST':
        myform = AddressBookForm(request.POST)
        email = request.POST['email_address']
        emailExist = AddressBookApplication.objects.filter(email_address=email).exists()
        # check whether it's valid:
        if emailExist == False:
          if myform.is_valid():
            form = myform.save(commit=True)
            form.save()
            return HttpResponseRedirect('/home/')
        else:
            form = AddressBookForm()
            message = "Emailid is already existing."
            return render(request, 'index.html', {'form': form , 'message':message})
    
    else:
        myform =  AddressBookForm()
        return render(request,  'index.html', {'myform': myform})
   except:
    return render(request, 'error.html') 
    
    #myform = AddressBookForm()
    #return render(request, 'index.html', { 'myform' : myform})

class AddressBookView(View):
    #model = AddressBookApplication
    
    def get(self,request):
      try:
        model = AddressBookApplication()
        all_user= AddressBookApplication.objects.all()
        print(all_user)
        return render(request, 'user_table.html', {'all_user': all_user })
      except:
        return render(request, 'error.html')
    
class EditContact(View):
    #book_inst=get_object_or_404(AddressBookApplication, email_address=email)
    
    def get(self,request):
        try:
          return render(request, 'edit.html')
        except:
          return render(request, 'error.html')
            
        
        
        
    def post(self,request):
        try:
            email =request.POST['email']
            print(email)
            emailExist = AddressBookApplication.objects.filter(email_address=email).exists()
            print(emailExist)
            if emailExist:
                contact= AddressBookApplication.objects.get(email_address=email)
                form = UpdateAddressBookForm(instance=contact)
                return render(request, 'update.html', {'form' : form , 'email' : email})
            else:
                message = "Please enter an existing email id to update"
                return render(request, 'edit.html',{'message': message})
        except:
            return render(request, 'error.html')
                
                

class deleteView(View):
    
        def get(self,request):
            try:
               message =  "Please enter email to delete the contact"
               return render(request, 'edit.html' , {'message' : message})
            except:
               return render(request, 'error.html')
        
        def post(self,request):
          try:
            formData = request.POST.copy()
            email =request.POST['email']
            print(email)
            address = AddressBookApplication.objects.filter(email_address=email).exists()
            print(address)
            if address:
                contact= AddressBookApplication.objects.get(email_address=email)
                contact.delete()
                message = "You have deleted the contact "+  str(email)
                return render(request, 'edit.html', {'message' :message })
            else:
                message = "No email ID found to delete"
                return render(request, 'edit.html', {'message' : message})
          except:
            return render(request, 'error.html')
 
            
class UpdateView(View):
    
    
    
    def post(self,request):
        try:   
          if request.method == 'POST':
             formdata = UpdateAddressBookForm(request.POST)
             emailid =request.POST.get('email')
             #print(emailid)
             fname = request.POST['first_name']
             lname = request.POST['last_name']
             num = request.POST['phone_number']
             zipcode = request.POST['zip_code']
             city =  request.POST['city']
             state = request.POST['state']
             notes = request.POST['notes']
             AddressBookApplication.objects.filter(email_address=emailid).update(first_name=fname, last_name=lname,phone_number=num,zip_code=zipcode,city=city,state=state,notes=notes)
             msg = "Contact has been updated"
             return render(request, 'update.html',{'message': msg})
        except:
             return render(request, 'error.html')
                 
      
class AddContactView(View):
    
     def get(self,request):
       try:
         form = AddressBookForm()
         return render(request, 'addform.html', {'form': form})
       except:
         return render(request, 'error.html')
     
     def post(self,request):
       try:
         if request.method == 'POST':
          form = AddressBookForm()
          myform = AddressBookForm(request.POST)
          email = request.POST['email_address']
          emailExist = AddressBookApplication.objects.filter(email_address=email).exists()
        # check whether it's valid:
          if emailExist == False:
             if myform.is_valid():
               form = myform.save(commit=True)
               form.save()
               message= "contact has been added successfully"
               return render(request, 'addform.html', { 'form': form , 'message': message})
          else:
             form = AddressBookForm()
             message = "Emailid is already existing."
             return render(request, 'addform.html', {'form': form , 'message':message})
         else:
           myform =  AddressBookForm()
           return render(request,  'addform.html', {'myform': myform})
       except:
            return render(request, 'error.html')
         
    
    
class UserProfileView(View):

    
    def post(self,request):
       try:
        logged_user = request.POST.get('username')
        print(logged_user)
        userExist = User.objects.filter(username=logged_user).exists()
        print(userExist)
        contact= User.objects.get(username=logged_user)
        form = UpdateProfile(instance=contact)
        return render(request, 'UserProfile.html', {'form' : form , 'email' : logged_user})
       except:
        return render(request, 'error.html')
        
    
    

class UpdateUser(View):
    
    
        def get(self,request):
            logged_user = request.post['username']
            print(logged_user)
            userExist = User.objects.filter(username=logged_user).exists()
            print(userExist)
            contact= User.objects.get(username=logged_user)
            form = UpdateProfile(instance=contact)
            return render(request, 'UserProfile.html', {'form' : form })
       
        def post(self,request):
            if request.method == 'POST':
              formdata = UpdateProfile(request.POST)
              username1 =request.POST.get('username')
              fname = request.POST['first_name']
              lname = request.POST['last_name']
              emailid = request.POST['email']
              print(username1)
              print(fname, lname)
              User.objects.filter(username=username1).update(first_name=fname, last_name=lname, email=emailid)
              msg = "Your details has been updated"
              return render(request, 'UserProfile.html' , { "msg": msg} )
            else:
              return render(request, "error.html" )
                 
                 
    
    
    
           


