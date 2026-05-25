import tkinter as tk
from tkinter import messagebox

def add_todo():
    todo = entry.get()
    if todo != "":
        todo_listbox.insert(tk.END, todo)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("경고", "할 일을 입력해주세요!")

def delete_todo():
    try:
        selected_index = todo_listbox.curselection()[0]
        todo_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("경고", "삭제할 항목을 선택해주세요!")

root = tk.Tk()
root.title("나의 첫 시각적 투두리스트")
root.geometry("300x400")

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

add_button = tk.Button(root, text="할 일 추가", command=add_todo)
add_button.pack()

todo_listbox = tk.Frame(root)
todo_listbox = tk.Listbox(root, width=25, height=15)
todo_listbox.pack(pady=10)

delete_button = tk.Button(root, text="선택 항목 삭제", command=delete_todo)
delete_button.pack()

root.mainloop()