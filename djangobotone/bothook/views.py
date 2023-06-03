from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.views import APIView

# Create your views here.

class WebhookView(APIView):
    def post(self, request):
        print(request.data)
        return Response(status=200)
    
    def get(self, request):
        print(request.data)
        return Response(status=200)