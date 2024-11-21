import tkinter as tk
from pymongo import MongoClient

client = MongoClient("mongodb://root:example@localhost:33333")
db = client["dulieu"]
collection = db["kinhdoanh"]

def getData():
    thang = tbx_month.get()
    nam = tbx_year.get()
    try:
        thang = int(thang)
        nam = int(nam)
        result = collection.find_one({"thang": thang, "nam": nam})
        if result:
            lbl_result.config(text=f"Lợi nhuận: {result['loinhuan']} VND", fg="green")
        else:
            lbl_result.config(text="Dữ liệu không tồn tại", fg="red")
    except ValueError:
        lbl_result.config(text="Vui lòng nhập tháng và năm hợp lệ", fg="red")

root = tk.Tk()
root.title("Lợi nhuận tháng")

lbl_month = tk.Label(root, text="Nhập tháng:")
lbl_month.grid(row=0, column=0, padx=10, pady=5)
tbx_month = tk.Entry(root)
tbx_month.grid(row=0, column=1, padx=10, pady=5)

lbl_year = tk.Label(root, text="Nhập năm:")
lbl_year.grid(row=1, column=0, padx=10, pady=5)
tbx_year = tk.Entry(root)
tbx_year.grid(row=1, column=1, padx=10, pady=5)

btn_submit = tk.Button(root, text="Enter", command=getData)
btn_submit.grid(row=2, column=0, columnspan=2, pady=10)

lbl_result = tk.Label(root, text="")
lbl_result.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()