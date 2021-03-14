
from rest_framework import serializers
from .models import Comment, SubComment
from core.models import User

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class SubCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubComment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'fullname', 'email', 'phone')


class SubCommentDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = SubComment
        fields = ('id', 'text', 'user')


class CommentDetailsSerializer(serializers.ModelSerializer):
    sub_comment = SubCommentDetailsSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'name', 'user', 'sub_comment')


