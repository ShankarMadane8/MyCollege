
from django.urls import path
from . import views
urlpatterns = [
  path("signup/",views.signup,name='signup'),
  path("login/",views.login,name='login'),
  path("logout/",views.logout,name='logout'),
  path("files/",views.fileupload,name='files'),
  path("dashboard/",views.dashboard,name='dashboard'),
  path("update/<int:id>/",views.update,name='update'),
    
]


