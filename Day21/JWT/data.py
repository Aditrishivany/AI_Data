import sqlite3


def create_connection(db_name):
    """Create a database connection."""
    conn = sqlite3.connect(db_name)
    return conn


def create_table(conn):
    """Create users table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE
        )
    """)
    conn.commit()


def insert_user(conn, name, age, email):
    """Insert a new user."""
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
        (name, age, email)
    )
    conn.commit()


def get_all_users(conn):
    """Fetch all users."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


def update_user_age(conn, user_id, new_age):
    """Update user's age."""
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET age = ? WHERE id = ?",
        (new_age, user_id)
    )
    conn.commit()


def delete_user(conn, user_id):
    """Delete a user."""
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )
    conn.commit()


def main():
    database = "mydatabase.db"

    # Create connection
    conn = create_connection(database)

    # Create table
    create_table(conn)

    # Insert users
    insert_user(conn, "Alice", 25, "alice@example.com")
    insert_user(conn, "Bob", 30, "bob@example.com")
    insert_user(conn, "Charlie", 22, "charlie@example.com")

    print("\n--- All Users ---")
    users = get_all_users(conn)
    for user in users:
        print(user)

    # Update user
    update_user_age(conn, 1, 26)
    print("\n--- After Updating Alice's Age ---")
    users = get_all_users(conn)
    for user in users:
        print(user)

    # Delete user
    delete_user(conn, 2)
    print("\n--- After Deleting Bob ---")
    users = get_all_users(conn)
    for user in users:
        print(user)

    conn.close()


if __name__ == "__main__":
    main()