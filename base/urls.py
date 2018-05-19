from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='base'),
    path('competencies/', views.competency_list, name='competency_list'),
    # ex: /competency/1
    path('competencies/<competency_name>/', views.competency_detail,
         name='competency_detail')
]
