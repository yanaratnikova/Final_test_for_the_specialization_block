class Animal:
    animal_counter = 0

    def __init__(self, name, species, commands, birth_date):
        self.name = name
        self.species = species
        self.commands = commands
        self.birth_date = birth_date
        Animal.animal_counter += 1

    def get_commands(self):
        return self.commands


animal_registry = {}


def add_animal():
    name = input("Введите имя животного: ")
    species = input("Введите вид животного (собака, кошка, хомяк и т.д.): ")
    commands = input("Введите список команд, которые может выполнять животное: ")
    birth_date = input("Введите дату рождения животного (гггг-мм-дд): ")

    animal = Animal(name, species, commands, birth_date)
    animal_registry[name] = animal
    print("Животное добавлено в реестр.")


def list_commands():
    name = input("Введите имя животного, для которого хотите увидеть список команд: ")
    if name in animal_registry:
        animal = animal_registry[name]
        print(f"Список команд для {name}: {animal.get_commands()}")
    else:
        print("Животное не найдено.")


def teach_commands():
    name = input("Введите имя животного, которому хотите добавить новую команду: ")
    if name in animal_registry:
        new_command = input("Введите новую команду: ")
        animal = animal_registry[name]
        animal.commands += ", " + new_command
        print(f"Новая команда добавлена для {name}.")
    else:
        print("Животное не найдено.")


def list_animals_by_birth_date():
    sorted_animals = sorted(animal_registry.values(), key=lambda x: x.birth_date)
    print("Список животных по дате рождения:")
    for animal in sorted_animals:
        print(f"{animal.name} - {animal.birth_date}")


def display_animal_count():
    print(f"Общее количество животных в реестре: {Animal.animal_counter}")


# Навигация по меню
while True:
    print("Меню:")
    print("1. Добавить новое животное")
    print("2. Список команд животного")
    print("3. Обучение новым командам")
    print("4. Вывести список животных по дате рождения")
    print("5. Вывести количество созданных животных")
    print("6. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        add_animal()
    elif choice == '2':
        list_commands()
    elif choice == '3':
        teach_commands()
    elif choice == '4':
        list_animals_by_birth_date()
    elif choice == '5':
        display_animal_count()
    elif choice == '6':
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")