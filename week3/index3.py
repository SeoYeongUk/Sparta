from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


# find({}) : 모든 데이터 가져오기
# find({'age':40}) : age가 40인 데이터만 가져온다.
# all_users = list(db.users.find({'age':40},{'_id':False})) : age가 40인 데이터를 가져오는데 _id는 빼고 가져와 _id 대신 name이 들어가면 이름 빼고 가져와
# MongoDB에서 데이터 모두 보기
all_users = list(db.users.find({'age':40},{'_id':False}))

print(all_users[0])  # 0번째 결과값을 보기
print(all_users[0]['name'])  # 0번째 결과값의 'name'을 보기

for user in all_users:  # 반복문을 돌며 모든 결과값을 보기
    print(user)