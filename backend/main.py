from flask import Flask, request, jsonify
import mysql.connector, mysql.connector.pooling

app = Flask(__name__)

# https://dev.mysql.com/doc/connector-python/en/connector-python-connection-pooling.html
dbconfig = {
    "host": "192.168.56.12",
    "user": "webuser",
    "password": "placeholder_password",
    "database": "ironsand"
}


cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",
                              pool_size = 5,
                              **dbconfig)
    
@app.route("/retrieve_samples")
def list_deposits():
    try:
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM SAMPLE")
        rows = cursor.fetchall()

        cursor.close()
        cnx.close()

        return jsonify(rows)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


@app.route("/insert_sample", methods=["POST"])
def insert_sample():
    data = request.get_json()
    
    try:
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
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
        cnx.commit()
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


@app.route("/update_sample", methods=["PUT"])
def update_sample():
    pass

@app.route("/delete_sample", methods=["DELETE"])
def delete_sample():
    data = request.args.get("id")
    try:
        cnx = cnxpool.get_connection()
        cursor = cnx.cursor()
        cursor.execute(
            "DELETE FROM SAMPLE WHERE id = %s",
            (
                data,
            )
        )
        cnx.commit()
        cursor.close()
        cnx.close()  
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500     

    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

