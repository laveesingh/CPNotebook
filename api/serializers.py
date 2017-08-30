from rest_framework import serializers

from api.models import Post

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('author', 'creation', 'last_edit', 'title', 'content')
