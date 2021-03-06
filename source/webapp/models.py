from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=15, verbose_name='Статус')

    def __str__(self): return self.name


class Task_type(models.Model):
    name = models.CharField(max_length=15, verbose_name='Тип')

    def __str__(self): return self.name


class Task(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length= 3000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.PROTECT, verbose_name='Статус')
    type_task = models.ForeignKey('webapp.Task_type', related_name='type', on_delete=models.PROTECT, verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return "{}. {}".format(self.pk, self.summary)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'