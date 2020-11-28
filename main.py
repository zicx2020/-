class goose :
    name = 'Серый, Белый'
    voice = 'га - га'
    weight = str(7) + ' Кг'
    satiety = 'Голод'
    eggs = 'Есть яйца в гнезде'
    def  feed(self):
         self.satiety = 'Сытость'
    def  collect_eggs(self):
         self.eggs = 'Нету яиц в гнезде'
goose_0 = goose()

class cow :
    name = 'Манька'
    voice = 'Мууу'
    satiety = 'Голод'
    weight = str(250) + ' Кг'
    milk = 'Есть молоко'
    def  feed(self):
         self.satiety = 'Сытость'
    def take_milk(self):
        self.milk = 'Нету молока'
cow_0 = cow()


class shep :
    name = 'Барашек , Кудрявый'
    voice = 'Бееее'
    satiety = 'Голод'
    weight = str(70) + ' Кг'
    wool = 'Есть шерсть '
    def  feed(self):
         self.satiety = 'Сытость'
    def cut(self):
        self.wool = 'Нету шерсти '
shep_0 = shep()


class  chicken(goose):
    name = ['Ко-Ко,Кукареку']
    voice = 'кудкудах'
    weight = str(4) + ' Кг'
chicken_0 = chicken()



class goat(cow):
    name = ['Рога,Копыта']
    voice = 'Мееее'
    weight = str(30) + 'Кг'
goat_0 = goat()




class duck(goose) :
    name = 'Кряква'
    voice = 'Кря-кря'
    weight = str(5) + 'Кг'
duck_0 = duck()



def poo() :
    print('Выберите действие :'
          ' \n 1 - покормить всех '
          ' \n 2 - подоить  '
          ' \n 3 - собрать яйца'
          ' \n 4 - постричь '
          ' \n 5 - сделать всё')

    user = int(input('Выберите  действие из выше перечисленых : '))
    if  user == 1 :
        goose_0.feed()
        duck_0.feed()
        cow_0.feed()
        goat_0.feed()
        chicken_0.feed()
        shep_0.feed()
        print('Все накормлены .')

    elif user == 2 :
        cow_0.take_milk()
        goat_0.take_milk()
        print('Молоко собрано .')

    elif user == 3 :
        chicken_0.collect_eggs()
        duck_0.collect_eggs()
        goose_0.collect_eggs()
        print('Все яйца собраны .')

    elif user == 4 :
        shep_0.cut()
        print('Овцы пострижены .')

    elif user == 5 :
        goose_0.feed()
        duck_0.feed()
        cow_0.feed()
        goat_0.feed()
        chicken_0.feed()
        shep_0.feed()
        print('\nВсе накормлены . \n')
        cow_0.take_milk()
        goat_0.take_milk()
        print('Молоко собрано .\n')
        chicken_0.collect_eggs()
        duck_0.collect_eggs()
        goose_0.collect_eggs()
        print('Все яйца собраны .\n')
        shep_0.cut()
        print('Овцы пострижены .\n')
    return
print(poo())