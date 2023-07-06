from lib.post import *

class PostRepository:
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row['id'], row['post_title'], row['post_content'], row['number_of_views'], row['user_id'])
            posts.append(item)
        return posts
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM posts WHERE id = %s', [id])
        row = rows[0]
        post = Post(row['id'], row['post_title'], row['post_content'], row['number_of_views'], row['user_id'])
        return post

    def create(self, post):
        self._connection.execute('INSERT INTO posts (post_title, post_content, number_of_views, user_id) VALUES(%s,%s, %s, %s)', [post.post_title, post.post_content, post.number_of_views, post.user_id])
        return None
    
    def delete(self, id):
        self._connection.execute('DELETE FROM posts WHERE id = %s', [id])
        return None