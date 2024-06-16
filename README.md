データベース挿入方法

1. 新しいターミナルで
    mysql -u root -p
    その後パスワードを入力

2. create database 8Apra
    この後、query okとでたら
    show databases
    を入力してみて、"8A pra"が作成されてるか確認

3. 別のターミナルで、lsをして、backend, frontend, dubm.sql, README.mdの4つがでてる場所まで戻る
    必要に応じて、cd ..をして戻る

4. mysql -u root -p mydatabase < dump.sql
    おそらくパスワードを求められるので入力


5. 先ほどのmysqlを開いてるターミナルで、
    use 8Apra
    show tables from 8Apra
    をして、8Apraの中にUser, Bookmark, Restaurantテーブルが入ってることを確認

    select * from User
    で実際に5個くらいデータが入ってることを確認
    
