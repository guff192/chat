from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import truncatewords


class Message(models.Model):
    text = models.TextField(max_length=1000, help_text='Message text')
    sent_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, help_text='Date and time at which the message was sent')

    @property
    def shortened(self):
        return truncatewords(self.text, 40)

    class Meta:
        ordering = ['created', 'sent_by']
