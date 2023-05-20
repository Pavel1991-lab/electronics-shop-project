from src.item import Item


class Mixin_Lang():
    lang_count = 0

    def change_lang(self):
        self.lang_count += 1
        if self.lang_count %2 == 0:
            self.language = "EN"
        else:
            self.language = "RU"
        return self

class Keyboard(Item, Mixin_Lang):
    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self.language = language






