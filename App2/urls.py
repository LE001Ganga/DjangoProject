from django.urls import path
from App2 import views
from django.contrib.auth import views as as_views


urlpatterns=[
    # path('home/',views.hometown,name="hometown"),
     path('index/',views.index,name='index'),
    # path('StudentUrl/',views.Student,name="Student"),
    # path('valueurl/<int:num>',views.sendValue,name='sendValue'),
    # path('sample/',views.sample,name="sample"),
    path('registerurl/',views.register,name="register"),
    path('display/',views.display_details,name='details'),
    path('update/<int:id>',views.update_details,name="update"),
    path('delete/<int:id>',views.delete_details,name="delete"),
    path('signup/',views.signup,name='signup'),
    path('userregistration/',views.registration,name='registration'),
    path('showData/',views.showData,name='showData'),
    path('signupform/',views.signupForm,name='signupform'),
    path('login/',as_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',as_views.LogoutView.as_view(),name='logout'),
    path('profile/',views.profile,name='profile'),

]