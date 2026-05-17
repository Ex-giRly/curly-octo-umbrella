import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)
    if length == 0:
        strength.set("Enter a password")
    elif length < 4:
        strength.set("Weak")
    elif length < 8:
        strength.set("Moderate")
    else:
        strength.set("Strong")

root = tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*")
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_strength).pack(pady=5)

strength = tk.StringVar()
tk.Label(root, textvariable=strength, font=("Arial", 12, "bold")).pack(pady=10)

root.mainloop()