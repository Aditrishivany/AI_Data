# Project 1: Student Record Viewer using Flask and MySQL
# This project displays student list from database and shows student details when clicked
# Concepts used: Flask routing, MySQL connection, Jinja template renderingfrom flask import Flask, render_template_string
# import mysql.connector

# app = Flask(__name__)

# # MySQL Connection
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # Home - Show Student List
# @app.route("/")
# def home():
#     cursor.execute("SELECT * FROM students")
#     students = cursor.fetchall()

#     html = """
#     <h2>Student List</h2>
#     <ul>
#     {% for s in students %}
#         <li>
#             <a href="/student/{{s.id}}">
#                 {{s.name}}
#             </a>
#         </li>
#     {% endfor %}
#     </ul>
#     """

#     return render_template_string(html, students=students)

# # Student Details Page
# @app.route("/student/<int:id>")
# def student_detail(id):
#     cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
#     student = cursor.fetchone()

#     html = """
#     <h2>Student Details</h2>
#     <p>Name: {{student.name}}</p>
#     <p>Age: {{student.age}}</p>
#     <p>Course: {{student.course}}</p>

#     <a href="/">Back</a>
#     """

#     return render_template_string(html, student=student)

# if __name__ == "__main__":
#     app.run(debug=True)

#project-2:The Simple To-Do List project is a basic web application built using Flask and MySQL.
# It allows users to add, view, and delete daily tasks easily.
# This project demonstrates basic CRUD operations and fundamental web development concepts.
# from flask import Flask, render_template_string, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME / TODO LIST =====
# @app.route("/", methods=["GET", "POST"])
# def todo_home():

#     # ADD TASK
#     if request.method == "POST":
#         title = request.form["title"]

#         cursor.execute(
#             "INSERT INTO todo (title, status) VALUES (%s, %s)",
#             (title, "Pending")
#         )
#         conn.commit()

#         return redirect("/")

#     # SHOW TASKS
#     cursor.execute("SELECT * FROM todo")
#     tasks = cursor.fetchall()

#     html = """
#     <h2>Simple To Do List</h2>

#     <form method="POST">
#         <input name="title" placeholder="Enter Task" required>
#         <button>Add Task</button>
#     </form>

#     <hr>

#     {% for t in tasks %}
#         <p>
#             {{t.title}} ({{t.status}})
#             <a href="/delete/{{t.id}}">Delete</a>
#         </p>
#     {% endfor %}
#     """

#     return render_template_string(html, tasks=tasks)

# # ===== DELETE TASK =====
# @app.route("/delete/<int:id>")
# def delete_task(id):

#     cursor.execute("DELETE FROM todo WHERE id=%s", (id,))
#     conn.commit()

#     return redirect("/")


# if __name__ == "__main__":
#     app.run(debug=True)

#project 3:The Contact List App is a simple web application built using Flask and MySQL.
# It allows users to add new contacts, view the contact list, and see detailed information for each contact.
# This project demonstrates database insertion, data retrieval, and dynamic page rendering using Flask.
# from flask import Flask, render_template_string, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - ADD + SHOW CONTACTS =====
# @app.route("/", methods=["GET", "POST"])
# def contact_home():

#     # ADD CONTACT
#     if request.method == "POST":
#         name = request.form["name"]
#         phone = request.form["phone"]
#         email = request.form["email"]

#         cursor.execute(
#             "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)",
#             (name, phone, email)
#         )
#         conn.commit()

#         return redirect("/")

#     # SHOW CONTACT LIST
#     cursor.execute("SELECT * FROM contacts")
#     contacts = cursor.fetchall()

#     html = """
#     <h2>Contact List App</h2>

#     <h3>Add Contact</h3>
#     <form method="POST">
#         <input name="name" placeholder="Name" required><br><br>
#         <input name="phone" placeholder="Phone" required><br><br>
#         <input name="email" placeholder="Email" required><br><br>
#         <button>Add Contact</button>
#     </form>

#     <hr>

#     <h3>Contact List</h3>
#     <ul>
#     {% for c in contacts %}
#         <li>
#             <a href="/contact/{{c.id}}">
#                 {{c.name}}
#             </a>
#         </li>
#     {% endfor %}
#     </ul>
#     """

#     return render_template_string(html, contacts=contacts)

# # ===== CONTACT DETAILS PAGE =====
# @app.route("/contact/<int:id>")
# def contact_detail(id):

#     cursor.execute("SELECT * FROM contacts WHERE id=%s", (id,))
#     contact = cursor.fetchone()

#     html = """
#     <h2>Contact Details</h2>

#     <p><b>Name:</b> {{contact.name}}</p>
#     <p><b>Phone:</b> {{contact.phone}}</p>
#     <p><b>Email:</b> {{contact.email}}</p>

#     <a href="/">Back to Contact List</a>
#     """

#     return render_template_string(html, contact=contact)


# if __name__ == "__main__":
#     app.run(debug=True)

#project 4:his project shows a list of products from the database on the home page.
# Clicking a product shows its full details on a separate page.
# It demonstrates template loops, database SELECT queries, and dynamic HTML rendering using Flask

# from flask import Flask, render_template_string
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - PRODUCT LIST =====
# @app.route("/")
# def product_list():
#     cursor.execute("SELECT * FROM products")
#     products = cursor.fetchall()

#     html = """
#     <h2>Product List</h2>
#     <ul>
#     {% for p in products %}
#         <li>
#             <a href="/product/{{p.id}}">
#                 {{p.name}} - ${{p.price}}
#             </a>
#         </li>
#     {% endfor %}
#     </ul>
#     """
#     return render_template_string(html, products=products)

# # ===== PRODUCT DETAIL PAGE =====
# @app.route("/product/<int:id>")
# def product_detail(id):
#     cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
#     product = cursor.fetchone()

#     html = """
#     <h2>Product Details</h2>
#     <p><b>Name:</b> {{product.name}}</p>
#     <p><b>Price:</b> ${{product.price}}</p>
#     <p><b>Description:</b> {{product.description}}</p>

#     <a href="/">Back to Product List</a>
#     """
#     return render_template_string(html, product=product)

# if __name__ == "__main__":
#     app.run(debug=True)

#project 5:This project displays a list of blogs from the database on the home page.
# Clicking a blog shows its full content on a separate page.
# It demonstrates dynamic templates, database SELECT queries, and page rendering using Flask.


# from flask import Flask, render_template_string
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - BLOG LIST =====
# @app.route("/")
# def blog_list():
#     cursor.execute("SELECT * FROM blogs")
#     blogs = cursor.fetchall()

#     html = """
#     <h2>Blog List</h2>
#     <ul>
#     {% for b in blogs %}
#         <li>
#             <a href="/blog/{{b.id}}">
#                 {{b.title}}
#             </a>
#         </li>
#     {% endfor %}
#     </ul>
#     """
#     return render_template_string(html, blogs=blogs)

# # ===== BLOG DETAILS PAGE =====
# @app.route("/blog/<int:id>")
# def blog_detail(id):
#     cursor.execute("SELECT * FROM blogs WHERE id=%s", (id,))
#     blog = cursor.fetchone()

#     html = """
#     <h2>{{blog.title}}</h2>
#     <p>{{blog.content}}</p>

#     <a href="/">Back to Blog List</a>
#     """
#     return render_template_string(html, blog=blog)

# if __name__ == "__main__":
#     app.run(debug=True)


#project 6:This project displays all employees from the database and allows filtering by department.
# Users can type a department name to see only relevant employees.
# Flask handles requests, MySQL fetches data using SELECT queries, and HTML is rendered dynamically.


# from flask import Flask, render_template_string, request
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - EMPLOYEE LIST =====
# @app.route("/", methods=["GET"])
# def employee_list():
#     department = request.args.get("department")

#     if department:
#         cursor.execute("SELECT * FROM employees WHERE department=%s", (department,))
#     else:
#         cursor.execute("SELECT * FROM employees")
    
#     employees = cursor.fetchall()

#     html = """
#     <h2>Employee Directory</h2>

#     <form method="GET">
#         <input name="department" placeholder="Filter by department">
#         <button>Filter</button>
#     </form>

#     <hr>

#     <ul>
#     {% for e in employees %}
#         <li>{{e.name}} - {{e.department}} - {{e.email}}</li>
#     {% endfor %}
#     </ul>
#     """
#     return render_template_string(html, employees=employees)

# if __name__=="__main__":
#     app.run(debug=True)
#project-7: This project displays a random quote from the database each time the page is loaded.
# It fetches all quotes, selects one randomly, and shows it on the homepage.
# Flask handles routing, MySQL stores quotes, and HTML is dynamically rendered.


# from flask import Flask, render_template_string
# import mysql.connector
# import random

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - RANDOM QUOTE =====
# @app.route("/")
# def quote_of_the_day():
#     cursor.execute("SELECT * FROM quotes")
#     quotes = cursor.fetchall()
#     quote = random.choice(quotes) if quotes else None

#     html = """
#     <h2>Quote of the Day</h2>

#     {% if quote %}
#         <p>"{{quote.quote}}"</p>
#         <p><b>- {{quote.author}}</b></p>
#     {% else %}
#         <p>No quotes available.</p>
#     {% endif %}
#     """
#     return render_template_string(html, quote=quote)

# if __name__=="__main__":
#     app.run(debug=True)

#project-8:This project lets users add, edit, delete, and mark tasks as complete in a To-Do list.
# Flask handles routing and forms, while MySQL stores all tasks and their status.
# Dynamic HTML is rendered for all operations, implementing full CRUD functionality.

# from flask import Flask, render_template_string, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - SHOW + ADD TASK =====
# @app.route("/", methods=["GET", "POST"])
# def todo_home():
#     if request.method == "POST":
#         title = request.form["title"]
#         cursor.execute("INSERT INTO todo (title, status) VALUES (%s, %s)", (title, "Pending"))
#         conn.commit()
#         return redirect("/")

#     cursor.execute("SELECT * FROM todo")
#     tasks = cursor.fetchall()

#     html = """
#     <h2>To-Do List</h2>

#     <form method="POST">
#         <input name="title" placeholder="Enter Task" required>
#         <button>Add Task</button>
#     </form>

#     <hr>

#     {% for t in tasks %}
#         <p>
#             {{t.title}} ({{t.status}})
#             <a href="/edit/{{t.id}}">Edit</a>
#             <a href="/complete/{{t.id}}">Complete</a>
#             <a href="/delete/{{t.id}}">Delete</a>
#         </p>
#     {% endfor %}
#     """
#     return render_template_string(html, tasks=tasks)

# # ===== EDIT TASK =====
# @app.route("/edit/<int:id>", methods=["GET","POST"])
# def edit_task(id):
#     cursor.execute("SELECT * FROM todo WHERE id=%s", (id,))
#     task = cursor.fetchone()
#     if request.method=="POST":
#         new_title = request.form["title"]
#         cursor.execute("UPDATE todo SET title=%s WHERE id=%s", (new_title, id))
#         conn.commit()
#         return redirect("/")
#     html = """
#     <h2>Edit Task</h2>
#     <form method="POST">
#         <input name="title" value="{{task.title}}" required>
#         <button>Update</button>
#     </form>
#     <a href="/">Back</a>
#     """
#     return render_template_string(html, task=task)

# # ===== MARK COMPLETE =====
# @app.route("/complete/<int:id>")
# def complete_task(id):
#     cursor.execute("UPDATE todo SET status='Completed' WHERE id=%s", (id,))
#     conn.commit()
#     return redirect("/")

# # ===== DELETE TASK =====
# @app.route("/delete/<int:id>")
# def delete_task(id):
#     cursor.execute("DELETE FROM todo WHERE id=%s", (id,))
#     conn.commit()
#     return redirect("/")

# if __name__=="__main__":
#     app.run(debug=True)

#project-9:This project allows users to create, view, edit, and delete blog posts.
# Flask handles routing and forms, while MySQL stores all blog data.
# All operations use dynamic HTML rendering inside Python, implementing full CRUD functionality.
# from flask import Flask, render_template_string, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - LIST BLOGS =====
# @app.route("/")
# def blog_list():
#     cursor.execute("SELECT * FROM blogs")
#     blogs = cursor.fetchall()
#     html = """
#     <h2>Blog List</h2>
#     <a href="/create">Create New Blog</a>
#     <ul>
#     {% for b in blogs %}
#         <li>
#             <a href="/blog/{{b.id}}">{{b.title}}</a>
#             - <a href="/edit/{{b.id}}">Edit</a>
#             - <a href="/delete/{{b.id}}">Delete</a>
#         </li>
#     {% endfor %}
#     </ul>
#     """
#     return render_template_string(html, blogs=blogs)

# # ===== CREATE BLOG =====
# @app.route("/create", methods=["GET","POST"])
# def create_blog():
#     if request.method=="POST":
#         title = request.form["title"]
#         content = request.form["content"]
#         cursor.execute("INSERT INTO blogs (title, content) VALUES (%s,%s)", (title, content))
#         conn.commit()
#         return redirect("/")
#     html = """
#     <h2>Create Blog</h2>
#     <form method="POST">
#         <input name="title" placeholder="Title" required><br><br>
#         <textarea name="content" placeholder="Content" required></textarea><br><br>
#         <button>Create</button>
#     </form>
#     <a href="/">Back</a>
#     """
#     return render_template_string(html)

# # ===== VIEW BLOG DETAILS =====
# @app.route("/blog/<int:id>")
# def blog_detail(id):
#     cursor.execute("SELECT * FROM blogs WHERE id=%s",(id,))
#     blog = cursor.fetchone()
#     html = """
#     <h2>{{blog.title}}</h2>
#     <p>{{blog.content}}</p>
#     <a href="/">Back</a>
#     """
#     return render_template_string(html, blog=blog)

# # ===== EDIT BLOG =====
# @app.route("/edit/<int:id>", methods=["GET","POST"])
# def edit_blog(id):
#     cursor.execute("SELECT * FROM blogs WHERE id=%s",(id,))
#     blog = cursor.fetchone()
#     if request.method=="POST":
#         title = request.form["title"]
#         content = request.form["content"]
#         cursor.execute("UPDATE blogs SET title=%s, content=%s WHERE id=%s", (title, content, id))
#         conn.commit()
#         return redirect("/")
#     html = """
#     <h2>Edit Blog</h2>
#     <form method="POST">
#         <input name="title" value="{{blog.title}}" required><br><br>
#         <textarea name="content" required>{{blog.content}}</textarea><br><br>
#         <button>Update</button>
#     </form>
#     <a href="/">Back</a>
#     """
#     return render_template_string(html, blog=blog)

# # ===== DELETE BLOG =====
# @app.route("/delete/<int:id>")
# def delete_blog(id):
#     cursor.execute("DELETE FROM blogs WHERE id=%s",(id,))
#     conn.commit()
#     return redirect("/")

# if __name__=="__main__":
#     app.run(debug=True)

#project-10:This project allows users to add, edit, delete, and view student records in a system.
# Flask handles routing and forms, while MySQL stores all student information.
# Dynamic HTML is rendered for all CRUD operations inside Python using render_template_string().

# from flask import Flask, render_template_string, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - STUDENT LIST =====
# @app.route("/")
# def student_list():
#     cursor.execute("SELECT * FROM students")
#     students = cursor.fetchall()
#     html = """
#     <h2>Student Management System</h2>
#     <a href="/add">Add Student</a>
#     <ul>
#     {% for s in students %}
#         <li>
#             {{s.name}} - {{s.age}} - {{s.course}}
#             - <a href="/edit/{{s.id}}">Edit</a>
#             - <a href="/delete/{{s.id}}">Delete</a>
#         </li>
#     {% endfor %}
#     </ul>
#     """
#     return render_template_string(html, students=students)

# # ===== ADD STUDENT =====
# @app.route("/add", methods=["GET","POST"])
# def add_student():
#     if request.method=="POST":
#         name = request.form["name"]
#         age = request.form["age"]
#         course = request.form["course"]
#         cursor.execute("INSERT INTO students (name, age, course) VALUES (%s,%s,%s)",
#                        (name, age, course))
#         conn.commit()
#         return redirect("/")
#     html = """
#     <h2>Add Student</h2>
#     <form method="POST">
#         <input name="name" placeholder="Name" required><br><br>
#         <input name="age" placeholder="Age" required><br><br>
#         <input name="course" placeholder="Course" required><br><br>
#         <button>Add</button>
#     </form>
#     <a href="/">Back</a>
#     """
#     return render_template_string(html)

# # ===== EDIT STUDENT =====
# @app.route("/edit/<int:id>", methods=["GET","POST"])
# def edit_student(id):
#     cursor.execute("SELECT * FROM students WHERE id=%s",(id,))
#     student = cursor.fetchone()
#     if request.method=="POST":
#         name = request.form["name"]
#         age = request.form["age"]
#         course = request.form["course"]
#         cursor.execute("UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s",
#                        (name, age, course, id))
#         conn.commit()
#         return redirect("/")
#     html = """
#     <h2>Edit Student</h2>
#     <form method="POST">
#         <input name="name" value="{{student.name}}" required><br><br>
#         <input name="age" value="{{student.age}}" required><br><br>
#         <input name="course" value="{{student.course}}" required><br><br>
#         <button>Update</button>
#     </form>
#     <a href="/">Back</a>
#     """
#     return render_template_string(html, student=student)

# # ===== DELETE STUDENT =====
# @app.route("/delete/<int:id>")
# def delete_student(id):
#     cursor.execute("DELETE FROM students WHERE id=%s",(id,))
#     conn.commit()
#     return redirect("/")

# if __name__=="__main__":
#     app.run(debug=True)

#project-11:This project lets users add books, view all books, and delete any book from the list.
# Flask handles routing and form submission, while MySQL stores all book data.
# Dynamic HTML is rendered in Python to display the current list of books.


# from flask import Flask, render_template_string, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - BOOK LIST =====
# @app.route("/", methods=["GET", "POST"])
# def book_list():
#     if request.method=="POST":
#         title = request.form["title"]
#         author = request.form["author"]
#         cursor.execute("INSERT INTO books (title, author) VALUES (%s,%s)", (title, author))
#         conn.commit()
#         return redirect("/")

#     cursor.execute("SELECT * FROM books")
#     books = cursor.fetchall()

#     html = """
#     <h2>Book Management App</h2>

#     <form method="POST">
#         <input name="title" placeholder="Book Title" required><br><br>
#         <input name="author" placeholder="Author" required><br><br>
#         <button>Add Book</button>
#     </form>

#     <hr>

#     <ul>
#     {% for b in books %}
#         <li>
#             {{b.title}} - {{b.author}}
#             - <a href="/delete/{{b.id}}">Delete</a>
#         </li>
#     {% endfor %}
#     </ul>
#     """
#     return render_template_string(html, books=books)

# # ===== DELETE BOOK =====
# @app.route("/delete/<int:id>")
# def delete_book(id):
#     cursor.execute("DELETE FROM books WHERE id=%s",(id,))
#     conn.commit()
#     return redirect("/")

# if __name__=="__main__":
#     app.run(debug=True)

#PROJECT-12:

# from flask import Flask, render_template_string, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - SHOW + ADD NOTES =====
# @app.route("/", methods=["GET", "POST"])
# def notes_home():
#     if request.method=="POST":
#         title = request.form["title"]
#         content = request.form["content"]
#         cursor.execute("INSERT INTO notes (title, content) VALUES (%s,%s)", (title, content))
#         conn.commit()
#         return redirect("/")

#     cursor.execute("SELECT * FROM notes")
#     notes = cursor.fetchall()

#     html = """
#     <h2>Notes App</h2>

#     <form method="POST">
#         <input name="title" placeholder="Note Title" required><br><br>
#         <textarea name="content" placeholder="Write your note here..." required></textarea><br><br>
#         <button>Add Note</button>
#     </form>

#     <hr>

#     <ul>
#     {% for n in notes %}
#         <li>
#             <b>{{n.title}}</b>: {{n.content}}
#             - <a href="/delete/{{n.id}}">Delete</a>
#         </li>
#     {% endfor %}
#     </ul>
#     """
#     return render_template_string(html, notes=notes)

# # ===== DELETE NOTE =====
# @app.route("/delete/<int:id>")
# def delete_note(id):
#     cursor.execute("DELETE FROM notes WHERE id=%s",(id,))
#     conn.commit()
#     return redirect("/")

# if __name__=="__main__":
#     app.run(debug=True)

#PROJECT-13:

# from flask import Flask, render_template_string, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - MOVIE LIST + ADD MOVIE =====
# @app.route("/", methods=["GET","POST"])
# def movie_list():
#     if request.method=="POST":
#         title = request.form["title"]
#         director = request.form["director"]
#         year = request.form["year"]
#         cursor.execute("INSERT INTO movies (title, director, year) VALUES (%s,%s,%s)",
#                        (title, director, year))
#         conn.commit()
#         return redirect("/")

#     cursor.execute("SELECT * FROM movies")
#     movies = cursor.fetchall()

#     html = """
#     <h2>Movie List App</h2>

#     <form method="POST">
#         <input name="title" placeholder="Movie Title" required><br><br>
#         <input name="director" placeholder="Director" required><br><br>
#         <input name="year" placeholder="Year" required><br><br>
#         <button>Add Movie</button>
#     </form>

#     <hr>

#     <ul>
#     {% for m in movies %}
#         <li>
#             <a href="/movie/{{m.id}}">{{m.title}}</a> - {{m.director}} ({{m.year}})
#         </li>
#     {% endfor %}
#     </ul>
#     """
#     return render_template_string(html, movies=movies)

# # ===== MOVIE DETAILS PAGE =====
# @app.route("/movie/<int:id>")
# def movie_detail(id):
#     cursor.execute("SELECT * FROM movies WHERE id=%s",(id,))
#     movie = cursor.fetchone()
#     html = """
#     <h2>{{movie.title}}</h2>
#     <p><b>Director:</b> {{movie.director}}</p>
#     <p><b>Year:</b> {{movie.year}}</p>
#     <a href="/">Back to Movie List</a>
#     """
#     return render_template_string(html, movie=movie)

# if __name__=="__main__":
#     app.run(debug=True)

#PROJECT-14:

# from flask import Flask, render_template_string, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - SHOW + ADD PRODUCT =====
# @app.route("/", methods=["GET","POST"])
# def inventory_home():
#     if request.method=="POST":
#         product_name = request.form["product_name"]
#         quantity = request.form["quantity"]
#         cursor.execute("INSERT INTO inventory (product_name, quantity) VALUES (%s,%s)",
#                        (product_name, quantity))
#         conn.commit()
#         return redirect("/")

#     cursor.execute("SELECT * FROM inventory")
#     products = cursor.fetchall()

#     html = """
#     <h2>Inventory Manager</h2>

#     <form method="POST">
#         <input name="product_name" placeholder="Product Name" required><br><br>
#         <input name="quantity" placeholder="Quantity" required><br><br>
#         <button>Add Product</button>
#     </form>

#     <hr>

#     <ul>
#     {% for p in products %}
#         <li>
#             {{p.product_name}} - Quantity: {{p.quantity}}
#             - <a href="/update/{{p.id}}">Update</a>
#             - <a href="/delete/{{p.id}}">Delete</a>
#         </li>
#     {% endfor %}
#     </ul>
#     """
#     return render_template_string(html, products=products)

# # ===== UPDATE PRODUCT =====
# @app.route("/update/<int:id>", methods=["GET","POST"])
# def update_product(id):
#     cursor.execute("SELECT * FROM inventory WHERE id=%s",(id,))
#     product = cursor.fetchone()
#     if request.method=="POST":
#         quantity = request.form["quantity"]
#         cursor.execute("UPDATE inventory SET quantity=%s WHERE id=%s",(quantity,id))
#         conn.commit()
#         return redirect("/")
#     html = """
#     <h2>Update Product</h2>
#     <form method="POST">
#         <input name="quantity" value="{{product.quantity}}" required><br><br>
#         <button>Update</button>
#     </form>
#     <a href="/">Back</a>
#     """
#     return render_template_string(html, product=product)

# # ===== DELETE PRODUCT =====
# @app.route("/delete/<int:id>")
# def delete_product(id):
#     cursor.execute("DELETE FROM inventory WHERE id=%s",(id,))
#     conn.commit()
#     return redirect("/")

# if __name__=="__main__":
#     app.run(debug=True)


#project-15:

# from flask import Flask, render_template_string, request, redirect, session
# import mysql.connector

# app = Flask(__name__)
# app.secret_key = "mysecretkey123"  # required for sessions

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME / DASHBOARD =====
# @app.route("/")
# def dashboard():
#     if "user" in session:
#         username = session["user"]
#         html = f"""
#         <h2>Dashboard</h2>
#         <p>Welcome, {username}!</p>
#         <a href='/logout'>Logout</a>
#         """
#         return html
#     return redirect("/login")

# # ===== REGISTER =====
# @app.route("/register", methods=["GET","POST"])
# def register():
#     if request.method=="POST":
#         username = request.form["username"]
#         password = request.form["password"]
#         cursor.execute("INSERT INTO users (username, password) VALUES (%s,%s)", (username, password))
#         conn.commit()
#         return redirect("/login")
#     html = """
#     <h2>Register</h2>
#     <form method="POST">
#         <input name="username" placeholder="Username" required><br><br>
#         <input name="password" placeholder="Password" type="password" required><br><br>
#         <button>Register</button>
#     </form>
#     <a href="/login">Login</a>
#     """
#     return render_template_string(html)

# # ===== LOGIN =====
# @app.route("/login", methods=["GET","POST"])
# def login():
#     if request.method=="POST":
#         username = request.form["username"]
#         password = request.form["password"]
#         cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
#         user = cursor.fetchone()
#         if user:
#             session["user"] = username
#             return redirect("/")
#         else:
#             return "<p>Invalid credentials. <a href='/login'>Try again</a></p>"
#     html = """
#     <h2>Login</h2>
#     <form method="POST">
#         <input name="username" placeholder="Username" required><br><br>
#         <input name="password" placeholder="Password" type="password" required><br><br>
#         <button>Login</button>
#     </form>
#     <a href="/register">Register</a>
#     """
#     return render_template_string(html)

# # ===== LOGOUT =====
# @app.route("/logout")
# def logout():
#     session.pop("user", None)
#     return redirect("/login")

# if __name__=="__main__":
#     app.run(debug=True)

#project-16:
# from flask import Flask, render_template_string, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - SHOW POSTS =====
# @app.route("/")
# def posts_list():
#     cursor.execute("SELECT * FROM posts")
#     posts = cursor.fetchall()
#     html = """
#     <h2>Blog Posts</h2>
#     <ul>
#     {% for p in posts %}
#         <li>
#             <a href="/post/{{p.id}}">{{p.title}}</a>
#         </li>
#     {% endfor %}
#     </ul>
#     """
#     return render_template_string(html, posts=posts)

# # ===== POST DETAIL + COMMENTS =====
# @app.route("/post/<int:id>", methods=["GET","POST"])
# def post_detail(id):
#     # Add comment
#     if request.method=="POST":
#         author = request.form["author"]
#         comment = request.form["comment"]
#         cursor.execute("INSERT INTO comments (post_id, author, comment) VALUES (%s,%s,%s)",
#                        (id, author, comment))
#         conn.commit()
#         return redirect(f"/post/{id}")

#     # Fetch post
#     cursor.execute("SELECT * FROM posts WHERE id=%s",(id,))
#     post = cursor.fetchone()

#     # Fetch comments
#     cursor.execute("SELECT * FROM comments WHERE post_id=%s",(id,))
#     comments = cursor.fetchall()

#     html = """
#     <h2>{{post.title}}</h2>
#     <p>{{post.content}}</p>

#     <h3>Comments</h3>
#     <ul>
#     {% for c in comments %}
#         <li><b>{{c.author}}</b>: {{c.comment}}</li>
#     {% endfor %}
#     </ul>

#     <h3>Add Comment</h3>
#     <form method="POST">
#         <input name="author" placeholder="Your Name" required><br><br>
#         <textarea name="comment" placeholder="Write a comment..." required></textarea><br><br>
#         <button>Add Comment</button>
#     </form>

#     <a href="/">Back to Posts</a>
#     """
#     return render_template_string(html, post=post, comments=comments)

# if __name__=="__main__":
#     app.run(debug=True)
#project-17:
# from flask import Flask, render_template_string, request
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== PRODUCT LIST + CATEGORY FILTER =====
# @app.route("/")
# def product_list():
#     category_id = request.args.get("category")

#     if category_id:
#         cursor.execute("SELECT * FROM products WHERE category_id=%s", (category_id,))
#     else:
#         cursor.execute("SELECT * FROM products")

#     products = cursor.fetchall()

#     cursor.execute("SELECT * FROM categories")
#     categories = cursor.fetchall()

#     html = """
#     <h2>E-Commerce Product Catalog</h2>

#     <h3>Categories</h3>
#     <a href="/">All</a>
#     {% for c in categories %}
#         | <a href="/?category={{c.id}}">{{c.name}}</a>
#     {% endfor %}

#     <hr>

#     <h3>Products</h3>
#     <ul>
#     {% for p in products %}
#         <li>
#             <a href="/product/{{p.id}}">{{p.name}}</a> - ₹{{p.price}}
#         </li>
#     {% endfor %}
#     </ul>
#     """
#     return render_template_string(html, products=products, categories=categories)

# # ===== PRODUCT DETAIL PAGE =====
# @app.route("/product/<int:id>")
# def product_detail(id):
#     cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
#     product = cursor.fetchone()

#     html = """
#     <h2>{{product.name}}</h2>
#     <p><b>Price:</b> ₹{{product.price}}</p>
#     <p><b>Description:</b> {{product.description}}</p>
#     <a href="/">Back to Products</a>
#     """
#     return render_template_string(html, product=product)

# if __name__ == "__main__":
#     app.run(debug=True)

#project-18:

# from flask import Flask, render_template_string, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - SHOW ENROLLMENTS =====
# @app.route("/", methods=["GET","POST"])
# def home():

#     # ENROLL STUDENT
#     if request.method == "POST":
#         student_id = request.form["student_id"]
#         course_id = request.form["course_id"]

#         cursor.execute(
#             "INSERT INTO enrollments (student_id, course_id) VALUES (%s,%s)",
#             (student_id, course_id)
#         )
#         conn.commit()
#         return redirect("/")

#     # Fetch students and courses
#     cursor.execute("SELECT * FROM students")
#     students = cursor.fetchall()

#     cursor.execute("SELECT * FROM courses")
#     courses = cursor.fetchall()

#     # Fetch enrollments (JOIN)
#     cursor.execute("""
#         SELECT e.id, s.name, c.course_name
#         FROM enrollments e
#         JOIN students s ON e.student_id = s.id
#         JOIN courses c ON e.course_id = c.id
#     """)
#     enrollments = cursor.fetchall()

#     html = """
#     <h2>Student Course Enrollment</h2>

#     <h3>Enroll Student</h3>
#     <form method="POST">
#         <select name="student_id">
#             {% for s in students %}
#                 <option value="{{s.id}}">{{s.name}}</option>
#             {% endfor %}
#         </select>

#         <select name="course_id">
#             {% for c in courses %}
#                 <option value="{{c.id}}">{{c.course_name}}</option>
#             {% endfor %}
#         </select>

#         <button>Enroll</button>
#     </form>

#     <hr>

#     <h3>Enrollment List</h3>
#     <ul>
#     {% for e in enrollments %}
#         <li>{{e.name}} enrolled in {{e.course_name}}</li>
#     {% endfor %}
#     </ul>
#     """

#     return render_template_string(html, students=students, courses=courses, enrollments=enrollments)

# if __name__ == "__main__":
#     app.run(debug=True)

#project-19:

# from flask import Flask, render_template_string, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # ===== MySQL Connection =====
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="23082005",
#     database="flaskdb",
#     port=3306,
#     auth_plugin="mysql_native_password"
# )

# cursor = conn.cursor(dictionary=True)

# # ===== HOME - ADD + VIEW + FILTER EVENTS =====
# @app.route("/", methods=["GET","POST"])
# def event_home():

#     # ADD EVENT
#     if request.method == "POST":
#         title = request.form["title"]
#         event_date = request.form["event_date"]
#         category = request.form["category"]

#         cursor.execute(
#             "INSERT INTO events (title, event_date, category) VALUES (%s,%s,%s)",
#             (title, event_date, category)
#         )
#         conn.commit()
#         return redirect("/")

#     # FILTER
#     filter_category = request.args.get("category")

#     if filter_category:
#         cursor.execute("SELECT * FROM events WHERE category=%s", (filter_category,))
#     else:
#         cursor.execute("SELECT * FROM events")

#     events = cursor.fetchall()

#     html = """
#     <h2>Event Management System</h2>

#     <h3>Add Event</h3>
#     <form method="POST">
#         <input name="title" placeholder="Event Title" required><br><br>
#         <input type="date" name="event_date" required><br><br>
#         <input name="category" placeholder="Category (Tech, Sports, etc)" required><br><br>
#         <button>Add Event</button>
#     </form>

#     <hr>

#     <h3>Filter By Category</h3>
#     <a href="/">All</a> |
#     <a href="/?category=Tech">Tech</a> |
#     <a href="/?category=Sports">Sports</a>

#     <hr>

#     <h3>Event List</h3>
#     <ul>
#     {% for e in events %}
#         <li>
#             {{e.title}} - {{e.event_date}} ({{e.category}})
#             - <a href="/delete/{{e.id}}">Delete</a>
#         </li>
#     {% endfor %}
#     </ul>
#     """

#     return render_template_string(html, events=events)

# # ===== DELETE EVENT =====
# @app.route("/delete/<int:id>")
# def delete_event(id):
#     cursor.execute("DELETE FROM events WHERE id=%s", (id,))
#     conn.commit()
#     return redirect("/")

# if __name__ == "__main__":
#     app.run(debug=True)

#project-20:

from flask import Flask, render_template_string, request, redirect
import mysql.connector
import random
import string

app = Flask(__name__)

# ===== MySQL Connection =====
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="23082005",
    database="flaskdb",
    port=3306,
    auth_plugin="mysql_native_password"
)

cursor = conn.cursor(dictionary=True)

# ===== FUNCTION TO GENERATE SHORT CODE =====
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# ===== HOME - CREATE SHORT URL =====
@app.route("/", methods=["GET","POST"])
def home():

    short_url = None

    if request.method == "POST":
        long_url = request.form["long_url"]
        code = generate_code()

        cursor.execute(
            "INSERT INTO urls (long_url, short_code) VALUES (%s,%s)",
            (long_url, code)
        )
        conn.commit()

        short_url = request.host_url + code

    html = """
    <h2>URL Shortener</h2>

    <form method="POST">
        <input name="long_url" placeholder="Enter Long URL" required style="width:300px">
        <button>Shorten</button>
    </form>

    {% if short_url %}
        <p>Short URL: <a href="{{short_url}}">{{short_url}}</a></p>
    {% endif %}
    """

    return render_template_string(html, short_url=short_url)

# ===== REDIRECT USING SHORT CODE =====
@app.route("/<code>")
def redirect_url(code):
    cursor.execute("SELECT * FROM urls WHERE short_code=%s",(code,))
    url = cursor.fetchone()

    if url:
        return redirect(url["long_url"])
    return "Invalid short URL"

if __name__ == "__main__":
    app.run(debug=True)