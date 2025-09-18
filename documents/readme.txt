gemine_ai_key=   AIzaSyBwyiW7ZBOshQzTd3mjRv8fTenqunNkqAo


https://www.youtube.com/watch?v=tB3kwu2E0GM&list=PL49YuNfb-9OfL4EUPcFhPej_GUJFQO9xe



開新專案
python manage.py startapp demo


# 1. 建立/更新資料庫（會建立 auth_user 等內建表）
python manage.py migrate

# 2. 再建立管理員帳號
python manage.py createsuperuser


然後啟動伺服器：

python manage.py runserver

啟動 sql
sqlite3 db.sqlite3

同步資料庫
python manage.py makemigrations
python manage.py migrate






從 Cursor 推到 GitHub」的簡單指令清單


git add .


（把所有修改、新增、刪除的檔案加入暫存）


git commit -m "這裡寫你的修改說明"


範例：git commit -m "修正登入錯誤 & 新增使用者設定頁面"


git push origin main

之後只要打：
git push
