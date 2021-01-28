import tkinter as tk
import requests

window = tk.Tk()
window.title("Sequence view")

localHost="http://127.0.0.1:5000"

def get_seq():
    id=geneID.get()
    response=requests.get(localHost+"/v1/sequence/gene/"+id)
    output.insert(tk.END,response.json())
    

def gcContent():
    id=geneID.get()
    response=requests.get(localHost+"/v1/sequence/gene/"+id + "?gc_content=true")
    output.insert(tk.END,response.json())

def swap():
    localHost="http://127.0.0.1:5000"
    id=geneID.get()
    response=requests.get(localHost+"/v1/sequence/gene/"+id + "?swap=A:T")
    output.insert(tk.END,response.json())

def fasta():
    id=geneID.get()
    response=requests.get(localHost+"/v1/sequence/"+id + "?content-type=fasta")
    output.insert(tk.END,response.json())

labelGene = tk.Label(window, text = "Gene ID", font=("Arial", 12))
labelGene.grid(row = 0, column = 0)
geneID = tk.Entry(window)
geneID.grid(row = 0, column = 1)

output=tk.Text(window,height=30, width=100)
output.grid(row=3, column=0, columnspan=4)


btnShow = tk.Button(window, text = "Show sequence and exons",font=("Arial", 12), command =get_seq)
btnShow.grid(row = 1, column = 0)

btnShowGC = tk.Button(window, text = "Show GC content",font=("Arial", 12), command=gcContent)
btnShowGC.grid(row = 1, column = 1 )

btnShowSwap = tk.Button(window, text = "Swap",font=("Arial", 12), command=swap)
btnShowSwap.grid(row = 1, column =2)

btnShowFasta = tk.Button(window, text = "Show in Fasta",font=("Arial", 12), command=fasta)
btnShowFasta.grid(row = 1, column = 3)


#button Clear
btnClear=tk.Button(window, text="Clear", font=("Arial", 12),command=lambda:output.delete("1.0",tk.END))
btnClear.grid(row=4, column=5)

#button QUIT
btnQuit = tk.Button(window, text="QUIT", fg="red",font=("Arial", 12), command=window.destroy)
btnQuit.grid(row=5, column=5)

window.mainloop()
   
