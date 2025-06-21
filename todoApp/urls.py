from django.urls import path
from . import views

urlpatterns = [
    # Add task
    path('addTask/', views.addTask, name='addTask'), #addTask/ -> path, views.addTask - > views is file for business logic and addTask is a function in that file, addTask -> helps for routing or navigating
    
    #Mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'), # create the path and pass the PK, then only we will be able to fetch the data from the databse using the primary key
    
    #Mark as undo
    path('mark_as_undo/<int:pk>/', views.mark_as_undo, name='mark_as_undo'),

    #Edite Feature

]