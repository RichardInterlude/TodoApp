from rest_framework import serializers # type: ignore
from . models import Todo

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title','description','completed','created','updated']



