
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


def index_view(request):
    return Response({'status':status.HTTP_200_OK})
