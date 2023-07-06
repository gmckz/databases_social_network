class Post:

    def __init__(self, id, post_title, post_content, number_of_views, user_id):
        self.id = id
        self.post_title = post_title
        self.post_content = post_content
        self.number_of_views = number_of_views
        self.user_id = user_id

    def __repr__(self):
        return f"{self.id} - {self.post_title} - {self.post_content} - {self.number_of_views} - {self.user_id}"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__