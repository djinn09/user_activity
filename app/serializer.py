from rest_framework import serializers
from app.models import Users, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%b %d %Y %H:%M%p")
    end_time = serializers.DateTimeField(format="%b %d %Y %H:%M%p")

    class Meta:
        model = ActivityPeriod
        fields = (
            "start_time",
            "end_time",
        )


class UserActivitySerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(
        many=True, read_only=True, source="user_activity"
    )

    class Meta:
        model = Users
        fields = ("id", "real_name", "tz", "activity_periods")

