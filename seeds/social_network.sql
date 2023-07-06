-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email_address text,
  username text
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  post_title text,
  post_content text,
  number_of_views int,
-- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (email_address, username) VALUES ('email_1@email.com', 'user1');
INSERT INTO users (email_address, username) VALUES ('email_2@email.com', 'user2');
INSERT INTO users (email_address, username) VALUES ('email_3@email.com', 'user3');
INSERT INTO users (email_address, username) VALUES ('email_4@email.com', 'user4');
INSERT INTO users (email_address, username) VALUES ('email_5@email.com', 'user5');


INSERT INTO posts (post_title, post_content, number_of_views, user_id) VALUES ('title1', 'contents1', 1, 1);
INSERT INTO posts (post_title, post_content, number_of_views, user_id) VALUES ('title2', 'contents2', 2, 1);
INSERT INTO posts (post_title, post_content, number_of_views, user_id) VALUES ('title3', 'contents3', 3, 2);
INSERT INTO posts (post_title, post_content, number_of_views, user_id) VALUES ('title4', 'contents4', 4, 2);
INSERT INTO posts (post_title, post_content, number_of_views, user_id) VALUES ('title5', 'contents5', 5, 3);
INSERT INTO posts (post_title, post_content, number_of_views, user_id) VALUES ('title6', 'contents6', 6, 3);
INSERT INTO posts (post_title, post_content, number_of_views, user_id) VALUES ('title7', 'contents7', 7, 4);
INSERT INTO posts (post_title, post_content, number_of_views, user_id) VALUES ('title8', 'contents8', 8, 4);
INSERT INTO posts (post_title, post_content, number_of_views, user_id) VALUES ('title9', 'contents9', 9, 5);
INSERT INTO posts (post_title, post_content, number_of_views, user_id) VALUES ('title10', 'contents10', 10, 5);



