path = "file.txt"
# метод для поиска контакта 
def search_contact():
    with open(path, 'r', encoding='utf-8') as base:
        name = input("Введите данные для поиска: ")
        s = 0
        empty = False
        for i in base.read().split('\n'):
            if name.lower() in str(i.lower()):
                s += 1
                print(f"{s}. {i}")
                empty = True
        if not empty:
             print("Данного контакта нет в записной книжки")

# метод для добавления нового контакта 
def add_contact():
    with open(path, "a", encoding='utf-8') as base:
        data = base.write(input("Добавьте контакт: ") + '\n')
    return data

# показать все контакты
def show_contact():
    with open(path, "r", encoding='utf-8') as base:
        return base.read()

# перезапись файла 
def rewrite_files(book):
    with open('file.txt', 'w', encoding='utf-8') as base:
        base.writelines('')
    with open('file.txt', 'a', encoding='utf-8') as base:
        for i in book:
            if len(i) > 0:
                i = i+'\n'
            base.write(i)
    print('Данные успешно изменены')

# удаление контакта 
def delete_or_edit_contact():
    data = input('введите контакт для редактирования: ')
    with open(path, "r", encoding='utf-8') as base:
        book = base.read().split('\n')
        try:
            our_list = [i for i in book if data in i]
            count = 0
            for i in our_list:
                count += 1
                print(f"{count} - {i}")
            if len(our_list) > 1:
                del_string=int(input('Введите номер строки для редактирования: '))
                with open('file.txt', 'r', encoding='utf-8') as base:
                    book = base.read().split('\n')
                new_book = []
                del_or_edit = int(input("Выбирите действие: 1 - удалить контакт; 2 - редактировать => "))
                if del_or_edit == 1:
                    for i in range(len(book)):
                        if book[i] != our_list[del_string-1]:
                            new_book.append(book[i])
                    # rewrite_files(new_book)
                elif del_or_edit == 2:
                    for i in range(len(book)):
                        if book[i] != our_list[del_string-1]:
                            new_book.append(book[i])
                        else:
                            new_book.append(input('введите новое значение: '))
                else:
                    print("повторите ввод; 1 - удалить контакт; 2 - редактировать => ")
                rewrite_files(new_book)
                    
            else:
                with open('file.txt', 'r', encoding='utf-8') as base:
                    book = base.read().split('\n')
                new_book = []
                del_or_edit = int(input("Выбирите действие: 1 - удалить контакт; 2 - редактировать =>  "))
                if del_or_edit == 1:
                    for i in range(len(book)):
                        if book[i] != our_list[0]:
                            new_book.append(book[i])
                elif del_or_edit == 2:
                    for i in range(len(book)):
                        if book[i] != our_list[0]:
                            new_book.append(book[i])
                        else:
                            new_book.append(input('введите новое значение: '))
                else:
                    print("повторите ввод; 1 - удалить контакт; 2 - редактировать")
                rewrite_files(new_book)
        except IndexError:
            print('Данного контакта нет в записной книжки')
        