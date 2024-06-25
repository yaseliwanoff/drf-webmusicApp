from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from catalog import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('hello-world/', views.hello_world, name='hello-world'),
    path('artist/', views.ArtistView.as_view(), name='artist')
]