from django.db import models


class Admin(models.Model):
    admin_id = models.IntegerField(primary_key=True, help_text="ID администратора")
    email = models.EmailField(unique=True, help_text="Электронная почта администратора")
    password = models.CharField(max_length=500, help_text="Пароль администратора")

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"


class Answer(models.Model):
    qid = models.TextField(help_text="ID вопроса")
    ansid = models.TextField(help_text="ID ответа")

    def __str__(self) -> str:
        return self.qid

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"


class Feedback(models.Model):
    id = models.TextField(primary_key=True, help_text="Уникальный идентификатор отзыва")
    name = models.CharField(max_length=50, help_text="Имя отправителя отзыва")
    email = models.EmailField(help_text="Электронная почта отправителя отзыва")
    subject = models.CharField(max_length=500, help_text="Тема отзыва")
    feedback = models.CharField(max_length=500, help_text="Содержание отзыва")
    date = models.DateField(help_text="Дата отзыва")
    time = models.CharField(max_length=50, help_text="Время отзыва")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Обратная"
        verbose_name_plural = "Обратная"


class History(models.Model):
    email = models.EmailField(help_text="Электронная почта пользователя")
    eid = models.TextField(help_text="ID мероприятия")
    score = models.IntegerField(help_text="Баллы")
    level = models.IntegerField(help_text="Уровень")
    sahi = models.IntegerField(help_text="Правильные ответы")
    wrong = models.IntegerField(help_text="Неправильные ответы")
    date = models.DateTimeField(auto_now=True, help_text="Дата сохранения записи")

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "Истории"


class Options(models.Model):
    qid = models.CharField(max_length=50, help_text="ID вопроса")
    option = models.CharField(max_length=5000, help_text="Вариант ответа")
    optionid = models.TextField(help_text="ID варианта ответа")

    def __str__(self) -> str:
        return self.qid

    class Meta:
        verbose_name = "Опция"
        verbose_name_plural = "Опции"


class Questions(models.Model):
    eid = models.TextField(help_text="ID мероприятия")
    qid = models.TextField(help_text="ID вопроса")
    qns = models.TextField(help_text="Текст вопроса")
    choice = models.IntegerField(help_text="Выбор")
    sn = models.IntegerField(help_text="Порядковый номер")

    def __str__(self) -> str:
        return self.eid

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Quiz(models.Model):
    eid = models.TextField(help_text="ID мероприятия")
    title = models.CharField(max_length=100, help_text="Заголовок викторины")
    correct = models.IntegerField(help_text="Количество правильных ответов")
    wrong = models.IntegerField(help_text="Количество неправильных ответов")
    total = models.IntegerField(help_text="Общее количество вопросов")
    time = models.BigIntegerField(help_text="Время")
    intro = models.TextField(help_text="Вступление")
    tag = models.CharField(max_length=100, help_text="Тег")
    date = models.DateTimeField(auto_now=True, help_text="Дата сохранения записи")

    def __str__(self) -> str:
        return self.eid

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class Rank(models.Model):
    email = models.EmailField(help_text="Электронная почта пользователя")
    score = models.IntegerField(help_text="Баллы")
    time = models.DateTimeField(auto_now=True, help_text="Дата сохранения записи")

    def __str__(self) -> str:
        return self.email

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class User(models.Model):
    name = models.CharField(max_length=50, help_text="Имя пользователя")
    email = models.EmailField(
        primary_key=True, help_text="Электронная почта пользователя"
    )
    password = models.CharField(max_length=50, help_text="Пароль пользователя")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
