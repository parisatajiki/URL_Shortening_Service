from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from shorturl_app.models import ShortUrl
from shorturl_app.serializer import ShortUrlSerializer

import random
import string
def generate_short_code(length=5):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


class ShortUrlViewSet(ModelViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            short_url = serializer.validated_data.get('short_url')
            if not short_url:
                serializer.validated_data['short_url'] = generate_short_code()
            instance = serializer.save()
            return Response(self.get_serializer(instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class RetrieveUrl(APIView):
    def get(self, request, url):
        try:
            url = ShortUrl.objects.get(short_url=url)
            serializer = ShortUrlSerializer(url)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ShortUrl.DoesNotExist:
            return Response({"response":f" [{url}] not found"},status=status.HTTP_404_NOT_FOUND)


class DeleteShortUrl(APIView):
    def delete(self, request, url):
        try:
            url = ShortUrl.objects.get(short_url=url)
            url.delete()
            return Response({"response":f" [{url}] deleted"},status=status.HTTP_204_NO_CONTENT)
        except ShortUrl.DoesNotExist:
            return Response({"response":f" [{url}] not found"},status=status.HTTP_404_NOT_FOUND)


class DetailShortUrl(APIView):
    def get(self, request, url):
        try:
            queryset = ShortUrl.objects.get(short_url=url)
            queryset.access_count +=1
            queryset.save(update_fields=['access_count'])
            serializer = ShortUrlSerializer(queryset)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except ShortUrl.DoesNotExist:
            return Response({"response":f" [{url}]not found"},status=status.HTTP_404_NOT_FOUND)
