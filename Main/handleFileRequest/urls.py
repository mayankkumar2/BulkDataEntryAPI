from django.urls import path
from . import views

urlpatterns = [
    path('addBulk',views.handleCsvFile.as_view()),
    path("getALL",views.getALL.as_view()),
    path("getAllFileName",views.getAllFileNames.as_view())
]