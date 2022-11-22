import os
import csv
from post import Post

file_path = "C:\\Users\Hwang\\Desktop\\python-web-basic-projects\\mini-blog\\data.csv"
post_list = []

# 掲示文をロード
if os.path.exists(file_path):
    print("Loading Posts...")
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)
    for data in reader:
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
    f.close()
else:
    f = open(file_path, "w", encoding="utf8", newline="")
    f.close()

# 掲示文を書く
def write_post():
    print("\n\n==== Write Post ====")
    title = input("Please enter a title\n>>>>")
    content = input("Please enter the contents\n>>>>")
    # 最後の文番号の + 1
    if not post_list:
        id = 1
    else:
        id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print("*** Your post has been registered ***")


# 掲示文 list
def list_post():
    if not post_list:
        print("■■■■■■■■■■")
        print("Post does not exist")
        print("■■■■■■■■■■")
        return

    print("\n\n==== Post List ====")
    id_list = []
    for post in post_list:
        print("Id : ", post.get_id())
        print("Title : ", post.get_title())
        print("View Count : ", post.get_view_count())
        print("")
        id_list.append(post.get_id())

    while True:
        print("Q) Please Enter a Post Id (Enter -1 to return to the Menu)")
        try:
            id = int(input(">>>>"))
            if id in id_list:
                detail_post(id)
                break
            elif id == -1:
                break
            else:
                print("■■■■■■■■■■■■")
                print("This post doesn't exist")
                print("■■■■■■■■■■■■")
        except ValueError:
            print("Please enter a number")


# 掲示文の詳細を確認
def detail_post(id):
    print("\n\n==== Post Detail ====")
    for post in post_list:
        if post.get_id() == id:
            post.add_view_count()
            target = post
            print("Id : ", post.get_id())
            print("Title : ", post.get_title())
            print("=====================")
            print("[Content]\n")
            print(post.get_content())
            print("=====================")
            print("View Count : ", post.get_view_count())

    while True:
        print("")
        print("Q) Modify: 1 Delete: 2 (Enter -1 to return to the Menu)")
        try:
            choice = int(input(">>>>"))
            if choice == 1:
                update_post(target)
                break
            elif choice == 2:
                delete_post(target)
                break
            elif choice == -1:
                break
            else:
                print("You entered the wrong number")
        except ValueError:
            print("Please enter a number")


# 掲示文を修正
def update_post(target):
    print("\n\n==== Post Update ====")
    title = input("Please enter a title\n>>>>")
    content = input("Please enter the contents\n>>>>")
    target.set_post(target.id, title, content, target.view_count)
    print("*** Your post has been updated ***")


# 掲示文を削除
def delete_post(target):
    post_list.remove(target)
    print("*** Your post has been deleted ***")


# 掲示文を保存
def save():
    f = open(file_path, "w", encoding="utf8", newline="")
    writer = csv.writer(f)
    for post in post_list:
        row = [
            post.get_id(),
            post.get_title(),
            post.get_content(),
            post.get_view_count(),
        ]
        writer.writerow(row)
    f.close()
    print("*** Saved successfully ***")


# メニューを出力
while True:
    print("\n\n==== Main Menu ====")
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
            save()
            break
