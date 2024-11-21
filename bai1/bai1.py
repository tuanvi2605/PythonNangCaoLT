import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        phep_tinh = tbx_input.get()
        ket_qua = eval(phep_tinh)
        lbl_result.config(text=f"Ket qua: {ket_qua}")
    except:
        messagebox.showerror("Lỗi", "Phép tính khong hợp lệ")

root = tk.Tk()
root.title("Máy tính")

lbl_text1 = tk.Label(root, text="Nhập phép tính: ")
lbl_text1.grid(row=0, column=0, padx=5, pady=5)

tbx_input = tk.Entry(root, width=30)
tbx_input.grid(row=1, column=0, padx=5, pady=5)

btn_calculate = tk.Button(root, text="Enter", command=calculate)
btn_calculate.grid(row=2, column=0, padx=5, pady=5)

lbl_result = tk.Label(root, text="")
lbl_result.grid(row=3, column=0, padx=5, pady=10)

root.mainloop()
