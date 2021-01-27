"""
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py shell
"""
#Inshell:
# Подключаем модели
from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment

# Создать двух пользователей (с помощью метода User.objects.create_user). Создадим 4-х пользвателей
User.objects.create_user(username='Alex')
User.objects.create_user(username='Boris')
User.objects.create_user(username='Cate')
User.objects.create_user(username='Diana')

# Создать два объекта модели Author, связанные с пользователями.
Author.objects.create(username=User.objects.get(username = 'Alex'),name = 'Alex')
Author.objects.create(username=User.objects.get(username = 'Boris'),name = 'Boris')

# Добавить 4 категории в модель Category.
Category.objects.create(name='Экономика')
Category.objects.create(name='Спорт')
Category.objects.create(name='Наука')
Category.objects.create(name='Политика')

# Добавить 2 статьи и 1 новость.
Post.objects.create(type='AR', author=Author.objects.get(name='Alex'), header='Экологичная конверсия', text= 'Российским учёным удалось увеличить эффективность сжигания угля и на 40% снизить выбросы угарного газа при его сгорании. Исследователи установили, что использование определённых солей металлов в качестве катализаторов позволяет в три раза уменьшить объём несгоревшего остатка при сжигании угля и увеличить количество выделяемого полезного тепла. Также специалисты отметили, что процесс горения благодаря применению добавок стал более управляемым.')
Post.objects.create(type='AR', author=Author.objects.get(name='Boris'), header='Год со дня гибели легенды НБА', text='26 января 2020 года авиакатастрофа унесла жизнь Коби Брайанта. В результате крушения частного вертолёта погибли восемь человек, включая самого баскетболиста, его друзей, а также 13-летнюю дочь Джианну. Дома атлета, которому шёл 42-й год, ждали жена Ванесса и трое детей. О наследии легенды НБА — в материале RT.')
Post.objects.create(author=Author.objects.get(name='Boris'), header='Денежное первенство: Китай обошёл США', text='В понедельник, 25 января, показатели фондового рынка Китая выросли до максимальных значений с 2015 года. Участники рынка позитивно восприняли информацию о том, что республика обошла США по уровню прямых иностранных инвестиций (ПИИ). По оценкам ООН, в 2020 году зарубежные инвесторы вложили в китайские предприятия $163 млрд, а в американские — $134 млрд.')

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
# Добавим категорию для статьи ID:1

# Вариант 1:
post = Post.objects.get(pk=1)
category = Category.objects.get(name='Наука')
post.category.add(category)

# или Вариант 2:
Post.objects.get(pk=1).category.add(Category.objects.get(name='Политика'))

# Удалим, ибо ошиблись
PostCategory.objects.filter(pk=1).delete() #Удаление записи с нужным ID

# Снова добавим категорию для статьи ID:1
Post.objects.get(pk=1).category.add(Category.objects.get(name='Политика'))

# Добавим категорию для статьи ID:2
Post.objects.get(pk=2).category.add(Category.objects.get(name='Спорт'))

# И добавим категории в новость (ID:3)
Post.objects.get(pk=3).category.add(Category.objects.get(name='Экономика'))
Post.objects.get(pk=3).category.add(Category.objects.get(name='Политика'))

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
Comment.objects.create(post=Post.objects.get(pk=1), user=User.objects.get(username='Cate'), text='Отличная научная статейка, пишите еще.')
Comment.objects.create(post=Post.objects.get(pk=2), user=User.objects.get(username='Diana'), text='Жалко парня, но жизнь есть жизнь.')
Comment.objects.create(post=Post.objects.get(pk=3), user=User.objects.get(username='Cate'), text='Китайцы молодцы! Через пару лет порвут США как тузик грелку.')
Comment.objects.create(post=Post.objects.get(pk=3), user=User.objects.get(username='Alex'), text='Мне, как гражданину США, больно читать комментарии предыдущего оратора.')

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).dislike()
Comment.objects.get(pk=1).like()

# Обновить рейтинги пользователей
for authors in Author.objects.all():
    Author.objects.get(name=authors.name).update_rating()

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
Author.objects.all().order_by('-rating').values('name', 'rating')

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
Post.objects.all().order_by('-rating').values('create_date', 'author__name', 'rating','header')[0]
Post.objects.all().order_by('-rating').preview()

# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
Comment.objects.filter(post=Post.objects.all().order_by('-rating')[0]).values('create_time', 'user__username', 'rating', 'text')
