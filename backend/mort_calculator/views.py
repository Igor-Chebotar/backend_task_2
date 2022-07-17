from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView, Response


class CreateMortgage(APIView):

    def post(self, request, format=None):
        print('test')
        return Response('test', status=status.HTTP_201_CREATED)
