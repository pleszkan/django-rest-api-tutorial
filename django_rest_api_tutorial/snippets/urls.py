from django.urls import path, include

urlpatterns = [
    path('', include('django_rest_api_tutorial.snippets.urls')),
]
