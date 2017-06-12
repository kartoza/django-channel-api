from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

__author__ = 'Muhammad Anis <anis@kartoza.com>'
__date__ = '09/06/17'


class Group(APIView):
    """
    Get
    """
    def get(self,request, format=None):
        return Response([])
    """
     Create A new message to spesific group
    """
    def post(self,request, format=None):
        data = request.data
        return Response([], status=status.HTTP_201_CREATED)
