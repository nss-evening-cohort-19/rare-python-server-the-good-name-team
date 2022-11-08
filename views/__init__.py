"""Creates views package"""
from .post_request import (create_post,
                           get_all_posts,
                           update_post,
                           delete_post)
from .category_requests import (
    create_category, update_category, get_all_categories, get_single_category, delete_category)
from .comment_requests import (create_comment, get_post_comments, update_comment, delete_comment)
