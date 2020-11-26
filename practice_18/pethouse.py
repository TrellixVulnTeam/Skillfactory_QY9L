from petclass import Cat

cats = []
cats.append(("Сэм","Мальчик",2))
cats.append(("Барон","Мальчик",2))
for cat_name,cat_sex,cat_age in cats:
    cat_ex=Cat(cat_name,cat_sex,cat_age)
#    print(5 * "-","Вывод данных кота {0} через аргументы дочернего(Cat)".format(cat_ex.name),5 * "-")
    print("Кот {0}, {1}, возраст {2}".format(cat_ex.name,cat_ex.sex,cat_ex.age))
#    print(5*"-","Вывод данных кота {0} через метод fullData дочернего класса (Cat)".format(cat_ex.name),5 * "-")
#    cat_ex.fullData()
#    print(5 * "-","Вывод данных кота {0} через метод getData унаследованный от родительского класса (Pet)".format(cat_ex.name),5 * "-")
#    cat_ex.getData()
 #   print(30*"=")
