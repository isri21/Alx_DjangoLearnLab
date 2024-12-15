from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ["author", "title", "content", "created_at", "updated_at"]
		# These three fields will only displayed for GET method
		read_only_fields = ["author", "created_at", "updated_at"]

	# Customize the method to create a new post instance
	def create(self, validated_data):
		# Manually adding an author key in the validate_data dictionary
		# The value will be passed by the user when the call serializer.save(created_by=request.user)
		validated_data["author"] = self.context.get("created_by")
		return Post.objects.create(**validated_data)

	
class CommentSerializer(serializers.ModelSerializer):

	# Nested Serializer for related post data
	post = PostSerializer()
	class Meta:
		model = Comment
		fields = ["author", "content", "created_at", "updated_at", "post"]
	
		# These three fields will only displayed for GET method
		read_only_fields = ["author", "created_at", "updated_at"]

		def create(self, validated_data):
			# Manually adding an author key in the validate_data dictionary
			# The value will be passed by the user when the call serializer.save(created_by=request.user)
			validated_data["author"] = self.context.get("created_by")
			return Post.objects.create(**validated_data)