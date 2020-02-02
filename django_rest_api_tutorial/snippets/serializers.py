from django.contrib.auth.models import User
from rest_framework import serializers
from django_rest_api_tutorial.snippets.models import Snippet, STYLE_CHOICES, LEXERS, LANGUAGE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
