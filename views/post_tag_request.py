import sqlite3
import json
from models import PostTag
from models import Tag

def get_all_post_tags():
    """Gets all postsTags"""
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
      SELECT
        pt.id,
        pt.post_id,
        pt.tag_id
      FROM PostTag pt
      JOIN Post p
      ON p.id = pt.post_id
      JOIN Tag t
      ON t.id = pt.tag_id
      """)

        post_tags = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post_tag = PostTag(row['id'], row['post_id'], row['tag_id'])
            post_tags.append(post_tag.__dict__)

    return json.dumps(post_tags)


def get_single_post_tag(id):
    """Gets a single postTag"""
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()


        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id
        FROM Posttag pt
         WHERE pt.id = ?
        """, ( id, ))


        data = db_cursor.fetchone()

        post_tags = PostTag(data['id'], data['postId'], data['tagId'])

        return json.dumps(post_tags.__dict__)

def create_post_tag(new_post_tag):
    """Creates a new postTag"""
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
		INSERT INTO post_tag
			( post_id, tag_id )
		VALUES
			(?, ?);
		""", (new_post_tag['post_id'], new_post_tag['tag_id']) )
        id = db_cursor.lastrowid
        new_post_tag['id'] = id
    return json.dumps(new_post_tag)

def delete_post_tag(post_tag_id):
    """Gets all posts"""
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
            DELETE FROM post_tag
            WHERE id = ?
            """, (post_tag_id, ) )

        rows_needed = db_cursor.rowcount

        if rows_needed == 0:
            return False
        else:
            return True

def get_post_tags_by_post_id(post_id):
    """Get PostTag by Post_id"""
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id,
            t.id tag_id,
            t.label
        FROM post_tags pt
        JOIN tags t ON t.id = pt.tag_id
        WHERE pt.post_id = ?
               """,(post_id, ))

        post_tags = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post_tag = PostTag(row['id'], row['post_id'], row['tag_id'])
            tag = Tag(row['tag_id'], row['label'])
            post_tag.tags = tag.__dict__
            post_tags.append(post_tag.__dict__)

    return json.dumps(post_tags)
