import mysql.connector

def create_db():
    try:
        # Connect to MySQL
        mydb = mysql.connector.connect(host='localhost', user='root', password='varsha', database='firstproject')
        cur = mydb.cursor()

        # Create 'course' table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS course (
                courseid INT AUTO_INCREMENT PRIMARY KEY,
                coursename TEXT,
                duration TEXT,
                charges TEXT,
                description TEXT
            )
        """)

        # Create 'student' table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS student (
                rollno INT AUTO_INCREMENT PRIMARY KEY,
                name TEXT,
                email TEXT,
                gender TEXT,
                dateofbirth TEXT,
                contactno TEXT,
                admission TEXT,
                course TEXT,
                state TEXT,
                city TEXT,
                pincode TEXT,
                address TEXT
            )
        """)

        # Create 'result' table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS result (
                rid INT AUTO_INCREMENT PRIMARY KEY,
                roll TEXT,
                name TEXT,
                course TEXT,
                marks TEXT,
                full_marks TEXT,
                per TEXT
            )
        """)

        # Commit the changes
        mydb.commit()

        

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close cursor and database connection
        if cur:
            cur.close()
        if mydb:
            mydb.close()

# Call the function to create tables
create_db()
