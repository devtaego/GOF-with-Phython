from abc import ABC, abstractmethod


# =========================
# Abstract Product
# =========================

class Button(ABC):

    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):

    @abstractmethod
    def render(self):
        pass


# =========================
# Windows Products
# =========================

class WindowsButton(Button):

    def render(self):
        return "Windows Button"


class WindowsCheckbox(Checkbox):

    def render(self):
        return "Windows Checkbox"


# =========================
# Mac Products
# =========================

class MacButton(Button):

    def render(self):
        return "Mac Button"


class MacCheckbox(Checkbox):

    def render(self):
        return "Mac Checkbox"
