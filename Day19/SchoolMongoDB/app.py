from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError
from bson.son import SON
import subprocess

# -----------------------------------------
# CONNECT TO MONGODB
# -----------------------------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["schooldb"]

# -----------------------------------------
# PART 1 — INSERT DOCUMENTS
# -----------------------------------------

students = db.students
courses = db.courses
departments = db.departments
instructors = db.instructors
enrollments = db.enrollments

students.delete_many({})
courses.delete_many({})
departments.delete_many({})
instructors.delete_many({})
enrollments.delete_many({})

students.insert_many([
    {"student_id": 1, "name": "Aarav", "age": 21, "email": "aarav@example.com", "department_id": 10},
    {"student_id": 2, "name": "Riya", "age": 19, "email": "riya@example.com", "department_id": 11},
    {"student_id": 3, "name": "Karthik", "age": 22, "email": "karthik@example.com", "department_id": 10},
    {"student_id": 4, "name": "Neha", "age": 20, "email": "neha@example.com", "department_id": 12},
    {"student_id": 5, "name": "Vikram", "age": 23, "email": "vikram@example.com", "department_id": 11}
])

courses.insert_many([
    {"course_id": "C1", "course_name": "DB Systems", "credits": 4, "instructor_id": 501},
    {"course_id": "C2", "course_name": "OS", "credits": 3, "instructor_id": 502},
    {"course_id": "C3", "course_name": "Data Structures", "credits": 2, "instructor_id": 501},
    {"course_id": "C4", "course_name": "Networks", "credits": 4, "instructor_id": 503},
    {"course_id": "C5", "course_name": "Web Dev", "credits": 3, "instructor_id": 504}
])

departments.insert_many([
    {"department_id": 10, "name": "CSE"},
    {"department_id": 11, "name": "IT"},
    {"department_id": 12, "name": "ECE"}
])

instructors.insert_many([
    {"instructor_id": 501, "name": "Dr Mehta"},
    {"instructor_id": 502, "name": "Dr Sharma"},
    {"instructor_id": 503, "name": "Prof Reddy"},
    {"instructor_id": 504, "name": "Prof Sen"}
])

enrollments.insert_many([
    {"student_id": 1, "course_id": "C1", "grade": "A"},
    {"student_id": 1, "course_id": "C3", "grade": "A-"},
    {"student_id": 2, "course_id": "C2", "grade": "B"},
    {"student_id": 3, "course_id": "C1", "grade": "B+"},
    {"student_id": 4, "course_id": "C5", "grade": "A"}
])

print("\n✔ Insert Done")

# -----------------------------------------
# PART 2 — READ OPERATIONS
# -----------------------------------------

print("\nAll Students:")
for s in students.find():
    print(s)

print("\nStudents older than 20:")
for s in students.find({"age": {"$gt": 20}}):
    print(s)

print("\nFind student by email:")
print(students.find_one({"email": "riya@example.com"}))

print("\nCourses with credits > 3:")
for c in courses.find({"credits": {"$gt": 3}}):
    print(c)

print("\nStudents from department 10:")
for s in students.find({"department_id": 10}):
    print(s)

# -----------------------------------------
# PART 3 — UPDATE OPERATIONS
# -----------------------------------------

students.update_one({"student_id": 1}, {"$set": {"email": "aarav.new@example.com"}})
courses.update_many({}, {"$inc": {"credits": 1}})
courses.update_one({"course_id": "C3"}, {"$set": {"instructor_id": 600}})
departments.update_one({"department_id": 10}, {"$set": {"name": "Computer Science"}})

print("\n✔ Updates Done")

# -----------------------------------------
# PART 4 — DELETE OPERATIONS
# -----------------------------------------

students.delete_one({"student_id": 5})
courses.delete_many({"credits": 0})
enrollments.delete_many({"student_id": 1})

print("\n✔ Deletions Done")

# -----------------------------------------
# PART 5 — ADVANCED OPERATORS
# -----------------------------------------

print("\nStudents aged 18–25:")
for x in students.find({"age": {"$gt": 18, "$lt": 25}}):
    print(x)

print("\nCourses with credits 2, 3, 4:")
for x in courses.find({"credits": {"$in": [2, 3, 4]}}):
    print(x)

print("\nStudents NOT in department 11:")
for x in students.find({"department_id": {"$ne": 11}}):
    print(x)

# -----------------------------------------
# PART 6 — PROJECTION
# -----------------------------------------

print("\nOnly student name and email:")
for x in students.find({}, {"name": 1, "email": 1, "_id": 0}):
    print(x)

print("\nHide student_id:")
for x in students.find({}, {"student_id": 0}):
    print(x)

print("\nShow only course name:")
for x in courses.find({}, {"course_name": 1, "_id": 0}):
    print(x)

# -----------------------------------------
# PART 7 — AGGREGATIONS
# -----------------------------------------

print("\nCount students per department:")
pipeline = [
    {"$group": {"_id": "$department_id", "count": {"$sum": 1}}}
]
print(list(students.aggregate(pipeline)))

print("\nEnrollments per course:")
pipeline = [
    {"$group": {"_id": "$course_id", "count": {"$sum": 1}}}
]
print(list(enrollments.aggregate(pipeline)))

print("\nAverage student age:")
pipeline = [
    {"$group": {"_id": None, "avg_age": {"$avg": "$age"}}}
]
print(list(students.aggregate(pipeline)))

print("\nCourse with max enrollments:")
pipeline = [
    {"$group": {"_id": "$course_id", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 1}
]
print(list(enrollments.aggregate(pipeline)))

# -----------------------------------------
# PART 8 — INDEXING
# -----------------------------------------

students.create_index([("email", ASCENDING)])
courses.create_index([("course_id", ASCENDING)])
students.create_index([("department_id", ASCENDING)])

print("\nIndexes created:")
print(students.index_information())

# -----------------------------------------
# PART 9 — VALIDATION
# -----------------------------------------

db.command({
    "collMod": "students",
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "email", "age"],
            "properties": {
                "name": {"bsonType": "string"},
                "email": {"bsonType": "string", "pattern": "^.+@.+\\..+$"},
                "age": {"bsonType": "int", "minimum": 16, "maximum": 60}
            }
        }
    }
})

print("\n✔ Validation schema applied")

# -----------------------------------------
# PART 10 — TRANSACTIONS
# -----------------------------------------
session = client.start_session()
session.start_transaction()

try:
    students.insert_one({"student_id": 999, "name": "TX Test", "age": 22, "email": "txtest@example.com"}, session=session)
    enrollments.insert_one({"student_id": 999, "course_id": "C1"}, session=session)
    courses.update_one({"course_id": "C1"}, {"$inc": {"enrollment_count": 1}}, session=session)

    session.commit_transaction()
    print("\n✔ Transaction SUCCESS")
except Exception as e:
    print("Transaction failed:", e)
    session.abort_transaction()

# -----------------------------------------
# PART 11 — BACKUP & RESTORE (SHELL COMMANDS)
# -----------------------------------------

print("\nRunning mongodump...")
subprocess.run(["mongodump", "-d", "schooldb", "-o", "backup/"], shell=True)

print("To restore:")
print("mongorestore backup/")

# -----------------------------------------
# PART 12 — REAL WORLD CASE STUDY (Shopping DB)
# -----------------------------------------

shop = client["shopdb"]
shop.users.insert_many([
    {"user_id": 1, "name": "Aditi"},
    {"user_id": 2, "name": "Rahul"}
])
shop.products.insert_many([
    {"product_id": 101, "name": "Laptop", "price": 60000},
    {"product_id": 102, "name": "Phone", "price": 30000}
])
shop.orders.insert_many([
    {"order_id": 1, "user_id": 1, "product_id": 101},
    {"order_id": 2, "user_id": 1, "product_id": 102},
    {"order_id": 3, "user_id": 2, "product_id": 101}
])

print("\nUser 1 orders:")
pipeline = [
    {"$match": {"user_id": 1}},
    {"$lookup": {
        "from": "products",
        "localField": "product_id",
        "foreignField": "product_id",
        "as": "product_info"
    }}
]
print(list(shop.orders.aggregate(pipeline)))

print("\nTop selling product:")
pipeline = [
    {"$group": {"_id": "$product_id", "sold": {"$sum": 1}}},
    {"$sort": {"sold": -1}},
    {"$limit": 1}
]
print(list(shop.orders.aggregate(pipeline)))

print("\nUsers with most orders:")
pipeline = [
    {"$group": {"_id": "$user_id", "orders": {"$sum": 1}}},
    {"$sort": {"orders": -1}}
]
print(list(shop.orders.aggregate(pipeline)))

print("\n\n✔ ALL EXERCISES FINISHED SUCCESSFULLY ✔\n")