import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    branch TEXT
)
''')
conn.commit()

# Add a student
def add_student(name, age, branch):
    cursor.execute("INSERT INTO students (name, age, branch) VALUES (?, ?, ?)", (name, age, branch))
    conn.commit()
    print("Student added successfully!")

# View all students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- All Students ---")
    for row in rows:
        print(row)

# Update a student
def update_student(student_id, name, age, branch):
    cursor.execute("UPDATE students SET name = ?, age = ?, branch = ? WHERE id = ?", (name, age, branch, student_id))
    conn.commit()
    print("Student updated successfully!")

# Delete a student
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("Student deleted successfully!")

# Menu
def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            branch = input("Enter branch: ")
            add_student(name, age, branch)

        elif choice == '2':
            view_students()

        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            branch = input("Enter new branch: ")
            update_student(student_id, name, age, branch)

        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# Run the app
if __name__ == "__main__":
    menu()
    conn.close()
