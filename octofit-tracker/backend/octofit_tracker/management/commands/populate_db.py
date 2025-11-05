from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel')
        dc = Team.objects.create(name='DC', description='Team DC')

        # Create users (superheroes)
        users = [
            User(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User(name='Captain America', email='cap@marvel.com', team=marvel, is_superhero=True),
            User(name='Thor', email='thor@marvel.com', team=marvel, is_superhero=True),
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User(name='Superman', email='superman@dc.com', team=dc, is_superhero=True),
            User(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User(name='Flash', email='flash@dc.com', team=dc, is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user=users[0], type='Running', duration=30, date='2025-11-05'),
            Activity(user=users[1], type='Cycling', duration=45, date='2025-11-04'),
            Activity(user=users[4], type='Swimming', duration=60, date='2025-11-03'),
            Activity(user=users[5], type='Yoga', duration=20, date='2025-11-02'),
        ]
        Activity.objects.bulk_create(activities)

        # Create workouts
        workout1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        workout2 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio')
        workout1.suggested_for.set([users[0], users[1], users[4]])
        workout2.suggested_for.set([users[2], users[5], users[6]])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, points=120)
        Leaderboard.objects.create(team=dc, points=110)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
