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

        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='password1')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='password2')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='password3')

        # Teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')

        # Activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date=timezone.now())
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date=timezone.now())
        Activity.objects.create(user=user3, activity_type='Swimming', duration=60, date=timezone.now())

        # Leaderboard
        Leaderboard.objects.create(user=user1, score=100)
        Leaderboard.objects.create(user=user2, score=80)
        Leaderboard.objects.create(user=user3, score=120)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')
        Workout.objects.create(name='Jumping Jacks', description='Do 50 jumping jacks')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
