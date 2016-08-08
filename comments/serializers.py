from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .models import Comment

class CommentSerializer(serializers.HyperlinkedModelSerializer):
	# post = PostSerializer()
	# parent = serializers.SerializerMethodField(read_only=True)

	# def get_parent(self, instance):
	# 	queryset = instance.get_parent()
	# 	serializer = PostSerializer(queryset, context={"request": instance}, many=True)
	# 	return serializer.data

	class Meta:
		model = Comment
		fields = [
			"url",
			"id",
			"author",
			"comment_content",
			"timestamp",
			"parent",
		]


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer