from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        user_objs = {}
        for u in test_users:
            user = User.objects.create(**u)
            user_objs[u["email"]] = user

        # Teams
        for t in test_teams:
            Team.objects.create(**t)

        # Activities
        for a in test_activities:
            Activity.objects.create(user=user_objs[a["user_email"]], activity_type=a["activity_type"], duration=a["duration"], date=a["date"])

        # Leaderboard
        for l in test_leaderboard:
            Leaderboard.objects.create(user=user_objs[l["user_email"]], score=l["score"])

        # Workouts
        for w in test_workouts:
            Workout.objects.create(**w)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
        self.stdout.write(self.style.SUCCESS(f'Users: {User.objects.count()} | Teams: {Team.objects.count()} | Activities: {Activity.objects.count()} | Leaderboard: {Leaderboard.objects.count()} | Workouts: {Workout.objects.count()}'))
