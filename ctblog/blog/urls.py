from django.urls import path
from .views import home_page,LoginPage,SignupPage,LogoutPage,cntact_us
app_name = "blog"

urlpatterns = [
    path('home/',home_page, name="home"),
     path('',SignupPage,name='signup'),
    path("login/",LoginPage,name="login"),
    path("signup/",SignupPage,name="signup"),
    path('logout/',LogoutPage,name='logout'),
    path("contact-us" , cntact_us, name="contact-us")
]