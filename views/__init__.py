"""Creates views package"""
from .category_request import (create_category, delete_category,
                               get_all_categories, get_single_category,
                               update_category)
from .comment_requests import (create_comment, delete_comment,
                               get_all_comments, get_single_comment,
                               update_comment)
from .post_request import (create_post, delete_post, get_all_posts,
                           get_single_post, update_post)
from .post_tag_request import (create_post_tag, delete_post_tag,
                               get_post_tags_by_post_id)
from .tag_request import (create_tag, get_all_tags, get_single_tag)
