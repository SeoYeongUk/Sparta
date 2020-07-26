from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기


# 오타가 많으니 이 줄을 복사해서 씁시다!
db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 19}})
data_list = db.users.find({})
for data in data_list:
    db.users.delete_one({'name': '론'})
    # user = db.users.find_one({'name': '덤블도어'},{'_id':False})
    print(data)