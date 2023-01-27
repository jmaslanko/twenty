import tkinter as tk

class MainApp:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent)
        self.title = tk.Label(self.parent, text='20-20-20')
        self.text = tk.Label(self.parent, text='Look at something 20 feet away for 20 seconds!')
        self.title.pack()
        self.text.pack()
        self.frame.pack()

def main(): 
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()