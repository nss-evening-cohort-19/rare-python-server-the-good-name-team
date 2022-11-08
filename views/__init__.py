"""Creates views package"""
from .post_request import (create_post,
                           get_all_posts,
                           update_post,
                           delete_post,
                           get_single_post)
from .category_requests import (
    create_category, update_category, get_all_categories, get_single_category, delete_category)
from .tag_request import get_single_tag, get_all_tags, create_tag
