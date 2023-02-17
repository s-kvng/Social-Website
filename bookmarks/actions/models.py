from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Action(models.Model):

    #NB: Could make it more flexible by using generic relations instead of the foreign key for user
    user = models.ForeignKey('auth.User', related_name='actions', on_delete=models.CASCADE)

    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    #pointer to the models
    # (limit_choices_to=) attribute to limit the number of models it can point to
    target_ct = models.ForeignKey(ContentType,blank=True, null=True, related_name='target_obj', on_delete=models.CASCADE)
    # Stores primary key of related objects
    target_id = models.PositiveIntegerField(blank=True,null=True)

    target = GenericForeignKey('target_ct', 'target_id')


    class Meta:

        indexes =[
            models.Index(fields=['-created']),
            models.Index(fields=['target_ct' , 'target_id']),
        ]

        ordering = ['created']
