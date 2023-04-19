from rest_framework import serializers
from .models import Typing

class TypingSerializer(serializers.Serializer) : 
    id = serializers.IntegerField(read_only = True)
    duration = serializers.IntegerField()
    difficulty = serializers.CharField(max_length = 20)
    displayText = serializers.CharField(max_length = 100000)
    inputText = serializers.CharField(max_length = 100000)

    # function to create an instance 
    def create(self, validated_data) : 
        return Typing.objects.create(**validated_data)
    

    def update(self , instance , validated_data) : 
        instance.duration = validated_data.get('duration' , instance.duration )
        instance.difficulty = validated_data.get('difficulty' , instance.duration)
        instance.displayText = validated_data.get('displayText' , instance.displayText)
        instance.inputText = validated_data.get('inputText' , instance.inputText)

        instance.save()
        return instance
