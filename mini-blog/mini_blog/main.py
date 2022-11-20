import os
import csv
from post import Post

file_path = "./mini_blog/data.csv"
post_list = []

# 掲示文をロード
# データ.csvが存在する場合、ロード
if os.path.exists(file_path):
    print("Loading Posts...")
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
else:
    # データ.csvが存在しない場合、ファイルを生成
    f = open(file_path, "w", encoding="utf8", newline="")
    f.close()


def write_post():
    """
    掲示文を書く
    """
    print("\n\n==== Write post ====")
    title = input("Please enter a title\n>>>>")
    content = input("Please enter the contents\n>>>>")
    # 最後の文番号の + 1
    id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print("*** Your post has been registered ***")


def list_post():
    """
    掲示文 list
    """
    print(post_list)


# メニューを出力
while True:
    print("\n\n==== MINI BLOG ====")
    print("Please select a menu")
    print("1. Write post")
    print("2. List of posts")
    print("3. Exit")
    try:
        choice = int(input(">>>>"))
    except ValueError:
        print("Please enter a number")
    else:
        if choice == 1:
            write_post()
        elif choice == 2:
            list_post()
        elif choice == 3:
            print("Exit")
            break
