from lib.post_repository import *

"""
When we call #all on PostRepository
we get a list of all posts
"""
def test_all_returns_list_of_posts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = PostRepository(db_connection)
    posts = repo.all()
    assert posts == [
        Post(1, 'title1', 'contents1', 1, 1),
        Post(2, 'title2', 'contents2', 2, 1),
        Post(3, 'title3', 'contents3', 3, 2),
        Post(4, 'title4', 'contents4', 4, 2),
        Post(5, 'title5', 'contents5', 5, 3),
        Post(6, 'title6', 'contents6', 6, 3),
        Post(7, 'title7', 'contents7', 7, 4),
        Post(8, 'title8', 'contents8', 8, 4),
        Post(9, 'title9', 'contents9', 9, 5),
        Post(10, 'title10', 'contents10', 10, 5),
    ]

"""
When we call #find on PostRepository with a given id
we get the corresponding post
"""
def test_find_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = PostRepository(db_connection)
    post = repo.find(2)
    assert post == Post(2, 'title2', 'contents2', 2, 1)

"""
When we call #create on postRepository given a post
new post appears in #all
"""
def test_create_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = PostRepository(db_connection)
    new_post = Post(None, "title11", "contents11", 11, 5)
    repo.create(new_post)
    posts = repo.all()
    assert posts == [
        Post(1, 'title1', 'contents1', 1, 1),
        Post(2, 'title2', 'contents2', 2, 1),
        Post(3, 'title3', 'contents3', 3, 2),
        Post(4, 'title4', 'contents4', 4, 2),
        Post(5, 'title5', 'contents5', 5, 3),
        Post(6, 'title6', 'contents6', 6, 3),
        Post(7, 'title7', 'contents7', 7, 4),
        Post(8, 'title8', 'contents8', 8, 4),
        Post(9, 'title9', 'contents9', 9, 5),
        Post(10, 'title10', 'contents10', 10, 5),
        Post(11, 'title11', 'contents11', 11, 5),
    ]

"""
When we call #delete with a given id
that post is removed from all
"""
def test_delete_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = PostRepository(db_connection)
    repo.delete(5)
    posts = repo.all()
    assert posts == [
        Post(1, 'title1', 'contents1', 1, 1),
        Post(2, 'title2', 'contents2', 2, 1),
        Post(3, 'title3', 'contents3', 3, 2),
        Post(4, 'title4', 'contents4', 4, 2),
        Post(6, 'title6', 'contents6', 6, 3),
        Post(7, 'title7', 'contents7', 7, 4),
        Post(8, 'title8', 'contents8', 8, 4),
        Post(9, 'title9', 'contents9', 9, 5),
        Post(10, 'title10', 'contents10', 10, 5)
    ]