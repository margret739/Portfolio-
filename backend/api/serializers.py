from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User, Profile, Story, Comment


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'is_anonymous']

    def create(self, validate_data):
        if validated_data.get('is_anonymous'):
            validate_data['username'] = None
        return super().create(validate_data)

    def update(self, instance, validated_data):
        if validate_data.get('is_anonymous'):
            validated_data['username'] = None
        return super().update(instance, validated_data)

class StorySerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = ['id', 'title', 'content', 'author', 'author_username', 'created_at']
        
    def get_author_username(self, obj):
        return obj.author.username if not obj.author.is_anonymous else 'Anonymous'
        
class CommentSerializer(serializers.ModelSerializer):
    story_title = serializers.SerializerMethodField()
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'content', 'story', 'story_title', 'author', 'author_username', 'created_at']

    def get_author_username(self, obj):
        return obj.author.username if not obj.author.is_anonymous else 'Anonymous'

    def get_story_title(self, obj):
        return obj.story.story_title

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user