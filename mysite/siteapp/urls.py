from django.urls import path
from siteapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit-form/',views.submit_form, name='submit_form'),
    path('submissions/',views.view_submissions, name='view_submissions'),
]
