from app import ma


class PostSchema(ma.Schema):
	class Meta:
		ordered = True
		fields = ('pk', 'title', 'slug', 'body', 'author', 'created', 'updated', 'status', 'featured')


post_schema = PostSchema()
posts_schema = PostSchema(many=True)