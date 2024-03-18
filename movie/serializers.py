from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.movieSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
