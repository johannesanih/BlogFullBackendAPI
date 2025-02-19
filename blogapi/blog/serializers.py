from rest_framework import serializers
from .models import BlogPost, Comment, Like
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BlogPostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'created_at', 'comments', 'likes']

    def get_comments(self, obj):
        return CommentSerializer(obj.comments.all(), many=True).data

    def get_likes(self, obj):
        return obj.likes.count()

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'created_at']