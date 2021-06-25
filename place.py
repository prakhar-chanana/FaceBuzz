from tkinter import *
from tkinter import ttk


class PlaceholderEntry(ttk.Entry):
    # def __init__(self, master: Optional[tkinter.Misc], widget: Optional[str], *, background: tkinter._Color, class_: str, cursor: tkinter._Cursor, exportselection: bool, font: _FontDescription, foreground: tkinter._Color, invalidcommand: tkinter._EntryValidateCommand, justify: Literal["left", "center", "right"], name: str, show: str, state: str, style: str, takefocus: tkinter._TakeFocusValue, textvariable: tkinter.Variable, validate: Literal["none", "focus", "focusin", "focusout", "key", "all"], validatecommand: tkinter._EntryValidateCommand, width: int, xscrollcommand: tkinter._XYScrollCommand) -> None:
    #     super().__init__(master=master, widget=widget, background=background, class_=class_, cursor=cursor, exportselection=exportselection, font=font, foreground=foreground, invalidcommand=invalidcommand, justify=justify, name=name, show=show, state=state, style=style, takefocus=takefocus, textvariable=textvariable, validate=validate, validatecommand=validatecommand, width=width, xscrollcommand=xscrollcommand)
    def __init__(self, container, placeholder, *args, **kwargs):
        super().__init__(container,*args,**kwargs)
        self.placeholder = placeholder

        self.field_style = kwargs.pop("style","TEntry")
        self.placeholder_style = kwargs.pop("placeholder_style", self.field_style)
        self["style"] = self.placeholder_style

        self.insert("0", self.placeholder)
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>",self._add_placeholder)
    
    def _clear_placeholder(self,e):
        if self["style"]==self.placeholder_style:
            self.delete("0",'end')
            self["style"] = self.field_style

    def _add_placeholder(self,e):
        if not self.get():
            self.insert("0",self.placeholder)
            self["style"] = self.placeholder_style