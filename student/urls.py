
from django.urls import path
from . import views

urlpatterns = [
    path("",views.show,name="show"),
    path("add/",views.adddata,name="add"),
    path("update/<int:id>",views.updatedata,name="update"),
    path("delete/<int:id>",views.deletedata,name="delete"),
     path('search_student', views.searchstudent, name='searchstudent'),
]
