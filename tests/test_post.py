from lib.post import *

"""
Post constructs with id, post title, post contents, number of views and user id
"""
def test_post_constructs():
    post = Post(1, "title1", "contents1", 1, 1)
    assert post.id == 1
    assert post.post_title == "title1"
    assert post.post_content == "contents1"
    assert post.number_of_views == 1
    assert post.user_id == 1


"""
Post formats nicely
"""
def test_post_formats_nicely():
    post = Post(1, "title1", "contents1", 1, 1)
    assert str(post) == '1 - title1 - contents1 - 1 - 1'

"""
Identical posts assert as equal
"""
def test_identical_posts_are_equal():
    post1 = Post(1, "title1", "contents1", 1, 1)
    post2 = Post(1, "title1", "contents1", 1, 1)
    assert post1 == post2
