import sqlite3
import json
from models import PostTag

def get_all_postTags():
    with sqlite3.connect("./rare.db") as conn:
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

        postTags = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            postTag = PostTag(row['id'], row['post_id'], row['tag_id'])
            postTags.append(postTag.__dict__)

    return json.dumps(postTags)


def get_single_postTag(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()


        db_cursor.execute("""
        SELECT
            pt.id,
            pt.postId,
            pt.tagId
        FROM Posttag pt
         WHERE pt.id = ?
        """, ( id, ))


        data = db_cursor.fetchone()

        postTags = PostTag(data['id'], data['postId'], data['tagId'])

        return json.dumps(postTags.__dict__)

def create_postTag(new_postTag):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
		INSERT INTO post_tag
			( post_id, tag_id )
		VALUES
			(?, ?);
		""", (new_postTag['post_id'], new_postTag['tag_id']) )
        id = db_cursor.lastrowid
        new_postTag['id'] = id
    return json.dumps(new_postTag)

def delete_postTag(postTag_Id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
            DELETE FROM post_tag
            WHERE id = ?
            """, (postTag_Id, ) )

        rows_needed = db_cursor.rowcount

        if rows_needed == 0:
            return False
        else:
            return True
