documents_list = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': []}


def get_people(documents):
    """This function asks for the document number and displays the name of
    the person to whom it belongs. When the user enters a non-existent
    document, it returns an error."""

    doc_number = input("Введите номер документа - ")

    doc_len = len(documents)
    for key, value in enumerate(documents):
        if value["number"] == doc_number:
            return value["name"]

    if doc_len == len(documents):
        return "Документ не существует"


def get_shelf(directory):
    """This function asks for the document number and displays the shelf
    number on which it is located. When the user enters a non-existent
    document, it returns an error."""

    num_doc = input("Введите номер документа - ")

    for Shelf_number in directory:
        if num_doc in directory[Shelf_number]:
            return Shelf_number
    return "Документ не существует"


def get_list(documents):
    """This function displays a list of all documents."""

    result_list = ""
    for people in documents:
        result = " ".join(f"{value}" for key, value in people.items())
        result_list += result + "\n"
    return result_list


def get_add(documents, directory):
    """This function will add a new document to the catalog and to the shelf
    list, asking for its number, type, owner's name and the shelf number on
    which it will be stored. When the user tries to add a document to a
    non-existent shelf, return an error."""

    which_shelf = input("Введите номер полки - ")
    if which_shelf in directory.keys():
        type_doc = input("Введите наименование документа - ")
        doc_number = input("Введите номер документа - ")
        name_people = input("Введите ФИО - ")
        new_people = dict(type=type_doc, number=doc_number,
                          name=name_people)
        documents.append(new_people)
        list_doc = directory[which_shelf]
        list_doc.append(doc_number)
        directory[which_shelf] = list_doc
    else:
        print("Полка с таким номером не существует!")
        get_add(documents, directory)
    return documents, directory


def get_delete(documents, directory):
    """This function will ask for the document number and remove it from the
    catalog and shelf list. When the user enters a non-existent document,
    it returns an error."""

    doc_number = input("Введите номер документа - ")

    doc_len = len(documents)
    for key, value in enumerate(documents):
        if value["number"] == doc_number:
            documents.pop(key)

    if doc_len == len(documents):
        return "Документ не существует"

    for value_list in directory.values():
        for doc in value_list:
            if doc_number == doc:
                value_list.remove(doc)

    print(documents_list, directories)
    return "Документ успешно удален"


def get_move(directory):
    """This function will ask for the document number and target shelf and
    move it from the current shelf to the target shelf. When the user tries
    to move a nonexistent document or move a document to a non-existent
    shelf, it returns an error."""

    num_doc = input("Введите номер перемещаемого документа - ")
    num_shelf = input("Введите номер полки, на которую переместить "
                      "документ - ")

    doc_existence = False

    if num_shelf not in directories:
        return "Полки не существует"

    for shelf_number, doc_number in directory.items():
        if num_doc in doc_number:
            doc_existence = True
            directory[num_shelf] += [num_doc]
            doc_number.remove(num_doc)

    if doc_existence:
        print(directory)
        return "Документ успешно перемещен"
    else:
        # print(directory)
        return "Документ не существует"


def get_add_shelf(directory):
    """This function will ask for the number of the new shelf and add it to
    the list. When the user adds a shelf that already exists, it returns an
    error."""

    num_new_shelf = input("Введите номер новой полки - ")

    if num_new_shelf in directory:
        print(directory)
        return "Такая полка уже существует"

    directory[num_new_shelf] = []

    return directory


def main(documents, directory):
    print("Список команд:\n 1. p - 'people' Запрашивает номер документа и "
          "выведет имя человека, которому он принадлежит.\n "
          "2. s - 'shelf' Запрашивает номер документа и выведет номер полки, "
          "на которой он находится.\n 3. l - 'list' выведет список "
          "всех документов.\n 4. a - 'add' добавит новый документ в каталог "
          "и в перечень полок, спросив его номер, тип, имя владельца и номер "
          "полки, на котором он будет храниться.\n 5. d - 'delete' запросит "
          "номер документа и удалит его из каталога и из перечня полок.\n "
          "6. m - 'move' запросит номер документа и целевую полку и "
          "переместит его с текущей полки на целевую.\n 7. as - 'add shelf' "
          "запросит номер новой полки и добавит ее в перечень.\n")
    print(f" \n1. Список всех документов\n\n{get_list(documents)} \n"
          f"2. Полки с документами\n\n{directories}\n")

    while True:
        user_input = input('Введите команду (p,s,l,a,d,m,as,q) - ')
        if user_input == 'p':
            print(get_people(documents))
        elif user_input == 's':
            print(get_shelf(directory))
        elif user_input == 'l':
            print(get_list(documents))
        elif user_input == 'a':
            print(get_add(documents, directory))
        elif user_input == 'd':
            print(get_delete(documents_list, directories))
        elif user_input == 'm':
            print(get_move(directories))
        elif user_input == 'as':
            print(get_add_shelf(directory))
        elif user_input == 'h':
            print("То что в начале выводится")
        elif user_input == 'q':
            break


main(documents_list, directories)