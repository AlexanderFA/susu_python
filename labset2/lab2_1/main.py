# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# 1.  Напишите программу, содержащую класс "Воин".
#
# • От класса создаются два экземпляра.
# • Каждому устанавливается здоровье в 100 очков.
# • В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# • После каждого удара надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья.
# • Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
#
# 2.   Добавьте конструктор, устанавливающий здоровье 100 очков и имя воина при создании экземпляра
#
# 3.   Добавьте деструктор, выводящий сообщение "До свидания, воин <имя>!"

from Warrior import Warrior
from WarriorA import WarriorA
from Dice import roll_dice

name1 = input('Input warrior 1 name: ')
name2 = input('Input warrior 1 name: ')
# warrior_a, warrior_b = WarriorA(name1), Warrior(name2)
warrior_a, warrior_b = Warrior(name1), Warrior(name2)

while True:
    attacker, victim = warrior_a, warrior_b
    if 1 == roll_dice():
        attacker, victim = warrior_b, warrior_a

    attacker.hits(victim)

    if victim.get_hp() <= 0:
        print('Warrior', attacker.get_name(), 'has won!')
        break
