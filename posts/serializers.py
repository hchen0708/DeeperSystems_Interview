from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Post
		fields = [
			"url",
			"id",
			"author",
			"title",
			"post_content",
			"timestamp",
			"slug",
		]


class PostViewSet(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication]
	# permission_classes = [permissions.IsAuthentica]
	queryset = Post.objects.all()
	serializer_class = PostSerializer
