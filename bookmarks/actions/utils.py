from django.contrib.contenttypes.models import ContentType
import datetime
from django.utils import timezone
from .models import Action


def create_action(user, verb , target=None):

    #
    now = timezone.now()
    last_mintue = now - datetime.timedelta(seconds=60)
    similiar_actions = Action.objects.filter(user_id=user.id, verb=verb, created_gte=last_mintue)

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similiar_actions = similiar_actions.filter(target_ct=target_ct, target_id=target.id)


    if not similiar_actions:

        new_action = Action(user=user, verb=verb , target=target)
        new_action.save()
        return True

    return False