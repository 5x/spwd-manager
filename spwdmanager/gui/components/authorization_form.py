import ttkbootstrap as ttk

from spwdmanager.gui import INNER_PADDING
from spwdmanager.gui.components.password_block import PasswordExtendedWidget


class AuthorizationForm(ttk.Frame):
    def __init__(self, master=None, default_storage_path=None):
        super().__init__(master)

        path_block = ttk.Frame(self)
        path_block.pack(fill=ttk.X, expand=ttk.YES, pady=(0, INNER_PADDING))

        self._path = ttk.Entry(path_block)
        self._path.pack(side=ttk.LEFT, padx=(0, INNER_PADDING), fill=ttk.X, expand=ttk.YES)
        self._path.insert(0, str(default_storage_path))

        select_file_btn = ttk.Button(path_block, bootstyle="secondary-outline", image="folder")
        select_file_btn.pack(side=ttk.RIGHT)

        self._password = PasswordExtendedWidget(self)
        self._password.pack(fill=ttk.X, expand=ttk.YES)

    @property
    def path(self):
        return self._path.get()

    @path.setter
    def path(self, value):
        self._path.delete(0, ttk.END)
        self._path.insert(0, value)

    @property
    def password(self):
        return self._password.value

    def focus_password_input(self):
        self._password.focus()

    def bind_input_event(self, event_type, handle):
        self._password.input.bind(event_type, handle)
