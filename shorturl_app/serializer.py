from rest_framework import serializers
from shorturl_app.models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = '__all__'