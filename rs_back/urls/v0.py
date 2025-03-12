from django.urls import include, path

urlpatterns = [
    path('news/', include('news.urls')),
]
