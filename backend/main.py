from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route("/deposits")
def list_deposits():
    try:
        # Connect to the database VM
        db = mysql.connector.connect(
            host="192.168.56.12",  
            user="webuser",
            password="placeholder_password",
            database="ironsand"
        )

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM DEPOSIT")
        rows = cursor.fetchall()

        cursor.close()
        db.close()

        print (jsonify(rows))
        return jsonify(rows)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    
    
