from flask import Flask, request
import Hacka
import mysql.connector

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        csv_data = csv.reader(file)
        next(csv_data)  # Skip header row
        db_connection = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="yourdatabase"
        )
        cursor = db_connection.cursor()
        for row in csv_data:
            cursor.execute("INSERT INTO transactions (Amount, Description) VALUES (%s, %s)", (row[0], row[1]))
        db_connection.commit()
        db_connection.close()
        return 'File uploaded successfully!'
    else:
        return 'No file uploaded.'

if __name__ == '__main__':
    app.run(debug=True)
