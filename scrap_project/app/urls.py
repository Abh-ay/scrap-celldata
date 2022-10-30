
from django.urls import path
from app.views import CellDataList,CellDataViewSet
urlpatterns = [
    path('',CellDataList.as_view()),
    path('upload',CellDataViewSet.as_view())
]
