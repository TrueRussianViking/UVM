import tkinter as tk
from subprocess import run

root = tk.Tk()
root.title('UVM')

src = tk.Text(root,height=20,width=60)
src.pack()
out = tk.Text(root,height=10,width=60)
out.pack()

def build():
    open('tmp.json','w').write(src.get('1.0','end'))
    run(['python','assembler.py','tmp.json','tmp.bin'])
    run(['python','interpreter.py','tmp.bin','dump.csv','0','50'])
    out.insert('end',open('dump.csv').read())

tk.Button(root,text='Assemble & Run',command=build).pack()
root.mainloop()