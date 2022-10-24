from django.urls import path
from . import views
from .views import ProjektasListView, ManoProjektaiListView, ManoProjektasDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('darbai/', views.darbai, name='darbai'),
    path('projektai/', ProjektasListView.as_view(), name='projektai'),
    path('manoprojektai/', views.ManoProjektaiListView.as_view(), name='manoprojektai'),
    path('manoprojektai/<int:pk>', views.ManoProjektasDetailView.as_view(), name='manoprojektas'),
]