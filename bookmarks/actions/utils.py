import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action

#define a function to create Actions easily
def create_action(user, verb , target=None):
    #check for any similar action in the last mintue
    now = timezone.now()
    last_mintue = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(user=user, verb= verb , created_gte=last_mintue)

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_ct = target_ct, target_id = target.id)

    if not similar_actions:
        # If there are no similar actions
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False