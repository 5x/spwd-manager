import ttkbootstrap as ttk

from spwdmanager.gui import INNER_PADDING


class PasswordExtendedWidget(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.input = PasswordWidget(self)
        self.input.pack(side=ttk.LEFT, padx=(0, INNER_PADDING), fill=ttk.X, expand=ttk.YES)

        self.btn = ttk.Button(self, bootstyle="secondary-outline", image="eye", command=self.input.toggle_pass_view)
        self.btn.pack(side=ttk.RIGHT)

    @property
    def value(self):
        return self.input.value

    @value.setter
    def value(self, value):
        self.input = value

    def focus(self):
        if self.master:
            self.master.after(0, lambda: self.input.focus())
        else:
            self.focus()


class PasswordWidget(ttk.Entry):
    def __init__(self, master=None, hide_value=True, **kwargs):
        self.hide_value = hide_value
        show = "*" if self.hide_value else ""

        super().__init__(master, show=show, **kwargs)

    @property
    def value(self):
        return self.get()

    @value.setter
    def value(self, value):
        self.delete(0, ttk.END)
        self.insert(0, value)

    def toggle_pass_view(self):
        show = "" if self.hide_value else "*"
        self.config(show=show)
        self.hide_value = not self.hide_value
