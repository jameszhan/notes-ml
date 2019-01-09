from Tkinter import *   
import tkMessageBox   
import tkFileDialog   
import tkColorChooser   
  
root=Tk()   
  
tkMessageBox.showinfo("RESULT",str(tkMessageBox.askyesno("ASK","choose")))   
tkFileDialog.askopenfilename(   
                               
                                initialdir="e:",   
                               
                               filetypes=[(u"c file",".c"),(u"head file",".h")],   
                                title=u"search file"  
                            )   
  

tkColorChooser.askcolor(color="red",title=u"color")   

root.mainloop()  

