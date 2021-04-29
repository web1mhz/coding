from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# db 연결 확인
print(db)

# insert data in db
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 다중 입력
for i in range(0, 10):
    doc = {'name': 'bobby'+ str(i), 'age': i}
    db.users.insert_one(doc)

# 전체 검색
all_ages = list(db.users.find({},{'_id':False}))
print(all_ages)

# 1개 검색
one_search = list(db.users.find({'age':21},{'_id':False}))
print(one_search)

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})
