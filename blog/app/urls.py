from django.conf.urls import url
from django.urls import path 
# from.import views home, about
# from .views import 
from .import views

urlpatterns = [
    path("",views.base,name="base"),
    path("about.html",views.about,name="about"),
    path("login.html",views.login,name="login"),
    path("signup.html",views.signup,name='signup'),
    path("contact.html",views.contact,name="contact"),
    path("helpline.html",views.helpline,name="helpline"),
    path("donation.html",views.donation,name="donation"),
    path("vfaq.html",views.vfaq,name="vfaq"),
    
    path("vaccine.html",views.vaccine,name="vaccine"),
    path("covid.html",views.covid,name="covid"),
    # url(r'^home/search$',views.search),
    path('handlesignup', views.handlesignup, name='handlesignup'),
    path("handlelogin",views.handlelogin,name="handlelogin"),
    path("handlelogout",views.handlelogout,name="handlelogout"),
    path("contact",views.contact,name="contact"),


]