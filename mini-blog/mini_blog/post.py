class Post:
    """
    掲示文 Class
    param id : 文番号
    param title : タイトル
    param content : 本文
    param view_count : ビュー(アクセス数)
    """

    def __init__(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_view_count(self):
        return self.view_count

    def set_post(self, id, title, content, view_count):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count

    def add_view_count(self):
        self.view_count += 1


# テスト
# print(__name__)
# if __name__ == "__main__":
#     post = Post(1, "test_title", "test_content", 0)
#     post.set_post(1, "test_title2", "test_content2", 0)
#     post.add_view_count()
#     print(f"{post.get_id()} {post.get_title()} {post.get_content()} {post.get_view_count()}")
