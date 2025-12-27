from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .models import Task
from .serializers import TaskSerializer


@csrf_exempt
@api_view(['POST'])
@parser_classes([JSONParser])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)
