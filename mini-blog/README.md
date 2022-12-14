# ベーシック掲示板 (Console 操作)
**製作目的** : CRUD tutorial(+基礎文法学習)  
**デモンストレーション** : [Youtubeリンク](https://www.youtube.com/watch?v=tlgdM5Df-oY&ab_channel=%E9%BB%84%E4%B8%9E%E6%B6%93)

## **基本設計** : コンソール画面で基本的な掲示板を操作
| C            | R                  | U            | D            | その他         |
| ------------ | ------------------ | ------------ | ------------ | -------------- |
| 掲示文を書く | 掲示文リストを確認 | 掲示文を修正 | 掲示文を削除 | 掲示文をロード |
|              | 掲示文の詳細を確認 |              |              | メニューを出力 |
|              |                    |              |              | 掲示文を保存   |
---
## **詳細設計**
### **機能**  
### <u>Create</u>
- write_post() : 掲示文を書く
  - ![](./mini_blog/img/write.jpg)
  - Post インスタンスの生成
  - Post list に保存

### <u>Read</u>
- list_post() : 掲示文リストを確認
  - ![](./mini_blog/img/list.jpg)  
  - 出力
    - Post list を出力
  - 入力
    - 存在する文番号　⇒　詳細を見る
    - 存在しない文番号　⇒　Post list を出力
      - 文字を入力した場合、Exception 発生
    - 「-1」入力　⇒　メニューに戻る

- detail_post() : 掲示文の詳細を確認
  - ![](./mini_blog/img/detail.jpg) 
  - ユーザーが入力した番号の Post list から Post を探す
  - 該当する掲示文のビュー数の増加、詳細の出力
  - 修正、削除機能を出力
    - 該当 Post インスタンスを修正、削除メソッドに引数として渡す

### <u>Update</u>
- update_post() : 掲示文を修正
  - ![](./mini_blog/img/update.jpg) 
  - ユーザーが新しいタイトル、本文を入力
  - set_post メソッドで Post インスタンスを修正

### <u>Delete</u>
- delete_post() : 掲示文を削除
  - ![](./mini_blog/img/delete.jpg) 
  - post_list から該当 Post インスタンスを削除

### <u>その他</u>
- 掲示文をロード
  - ![](./mini_blog/img/loding.jpg) 
  - data.csvファイルにある掲示文データをロードする
    - データ.csvが存在する場合、ロード
        - データ1行ごとに Post インスタンスを作成
        - Post インスタンスを list に保存
    - データ.csvが存在しない場合、ファイルを生成
- メニューを出力
  - ![](./mini_blog/img/main.jpg)
  - 4、5入力(存在しない項目)入力時、にメニューを再出力
  - 文字入力時に Exception 発生
- save() : 掲示文を保存
  - ![](./mini_blog/img/save.jpg) 
  - post_list に保存された内容をdata.csvファイルに保存
---
### **Class**  
- Post (掲示文)
  - プロパティ
    - param id : 文番号
    - param title : タイトル
    - param content : 本文
    - param view_count : ビュー(アクセス数)
  - メソッド
      - set_post : プロパティ修正
      - get_{} : プロパティ取得
        - id
        - title
        - content
        - view_count
      - add_view_count : ビューの増加

