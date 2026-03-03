from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    # This command creates and populates test data for users, teams, activities, leaderboard, and workouts collections in octofit_db
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        users = db['users']
        teams = db['teams']
        activities = db['activities']
        leaderboard = db['leaderboard']
        workouts = db['workouts']

        # Clear collections
        users.delete_many({})
        teams.delete_many({})
        activities.delete_many({})
        leaderboard.delete_many({})
        workouts.delete_many({})

        # Ensure unique index on email
        users.create_index("email", unique=True)

        # Sample teams
        marvel = {"name": "Marvel", "members": ["Iron Man", "Captain America", "Thor", "Hulk"]}
        dc = {"name": "DC", "members": ["Superman", "Batman", "Wonder Woman", "Flash"]}
        teams.insert_many([marvel, dc])

        # Sample users
        user_data = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Thor", "email": "thor@marvel.com", "team": "Marvel"},
            {"name": "Hulk", "email": "hulk@marvel.com", "team": "Marvel"},
            {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Flash", "email": "flash@dc.com", "team": "DC"},
        ]
        users.insert_many(user_data)

        # Sample activities
        activities.insert_many([
            {"user": "Iron Man", "activity": "Running", "duration": 30},
            {"user": "Batman", "activity": "Cycling", "duration": 45},
            {"user": "Wonder Woman", "activity": "Swimming", "duration": 60},
            {"user": "Manga Maniacs", "activity": "Manga Maniacs", "duration": 0,
             "description": "Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).",
             "schedule": "Tuesdays at 7pm", "max_attendance": 15},
        ])

        # Sample leaderboard
        leaderboard.insert_many([
            {"team": "Marvel", "points": 120},
            {"team": "DC", "points": 110},
        ])

        # Sample workouts
        workouts.insert_many([
            {"user": "Thor", "workout": "Weightlifting", "reps": 100},
            {"user": "Flash", "workout": "Sprinting", "distance": 500},
        ])

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
