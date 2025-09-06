from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def connect_to_database():
    try:
        # Connect to the database VM
        db = mysql.connector.connect(
            host="192.168.56.12",  
            user="webuser",
            password="placeholder_password",
            database="ironsand"
        )
        if db.is_connected():
            return db
        else:
            raise Exception("Failed to connect")
    except mysql.connector.Error as err:
        raise Exception(f"Error connecting to database: {err}")



@app.route("/retrieve_samples")
def list_deposits():
    try:
        db = connect_to_database()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM SAMPLE")
        rows = cursor.fetchall()

        cursor.close()
        db.close()

        return jsonify(rows)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


@app.route("/insert_sample", methods=["POST"])
def insert_sample():
    data = request.get_json()
    
    try:
        db = connect_to_database()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO SAMPLE (name, latitude, longitude, rock_type, description, date_discovered) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (
                data["name"],
                data["latitude"],
                data["longitude"],
                data["rock_type"],
                data.get("description", ""),
                data["date_discovered"]
            )
        )
        db.commit()
        cursor.close()
        db.close()
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


@app.route("/update_deposit", methods=["PUT"])
def update_deposit():
    db = connect_to_database()
    db.close()
    return "<p>Hello, World!</p>"

@app.route("/delete_deposit", methods=["DELETE"])
def delete_deposit():
    db = connect_to_database()
    db.close()
    return "<p>Hello, World!</p>"
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

