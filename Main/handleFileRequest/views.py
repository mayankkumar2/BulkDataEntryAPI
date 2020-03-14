from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HackAttendDetails,FileStore
from django.http import HttpResponse,HttpRequest
from django.db import IntegrityError
import pandas as pd
from django.core import serializers

class handleCsvFile(APIView):
    def post(self,request):
        data = pd.read_csv(request.FILES['file']).to_dict('index')
        fileName = request.POST.get('name')
        fileInstance = FileStore(None,fileName)
        fileInstance.save()
        for x in range(len(data)):    
            HackAttendDetails.objects.create(**data[x],fileName=fileInstance)
        return HttpResponse(fileName)	
class getALL(APIView):
    def post(self,request):
        qs_json = serializers.serialize('json', HackAttendDetails.objects.all())
        return HttpResponse(qs_json, content_type='application/json')
class getAllFileNames(APIView):
    def post(self,request):
        qs_json = serializers.serialize('json', FileStore.objects.all())
        return HttpResponse(qs_json, content_type='application/json')
