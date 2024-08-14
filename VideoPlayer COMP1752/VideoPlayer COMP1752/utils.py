
import tkinter.scrolledtext as tkst

def set_text(text_widget, text):
    text_widget.configure(state="normal")
    text_widget.delete(1.0, "end")
    text_widget.insert("insert", text)
    text_widget.configure(state="disabled")
