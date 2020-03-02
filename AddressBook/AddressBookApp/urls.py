from django.conf.urls import url,include
#from django.conf.urls import patterns, url

#from polls import views
from AddressBookApp.views import AddressBook
from AddressBookApp.views import *
from django.views import View
#from django.urls import path

urlpatterns = [
    #url(r'^admin/', admin.site.urls),

    #path(r'home/', AddressBook.as_view(), name = 'home'),
    url(r'home/', AddressBook.as_view(), name = 'home'),
    url(r'login/', LoginView.as_view(), name = 'login'),
    #path(r'login/', LoginView.as_view(), name = 'login'),
    url(r'logout/', LogoutView.as_view(), name = 'logout'),
    #path(r'logout/', LogoutView.as_view(), name = 'logout'),
    url(r'users/', AddressBookView.as_view(), name = 'users'),
    url(r'editinfo/', EditContact.as_view(), name = 'editinfo'),
    url(r'deleteView/',deleteView.as_view(), name = 'delete'),
    url(r'updateView/', UpdateView.as_view(), name = 'update'),
    url(r'signup/', SignUp.as_view(), name='signup'),
    url(r'UserProfile/', UpdateUser.as_view(), name= 'Userprofile'),
    url(r'addcontact/',AddContactView.as_view(), name = 'add'),
    url(r'editUserProfile/', UserProfileView.as_view(), name= 'editUserprofile'),

     
     
#    url(r'^$', views.home, name = 'home'),
]
