import sqlite3
import json
from models import Comment, Post


def get_post_comments():
    """
        gets a single posts comments
    """
    with sqlite3.connect("./db.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id
            c.author_id
            p.id post_id
            p.category category_id
            p.title title
            p.publication_date publication_date
            p.image image_url
            p.content content
        FROM Comments c
        JOIN Posts p
            ON p.id = c.post_id
        """)

        # Initialize an empty list to hold all animal representations
        comments = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

    # Create an animal instance from the current row
            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'], row['category_id'], row['title'], row['image_url'], row['content'])

        # Create a Location instance from the current row
            post = Post(row['id'], row['post_id'], row['category_id'], row['title'], row['publication_date'], row['content'], row['image_url'])
    # Add the dictionary representation of the location to the animal
            comment.post = post.__dict__
    # Add the dictionary representation of the animal to the list
            comments.append(comment.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(comments)


def create_comment(new_comment):
    """AI is creating summary for create_comment

    Args:
        new_comment ([type]): [description]
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            ( post_id, author_id, content )
        VALUES
            ( ?, ?, ? );
        """, (new_comment['postId'], new_comment['authorId'], new_comment['content']))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_comment['id'] = id

    return json.dumps(new_comment)


def delete_comment(id):
    """
            deletes comment from database
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))


def update_comment(id, new_comment):
    """
        updates selected comment
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Comments
            SET
                content = ?
        WHERE id = ?
        """, (new_comment['content'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
        # Forces 204 response by main module
    return True
