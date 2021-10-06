import json

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from django.db.models import Q

from Books_Archive.models import Author, Books
from .serializers import BookSerializer
# Create your views here.

@api_view(['GET'])
def books(request):
    books_list = Books.objects.filter(verified=True)
    query_data = request.data or request.query_params
    query_data_copy = query_data.copy()
    #check if user searched by title or if the title was passed
    try:
        if query_data['title'] != "":
            search_list = books_list.filter(
                Q(title__icontains=query_data_copy['title'])
                # Q(category__icontains=query_search) |
                # Q(body__icontains=query_search)
            ).distinct()

        serializer = BookSerializer(search_list, many=True)
        return Response({
            'queryset': serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        pass

    try:
        if query_data['author'] != "":
            search_list = books_list.filter(
                Q(author__name__icontains=query_data_copy['author'])
            ).distinct()

        serializer = BookSerializer(search_list, many=True)
        return Response({
            'queryset': serializer.data
        }, status=status.HTTP_200_OK)

    except Exception as e:
        serializer = BookSerializer(search_list, many=True)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def download(request):
    data = request.data or request.query_params
    if data['id'] != "":
        
        book = Books.objects.filter(id=data["id"])
        serializer = BookSerializer(book, many=True)

        return Response({
            'queryset':serializer.data
        }, status=status.HTTP_200_OK)

