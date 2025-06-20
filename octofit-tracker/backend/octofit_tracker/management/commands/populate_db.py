from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
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

        # Test data
        test_users = [
            {"email": "alice@example.com", "name": "Alice", "password": "password1"},
            {"email": "bob@example.com", "name": "Bob", "password": "password2"},
            {"email": "carol@example.com", "name": "Carol", "password": "password3"},
        ]
        test_teams = [
            {"name": "Team Alpha"},
            {"name": "Team Beta"},
        ]
        test_activities = [
            {"user_email": "alice@example.com", "activity_type": "Running", "duration": 30, "date": timezone.now()},
            {"user_email": "bob@example.com", "activity_type": "Cycling", "duration": 45, "date": timezone.now()},
            {"user_email": "carol@example.com", "activity_type": "Swimming", "duration": 60, "date": timezone.now()},
        ]
        test_leaderboard = [
            {"user_email": "alice@example.com", "score": 100},
            {"user_email": "bob@example.com", "score": 80},
            {"user_email": "carol@example.com", "score": 120},
        ]
        test_workouts = [
            {"name": "Pushups", "description": "Do 20 pushups"},
            {"name": "Situps", "description": "Do 30 situps"},
            {"name": "Jumping Jacks", "description": "Do 50 jumping jacks"},
        ]

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
