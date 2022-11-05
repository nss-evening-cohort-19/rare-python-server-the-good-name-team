class Comment():
    """AI is creating summary for Comment
    """

    def __init__(self, id, user_id, post_id, content):
        self.id = id
        self.user_id = user_id
        self.post_id = post_id
        self.content = content

new_comment = Comment(1, 2, 3, "hello")
        