import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os, sys, csv

if not __name__ == '__main__':
    from . import logic




class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=400, height=320, borderwidth=4, relief='groove')
        self.root = root
        self.create_first_widgets()

    def create_first_widgets(self):
        # ファイル指定の関数
        def filedialog_clicked():
            #fTyp = [('csvファイル', '*.csv')]
            #iFile = os.path.abspath(os.path.dirname(__file__))
            #iFilePath = filedialog.askopenfilenames(filetypes = fTyp, initialdir = iFile)
            #entry1.set(iFilePath)
            iDir = os.path.abspath(os.path.dirname(__file__))
            iDirPath = filedialog.askdirectory(initialdir = iDir)
            entry1.set(iDirPath)

        # フォルダ指定の関数
        def dirdialog_clicked():
            iDir = os.path.abspath(os.path.dirname(__file__))
            iDirPath = filedialog.askdirectory(initialdir = iDir)
            entry2.set(iDirPath)
        
        # 実行ボタン押下時の実行関数
        def conductMain():
            targetPath = entry1.get()
            savePath = entry2.get()
            method_name = entry3.get()
            delta = int(entry4.get())
            degree = int(entry5.get())
            frag_delta = False
            frag_degree = False
            for i in range(len(method_index_box)):          #determine the method ID in method_index_box
                if method_index_box[i][1] == method_name:
                    frag_method = int(method_index_box[i][0])
                    if method_index_box[i][2] == 1:
                        frag_delta = True
                    if method_index_box[i][3]  == 1:
                        frag_degree = True
                    break


            method_name = method_name.replace('XXX', str(delta)).replace('YYY', str(degree))


            
            if targetPath == '' or savePath == '':
                messagebox.showerror('error', 'パスの指定がありません。')
            elif method_name == '':
                messagebox.showerror('error', 'モードが選択されていません。')
            elif frag_delta:
                if delta == '':
                    messagebox.showerror('error', 'deltaを設定してください。')
            elif frag_degree:
                if degree == '':
                    messagebox.showerror('error', 'degreeを設定してください。')
            else:
                logic.main_logic(targetPath=targetPath, savePath=savePath, frag_method=frag_method, 
                    method_name=method_name, delta=delta, degree=degree)




        with open(os.getcwd() + os.sep + 'st' + os.sep \
            + 'method_index.csv', encoding='shift-jis') as f:           #scan to method_index
            csvreader = csv.reader(f)
            method_index_box = [row for row in csvreader]

        # Frame1の作成
        frame1 = ttk.Frame(self.root, padding=10)
        frame1.grid(row=0, column=1, sticky=tk.E)

        # 「フォルダ参照」ラベルの作成
        IDirLabel = ttk.Label(frame1, text='参照先フォルダ＞＞', padding=(5, 2))
        IDirLabel.pack(side=tk.LEFT)

        # 「フォルダ参照」エントリーの作成
        entry1 = tk.StringVar()
        IDirEntry = ttk.Entry(frame1, textvariable=entry1, width=30)
        IDirEntry.pack(side=tk.LEFT)

        # 「フォルダ参照」ボタンの作成
        IDirButton = ttk.Button(frame1, text='参照', command=filedialog_clicked)
        IDirButton.pack(side=tk.LEFT)

        # Frame2の作成
        frame2 = ttk.Frame(self.root, padding=10)
        frame2.grid(row=2, column=1, sticky=tk.E)

        # 「ファイル参照」ラベルの作成
        IFileLabel = ttk.Label(frame2, text='保存先フォルダ＞＞', padding=(5, 2))
        IFileLabel.pack(side=tk.LEFT)

        # 「ファイル参照」エントリーの作成
        entry2 = tk.StringVar()
        IFileEntry = ttk.Entry(frame2, textvariable=entry2, width=30)
        IFileEntry.pack(side=tk.LEFT)

        # 「ファイル参照」ボタンの作成
        IFileButton = ttk.Button(frame2, text='参照', command=dirdialog_clicked)
        IFileButton.pack(side=tk.LEFT)

        # Frame3の作成
        frame3 = ttk.Frame(self.root, padding=10)
        frame3.grid(row=4, column=1, sticky=tk.W)

        # 「モード選択」ラベルの作成
        SModeLabel = ttk.Label(frame3, text='モード選択', padding=(5, 2))
        SModeLabel.pack(side=tk.LEFT)

        # モード選択肢の設置
        method_index = []
        for i in range(len(method_index_box)-1):
            method_index.append(method_index_box[i+1][1])
        entry3 = tk.StringVar()
        combobox1 = ttk.Combobox(frame3, height=3, state='readonly', textvariable=entry3, values=method_index)
        combobox1.pack(side=tk.LEFT)

        # 「delta」ラベルの作成
        SDeltaLabel = ttk.Label(frame3, text='delta', padding=(5, 2))
        SDeltaLabel.pack(side=tk.LEFT)

        # 「delta」エントリーの作成
        entry4 = tk.StringVar()
        SDeltaEntry = ttk.Entry(frame3, textvariable=entry4, width=5)
        SDeltaEntry.pack(side=tk.LEFT)

        # 「degree」ラベルの作成
        SDegreeLabel = ttk.Label(frame3, text='degree', padding=(5, 2))
        SDegreeLabel.pack(side=tk.LEFT)

        # 「degree」エントリーの作成
        entry5 = tk.StringVar()
        SDegreeEntry = ttk.Entry(frame3, textvariable=entry5, width=5)
        SDegreeEntry.pack(side=tk.LEFT)

        # Frame4の作成
        frame4 = ttk.Frame(self.root, padding=10)
        frame4.grid(row=7, column=1, sticky=tk.E)

        # 実行ボタンの設置
        button1 = ttk.Button(frame4, text='実行', command=conductMain)
        button1.pack(fill = 'x', padx=10, side = tk.LEFT)

        # キャンセルボタンの設置
        button2 = ttk.Button(frame4, text=('閉じる'), command=quit)
        button2.pack(fill = 'x', padx=10, side = tk.LEFT)



if __name__ == '__main__':
    import logic

    root = tk.Tk()
    root.title('SmoothinTool_ver1.2.0')
    root.geometry('550x200')
    app = Application(root=root)
    app.mainloop()