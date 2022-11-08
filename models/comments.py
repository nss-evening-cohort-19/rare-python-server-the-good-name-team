class Comment():
    """AI is creating summary for Comment
    """

    def __init__(self, id, author_id, post_id, content, category_id, title, publication_date, image_url):
        self.id = id
        self.author_id = author_id
        self.post_id = post_id
        self.content = content
        self.category = category_id
        self.title = title
        self.post_content = content
        self.date = publication_date
        self.image = image_url
