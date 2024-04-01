class MixinPrintRepr:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        class_name = self.__class__.__name__
        attrs = []
        for key, value in self.__dict__.items():
            attrs.append(f'{key}:{value}')
        return f'Создан объект {class_name} с атрибутами {", ".join(attrs)}'

