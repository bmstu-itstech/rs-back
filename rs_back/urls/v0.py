from django.urls import include, path


urlpatterns = [
    path('news/', include('news.urls')),
    path('achievements/', include('achievements.urls')),
    path('events/', include('events.urls')),
    path('partners/', include('partners.urls')),
    path('hardathons/', include('hardathons.urls')),
]
