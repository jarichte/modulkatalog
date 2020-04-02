from django.urls import path

from . import views

urlpatterns = [
    path('', views.overview, name='index'),
    path('<str:fak>/', views.overview_by_fak, name='fak'),
    path('<int:modulkat_id>/', views.renderashtml, name='detail'),
    path('<int:modulkat_id>/pdf', views.renderaspdf, name='pdf'),
    path('<int:modulkat_id>/copy', views.copymodel, name='copy')
]
