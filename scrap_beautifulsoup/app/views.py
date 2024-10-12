
from rest_framework.generics import ListAPIView
from .serializers import CellDataSerializer
from .models import CellData
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from app.pagination import CustomPagination
import csv
fs=FileSystemStorage(location="tmp/")

class CellDataList(ListAPIView):
    queryset = CellData.objects.all()
    serializer_class = CellDataSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class=CustomPagination
    filterset_fields = ['company', 'status','title']
    search_fields=['company', 'status','title']
    ordering_fields=['price']

class CellDataViewSet(APIView):
    def get(self,request):
        return Response("GET REQUEST IN UPLOAD FILE") 
    def post(self,request):
        file=request.FILES["file"]
        content=file.read()
        file_content=ContentFile(content)
        file_name=fs.save("_tmp.csv",file_content)
        tmp_file=fs.path(file_name)
        csv_file=open(tmp_file,errors='ignore')
        reader=csv.reader(csv_file)
        next(reader)
        cell=[]
        for row in enumerate(reader):
            print(row[1][1])
            site=row[1][1]
            company=row[1][2]
            title=row[1][3]
            price=row[1][4][3:]
            rating_review=row[1][5]
            url=row[1][6]
            status=row[1][7] 
            redirect_url=row[1][8]
            cell.append(CellData(site=site,company=company,title=title,price="Rs. "+price,rating_review=rating_review,url=url,status=status,redirect_url=redirect_url))
        CellData.objects.bulk_create(cell)
        return Response("Uploaded successfully")