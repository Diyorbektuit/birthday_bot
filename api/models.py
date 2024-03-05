from django.db import models

# Create your models here.


class AdminGroup(models.Model):
    name = models.CharField(max_length=123)
    username = models.CharField(max_length=123, null=True)
    tg_id = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Group(models.Model):
    admin = models.ForeignKey(AdminGroup, related_name='group_admin', on_delete=models.CASCADE)
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Position(models.Model):
    admin = models.ForeignKey(AdminGroup, related_name='position_admin', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='group_positions', on_delete=models.CASCADE)
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class BotUser(models.Model):
    admin = models.ForeignKey(AdminGroup, related_name='bot_users_admin', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='bot_users_group', on_delete=models.CASCADE)
    position = models.ForeignKey(Position, related_name='bot_users_position', on_delete=models.CASCADE)
    tg_id = models.CharField(max_length=15)
    first_name = models.CharField(max_length=123)
    last_name = models.CharField(max_length=123)
    username = models.CharField(max_length=123, null=True)
    birthday = models.DateField()

    def __str__(self):
        return self.first_name

