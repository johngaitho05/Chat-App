
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Contact(models.Model):
    user = models.ForeignKey(User, related_name="user_contacts",on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Message(models.Model):
    author = models.ForeignKey(User, related_name="user_messages",on_delete=models.DO_NOTHING)
    content = models.TextField()
    timestamp = models.DateTimeField()
    chat_room = models.CharField(max_length=50)

    def __str__(self):
        return self.author.username

    def sliced_content(self):
        return self.content[:40]


class ChatRoom(models.Model):
    name = models.CharField(max_length=50)
    last_message = models.ForeignKey(Message, related_name='chatroom_last_message',
                                     null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)











