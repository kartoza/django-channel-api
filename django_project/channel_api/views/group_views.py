from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from channels import Group

__author__ = 'Muhammad Anis <anis@kartoza.com>'
__date__ = '09/06/17'


class GroupAPI(APIView):
    """
    Get
    """
    def get(self,request, format=None):
        return Response([])
    """
     Create A new message to spesific group
    """
    def post(self,request, format=None):
        group_name = request.data['group']
        messages = request.data['text']
        data = {"text" : messages}
        # Push it to channel
        Group(group_name).send(data)
        return Response([], status=status.HTTP_201_CREATED)
