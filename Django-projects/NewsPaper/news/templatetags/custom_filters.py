from django import template

register = template.Library()  # если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать и фильтры потеряются(


@register.filter(name='censor') # регестрируем наш фильтр под именем censor, чтоб django понимал, что это именно фильтр, а не простая функция
def censor(value): # Используем как value|censor
    if isinstance(value, str):
        string = value
        words = ['хуй', 'пизда']
        cens_word = 'Джигурда'
        for word in words:
            string = str.replace(string, word, cens_word)
        return string
    else:
        raise ValueError(f'искомое поле - не текст') # в случае если кто-то неправильно воспользовался нашим тегом, это будет ошибкой