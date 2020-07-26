from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

movies = list(db.movies.find({}))


wallE_star = 0
#list로 만들어서 movie에 넣어줘

for movie in movies:
    if movie['title'] == '월-E':
        wallE_star = movie['star']


for movie in movies:
    if movie['star'] == wallE_star:
        db.movies.update_one({'title':movie['title']}, {'$set':{'star':0}})