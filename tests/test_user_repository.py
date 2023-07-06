from lib.user_repository import *
from lib.user import *
"""
When we call #all on UserRepository
we get a list of all users
"""
def test_all_returns_list_of_users(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = UserRepository(db_connection)
    users = repo.all()
    assert users == [
        User(1, "email_1@email.com", "user1"),
        User(2, "email_2@email.com", "user2"),
        User(3, "email_3@email.com", "user3"),
        User(4, "email_4@email.com", "user4"),
        User(5, "email_5@email.com", "user5"),
    ]

"""
When we call #find on UserRepository with a given id
we get the corresponding user
"""
def test_find_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = UserRepository(db_connection)
    user = repo.find(2)
    assert user == User(2, "email_2@email.com", "user2")

"""
When we call #create on UserRepository given a user
new user appears in #all
"""
def test_create_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = UserRepository(db_connection)
    new_user = User(None, "email_6@email.com", "user6")
    repo.create(new_user)
    users = repo.all()
    assert users == [
        User(1, "email_1@email.com", "user1"),
        User(2, "email_2@email.com", "user2"),
        User(3, "email_3@email.com", "user3"),
        User(4, "email_4@email.com", "user4"),
        User(5, "email_5@email.com", "user5"),
        User(6, "email_6@email.com", "user6"),
    ]

"""
When we call #delete with a given id
that user is removed from all
"""
def test_delete_user(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repo = UserRepository(db_connection)
    repo.delete(5)
    users = repo.all()
    assert users == [
        User(1, "email_1@email.com", "user1"),
        User(2, "email_2@email.com", "user2"),
        User(3, "email_3@email.com", "user3"),
        User(4, "email_4@email.com", "user4"),
    ]