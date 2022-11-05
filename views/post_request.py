"""post requests"""

import sqlite3
import json
from models import Post


def get_all_posts():
    """Gets all posts"""
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM posts p
        """)

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'],
                        row['publication_date'], row['image_url'], row['content'], row['approved'])

            posts.append(post.__dict__)

    return json.dumps(posts)


def create_post(new_post):
    """create a post"""
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Posts
            (user_id, category_id, title, publication_date, image_url, content, approved)
        VALUES
            ( ?, ?, ?, ?, ?, ?, ?);
        """, (new_post['user_id'],
              new_post['category_id'],
              new_post['title'],
              new_post['publication_date'],
              new_post['image_url'],
              new_post['content'],
              new_post['approved'], ))

        post_id = db_cursor.lastrowid

        new_post['id'] = post_id

    return json.dumps(new_post)


def update_post(id, new_post):
    """Updated a post"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Posts
            SET
                category_id = ?,
                title = ?,
                publication_date = ?,
                image_url = ?,
                content = ?,
                approved = ?
        WHERE id = ?
        """, (new_post['category_id'], new_post['title'],
              new_post['publication_date'], new_post['image_url'],
              new_post['content'], new_post['approved'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True


def delete_post(id):
    """Delete a post"""
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM posts
        WHERE id = ?
        """, (id, ))
