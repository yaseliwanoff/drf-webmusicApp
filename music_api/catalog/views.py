from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import authentication
from catalog.serializers import UserSerializer, ArtistSerializator, AlbumSerializator
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from music_api.catalog.models import Artist, Album
from rest_framework.throttling import UserRateThrottle


class UserViewSet(viewsets.ModelViewSet):
    """
    This is API endpoint allow users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class OncePerDayUserThrottle(UserRateThrottle):
	rate = '1/day'


@api_view(['GET', 'POST'])
@throttle_classes([OncePerDayUserThrottle])
def hello_world(request):
	if request.method == 'POST':
		print(request.data)
		return Response({
			'message': f'Got some data: {str(request.data)}'
        })
	return Response({
		'message': 'hello world'
    })


# class ArtistView(APIView):
# 	authentication_classes = [authentication.TokenAuthentication]
# 	permission_classes = [permissions.IsAuthenticated]
# 	throttle_classes = [OncePerDayUserThrottle]
	
# 	def get(self, request):
# 		artist = Artist.objects.all()
# 		return Response(artist)
	
# 	def post(self, request):
# 		return Response({
# 			'data': request.data
#         })


class ArtistGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializator
    permission_classes = [permissions.AllowAny]
    throttle_classes = [UserRateThrottle]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class ArtistDetailGenericView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializator
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class ArtistView(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializator
    permission_class = [permissions.AllowAny]


class ArtistDetailView(RetrieveUpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializator


class AlbumViewSet(viewsets.ModelViewSet):
    # queryset = Album.objects.all()
    serializer_class = AlbumSerializator
    throttle_classes = 'albums'

    def get_queryset(self):
        return Album.objects.all()
