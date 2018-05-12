from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='base'),
    # ex: /competency/1
    path('competency/<int:competency_id>/', views.competency_detail,
         name='competency_detail')
]
