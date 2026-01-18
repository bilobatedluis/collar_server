from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/gps", methods=["POST"])
def gps():
    data = request.json

    collar = data.get("id", "desconocido")
    lat = data.get("lat")
    lng = data.get("lng")
    rssi = data.get("rssi")

    print("\n===== NUEVO REPORTE =====")
    print("Collar:", collar)
    print("Lat:", lat)
    print("Lng:", lng)
    print("RSSI:", rssi)
    print("Hora:", datetime.now())

    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run()
