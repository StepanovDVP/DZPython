import function as fs

# программа
while True:
    choose = int(input("Выберите действие: " "\n"
                           "1 - Добавить контакт" "\n"
                           "2 - Показать все контакты" "\n"
                           "3 - Поиск контакта" "\n"
                           "4 - Редактировать или удалить контакт" "\n"
                           "0 - Завершить работу" "\n"
                            "Сделать выбор =>  "))
    if choose == 1:
        new_person = fs.add_contact()
        print(f"Контакт добавлен")
    elif choose == 2:
        print(f"Ваш справочник: \n{fs.show_contact()}")
    elif choose == 3:
        fs.search_contact()
    elif choose == 4:
        fs.delete_or_edit_contact()
    elif choose == 0:
        break