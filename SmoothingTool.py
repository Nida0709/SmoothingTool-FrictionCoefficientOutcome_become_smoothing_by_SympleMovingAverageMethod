import tkinter as tk
import st.HomeTk

def main():
    root = tk.Tk()
    root.title('SmoothingTool_ver1.2.0')
    root.geometry('550x200')
    app = st.HomeTk.Application(root=root)
    app.mainloop()

if __name__ == '__main__':
    main()