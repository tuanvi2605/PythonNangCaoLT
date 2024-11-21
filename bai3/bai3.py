from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://root:example@localhost:33333")
db = client["dulieu"]
collection = db["kinhdoanh"]

@app.route("/", methods=["GET", "POST"])
def index():
    data = ""
    if request.method == "POST":
        thang = request.form["thang"]
        nam = request.form["nam"]
        try:
            thang = int(thang)
            nam = int(nam)
            result = collection.find_one({"thang": thang, "nam": nam})
            if result:
                data = f"Lợi nhuận tháng {thang} năm {nam} là: {result['loinhuan']} USD"
            else:
                data = "Dữ liệu không tồn tại"
        except ValueError:
            data = "Vui lòng nhập tháng và năm hợp lệ"
    
    return render_template("index.html", loinhuan=data)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)
