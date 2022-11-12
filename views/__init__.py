"""Creates views package"""
from .post_request import (create_post,
                           get_all_posts,
                           update_post,
                           delete_post,
                           get_single_post)
from .category_request import (
    create_category, update_category, get_all_categories, get_single_category, delete_category)
from .comment_requests import (create_comment, get_all_comments, get_single_comment, delete_comment, update_comment)
from .tag_request import get_single_tag, get_all_tags, create_tag
from .post_tag_request import create_post_tag, delete_post_tag, get_post_tags_by_post_id
