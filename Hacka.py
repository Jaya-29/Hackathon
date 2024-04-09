from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/transactions', methods=['GET'])
def get_transactions():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    db_connection.close()
    return jsonify(transactions)

@app.route('/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    data = request.get_json()
    new_amount = data['amount']
    new_description = data['description']
    db_connection = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
    cursor = db_connection.cursor()
    cursor.execute("UPDATE transactions SET Amount = %s, Description = %s WHERE TransactionID = %s", (new_amount, new_description, transaction_id))
    db_connection.commit()
    db_connection.close()
    return 'Transaction updated successfully!'

@app.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    db_connection = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="yourdatabase"
    )
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM transactions WHERE TransactionID = %s", (transaction_id,))
    db_connection.commit()
    db_connection.close()
    return 'Transaction deleted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
