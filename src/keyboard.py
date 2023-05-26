from src.item import Item


class Mixin_Lang():
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language


    def change_lang(self):
        if self.__language == "EN":
            self.__language =  "RU"
        else:
            self.__language = "RU"
        return self


class Keyboard(Item, Mixin_Lang):
    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = language



# if __name__ == '__main__':
#     kb = Keyboard('Dark Project KD87A', 9600, 5)
#     assert str(kb) == "Dark Project KD87A"
#
#     assert str(kb.language) == "EN"
#
#     kb.change_lang()
#     assert str(kb.language) == "RU"
#
#     # Сделали RU -> EN -> RU
#     kb.change_lang().change_lang()
#     assert str(kb.language) == "RU"
#
#     kb.language = 'CH'
#     # AttributeError: property 'language' of 'KeyBoard' object has no setter



