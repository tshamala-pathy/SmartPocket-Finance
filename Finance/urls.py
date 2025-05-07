from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report_view, name='report'),
    path('report/pdf/', views.download_report_pdf, name='report_pdf'),
    path('add/', views.add_transaction, name='add_transaction'),
]
