import sqlite3
import json
from models import Tag

def get_all_tags():
    """Gets all tags"""
    with sqlite3.connect("./rare.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                t.id,
                t.lable
            FROM tag t
            """)

        tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            tag = Tag(row['id'], row['label'])

            tags.append(tag.__dict__)

    return json.dumps(tags)

def get_single_tag(id):
    """Gets single tag"""
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
          SELECT
              t.id,
              t.lable
          FROM Tag t
          WHERE t.id = ?
          """, ( id, ))

        data = db_cursor.fetchone()

        tag = Tag(data['id'], data['lable'])

    return json.dumps(tag.__dict__)

def create_tag(new_tag):
    """Creates a new tag"""
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tag
            ( label )
        VALUES
            ( ? );
        """, (new_tag['lable'],))

        id = db_cursor.lastrowid

        new_tag['id'] = id

    return json.dumps(new_tag)

def delete_tag(id):
    """Deletes a tag"""
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM tag
        WHERE id = ?
        """, (id, ))
