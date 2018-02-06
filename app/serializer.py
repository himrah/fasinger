from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import *
from rest_framework.reverse import  reverse


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ('id','comment_time','comment_by','comment','photo_id')        

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    comments_set = CommentSerializer(required=False,many=True)
    class Meta:
        model = Photos
        fields = ('id','original_photo','thumbs','photo','created_date','upload_by','comments_set')


        