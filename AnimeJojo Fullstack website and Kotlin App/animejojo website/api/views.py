from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def listLinks(request):
    linksDictionary = links
    return Response(linksDictionary)