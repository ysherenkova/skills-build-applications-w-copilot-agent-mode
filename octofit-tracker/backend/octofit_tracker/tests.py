from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', members=['Iron Man'])
        self.assertEqual(team.name, 'Marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='Test', activity='Running', duration=30)
        self.assertEqual(activity.activity, 'Running')

    def test_create_manga_maniacs_activity(self):
        activity = Activity.objects.create(
            user='Manga Maniacs',
            activity='Manga Maniacs',
            duration=0,
            description='Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).',
            schedule='Tuesdays at 7pm',
            max_attendance=15
        )
        self.assertEqual(activity.activity, 'Manga Maniacs')
        self.assertEqual(activity.schedule, 'Tuesdays at 7pm')
        self.assertEqual(activity.max_attendance, 15)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='Marvel', points=100)
        self.assertEqual(lb.team, 'Marvel')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user='Test', workout='Weightlifting', reps=10)
        self.assertEqual(workout.workout, 'Weightlifting')
