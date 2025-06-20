# Test data for OctoFit Tracker
from django.utils import timezone

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
