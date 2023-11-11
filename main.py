from random import randint
from graphic_arts.start_game_banner import run_screensaver

# Значение атаки по умолчанию.
DEFAULT_ATTACK_VALUE = 5
# Значение защиты по умолчанию.
DEFAULT_DEFENCE_VALUE = 10

DEFAULT_STAMINA = 80 


class Character:
    # Диапазон очков урона.
    ATTACK_VALUE_RANGE = (1, 3)
    # Диапазон очков защиты.
    DEFENCE_VALUE_RANGE = (1, 5)
    # Специальное умение.
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    # Количество очуов урона для 
    # Диапазон специального умения.
    SPECIAL_VALUE_RANGE = ()
    # Описание класса.
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    
    # Объявляем конструктор класса.
    def __init__(self, name):
        self.name = name

    # Объявляем метод атаки.
    def attack(self):
        attack_value = DEFAULT_ATTACK_VALUE + randint(*self.ATTACK_VALUE_RANGE)
        return(f'{self.name} нанес противнику урон, равный '
               f'{attack_value}')
    
    # Защита.
    def defence(self):
        defence_value = DEFAULT_DEFENCE_VALUE + randint(*self.DEFENCE_VALUE_RANGE)
        return (f'{self.name} блокировал {defence_value} ед. урона.')
    
    # Объявляем метод специального умения.
    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'

class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    ATTACK_VALUE_RANGE = (3, 5)
    DEFENCE_VALUE_RANGE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'
    

class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    ATTACK_VALUE_RANGE = (5, 10)
    DEFENCE_VALUE_RANGE = (-2 , 2)
    SPECIAL_BUFF = DEFAULT_ATTACK_VALUE + 40
    SPECIAL_SKILL = 'Атака'
    
    
class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    ATTACK_VALUE_RANGE = (-3, -1)
    DEFENCE_VALUE_RANGE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE_VALUE + 30
    SPECIAL_SKILL = 'Защита'


def choise_char_class(char_name: str) -> Character:
    game_classes = {
        'warrior':Warrior,
        'mage': Mage,
        'healer': Healer
    }

    approve_choise: str = None

    while approve_choise != 'y':
        selected_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)

        print(char_class)
        approve_choise = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class