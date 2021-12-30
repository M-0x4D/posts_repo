from rest_framework.decorators import api_view
from .models import Posts_Model
from .serializers import posts_serializer
from rest_framework.response import Response


@api_view(['GET'])
def posts_api(request):
    prev_posts = Posts_Model.objects.all()
    f_data = posts_serializer(prev_posts, many=True).data
    return Response({'data':f_data})