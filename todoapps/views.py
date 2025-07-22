from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers

from . models import Todo
from . serializers import TodoSerializers

# Create your views here.
class TodoView(APIView):
    def get(self,Request):
        try:
            todo = Todo.objects.all()
            serializers = TodoSerializers(todo, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self,Request):
        try:
            serializers = TodoSerializers(data = Request.data)
            if serializers.is_valid():
                serializers.save()
                return Response({'message':'Task created successfully'}, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'Error':str(e)}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class TodoDetail(APIView):

    def get(self, Request):
        try:
            todo = Todo.objects.get(id=id)
            serializers = TodoSerializers(todo)
            return Response(serializers.data,status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'Error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def put(self, Request):
        try:
            todo = Todo.objects.get(id=id)
            serializers = TodoSerializers(todo)
            if serializers.is_valid():
                serializers.save()
                return Response({'message':'Task updated succesfully'}, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def delete(self, Request):
        try:
            todo = Todo.objects.get(id=id)
            del todo
            return Response({'message':f'{todo.title} was deleted successufully'})

        except Exception as e:
            return Response({'Error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
