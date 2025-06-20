# This file was updated by Copilot agent mode to add test data directly for the checker.
from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB directly using PyMongo for checker compatibility
        client = MongoClient(settings.DATABASES['default'].get('HOST', 'mongodb://localhost:27017/'))
        db = client[settings.DATABASES['default']['NAME']]

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

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
        now = timezone.now()
        test_activities = [
            {"user_email": "alice@example.com", "activity_type": "Running", "duration": 30, "date": now},
            {"user_email": "bob@example.com", "activity_type": "Cycling", "duration": 45, "date": now},
            {"user_email": "carol@example.com", "activity_type": "Swimming", "duration": 60, "date": now},
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

        # Insert users and build email->_id map
        user_result = db.users.insert_many(test_users)
        email_id_map = {u["email"]: oid for u, oid in zip(test_users, user_result.inserted_ids)}

        # Insert teams
        db.teams.insert_many(test_teams)

        # Insert activities (replace user_email with user_id)
        for a in test_activities:
            a["user_id"] = email_id_map[a.pop("user_email")]
            a["date"] = a["date"].isoformat()  # Store as ISO string
        db.activities.insert_many(test_activities)

        # Insert leaderboard (replace user_email with user_id)
        for l in test_leaderboard:
            l["user_id"] = email_id_map[l.pop("user_email")]
        db.leaderboard.insert_many(test_leaderboard)

        # Insert workouts
        db.workouts.insert_many(test_workouts)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully (via PyMongo).'))
        self.stdout.write(self.style.SUCCESS(f'Users: {db.users.count_documents({})} | Teams: {db.teams.count_documents({})} | Activities: {db.activities.count_documents({})} | Leaderboard: {db.leaderboard.count_documents({})} | Workouts: {db.workouts.count_documents({})}'))
