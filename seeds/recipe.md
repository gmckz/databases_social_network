# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

*In this template, we'll use an example table `students`*

```
# EXAMPLE

Table: students

Columns:
id | name | cohort_name
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE students RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO students (name, cohort_name) VALUES ('David', 'April 2022');
INSERT INTO students (name, cohort_name) VALUES ('Anna', 'May 2022');
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)
class User


# Repository class
# (in lib/student_repository.py)
class UserRepository

# Model class
# (in lib/student.py)
class Post


# Repository class
# (in lib/student_repository.py)
class PostRepository
```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)

class User:
    def __init__(self):
        self.id = 0
        self.email_address = ""
        self.username = ""

        # Replace the attributes by your own columns.

class Post:
    def __init__(self):
        self.id = 0
        self.post_title = ""
        self.post_content = ""
        self.number_of_views = ""
# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> student = Student()
# >>> student.name = "Will"
# >>> student.cohort_name = "September Devs"
# >>> student.name
# 'Will'
# >>> student.cohort_name
# 'September Devs'

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: students

# Repository class
# (in lib/student_repository.py)

class UserRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM students;

        # Returns an array of Student objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM students WHERE id = $1;

        # Returns a single Student object.

        # Add more methods below for each operation you'd like to implement.

    def create(user)
    # Executes the SQL query:
    # INSERT INTO users (email_address, username) VALUES(%s,%s), [user.email_address, user.username]
    #returns None

    def delete(id)
    # Executes the SQL query:
    # DELETE FROM users WHERE id = %s, [id]
    #returns None

class PostRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM students;

        # Returns an array of Student objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM students WHERE id = $1;

        # Returns a single Student object.

        # Add more methods below for each operation you'd like to implement.

    def create(post)
    # Executes the SQL query:
    # INSERT INTO posts (post_title, post_content, number_of_views) VALUES(%s,%s), [post.post_title, post.post_content, post.number_of_views]
    #returns None

    def delete(id)
    # Executes the SQL query:
    # DELETE FROM posts WHERE id = %s, [id]
    #returns None
```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all users

repo = UserRepository()

users = repo.all()

len(users) # =>  2

users[0].id # =>  1
users[0].email_address # =>  'email1@email.com'
users[0].username # =>  'user1'

users[1].id # =>  2
users[1].email_address # =>  'email1@email.com'
users[1].username # =>  'user2'

# 2
# Get a single user

repo = UserRepository()

user = repo.find(1)

user.id # =>  1
user.email_address # =>  'email1@email.com'
user.username # =>  'user1'

# Add more examples for each method
#3
# Create a new user
repo = UserRepository()

repo.create(email_address, username)

#4
# Delete a user
repo = UserRepository()

repo.delete(1)


#

# 1
# Get all users

repo = postRepository()

posts = repo.all()

len(posts) # =>  2

posts[0].id # =>  1
posts[0].post_title # =>  'title1'
posts[0].post_content # =>  'content1'
posts[0].number_of_views # => '1'

posts[1].id # =>  1
posts[1].post_title # =>  'title2'
posts[1].post_content # =>  'content2'
posts[1].number_of_views # => '2'

# 2
# Get a single post

repo = postRepository()

post = repo.find(1)

posts[1].id # =>  2
posts[1].post_title # =>  'title2'
posts[1].post_content # =>  'content2'
posts[1].number_of_views # => '2'

# Add more examples for each method
#3
# Create a new post
repo = postRepository()

repo.create(post_title, post_content, number_of_views)

#4
# Delete a post
repo = postRepository()

repo.delete(1)
```

Encode this example as a test.



## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=resources%2Frepository_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->