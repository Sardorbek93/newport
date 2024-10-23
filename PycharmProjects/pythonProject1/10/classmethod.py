# @classmethod - Декоратор


class Animal:
    @classmethod
    def info (cls):
        print('Это для создания животных')

Animal.info()

