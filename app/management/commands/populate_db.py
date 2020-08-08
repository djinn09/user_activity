from faker import Faker
from django.core.management.base import BaseCommand
from app.models import Users, ActivityPeriod
from django.utils import timezone
from datetime import timedelta
import pytz
import random


class Command(BaseCommand):
    args = "<foo bar ...>"
    help = "our help string comes here"

    def _user_activity(self):
        print("Wait,Please wait for Populating data in Db .....")
        fake = Faker()
        timezones = list(pytz.all_timezones_set)
        timezones_length = len(timezones)

        # create 20 users and activity
        for i in range(20):
            real_name = fake.name()
            email = "{name}.{num}@example.com".format(
                name=".".join(real_name.split(" ")), num=i + 1
            )
            rn = random.randint(0, timezones_length - 1)
            tz = timezones[rn]
            user = Users(real_name=real_name, tz=tz, is_active=True, email=email)
            user.save()
            for _ in range(3):
                start_time = timezone.now()
                end_time = start_time + timedelta(minutes=10)
                ActivityPeriod(
                    user=user, start_time=start_time, end_time=end_time,
                ).save()
            print("{} Entry".format(i + 1))
        print("Done Successfully")

    def handle(self, *args, **options):
        self._user_activity()
