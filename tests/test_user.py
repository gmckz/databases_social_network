from lib.user import *

"""
User constructs with id email address and username
"""
def test_user_constructs():
    user = User(1, 'email_1@email.com', 'user1')
    assert user.id == 1
    assert user.email_address == 'email_1@email.com'
    assert user.username == 'user1'

"""
User formats nicely
"""
def test_user_formats_nicely():
    user = User(1, 'email_1@email.com', 'user1')
    assert str(user) == '1 - email_1@email.com - user1'

"""
Identical users assert as equal
"""
def test_identical_users_are_equal():
    user1 = User(1, 'email_1@email.com', 'user1')
    user2 = User(1, 'email_1@email.com', 'user1')
    assert user1 == user2
