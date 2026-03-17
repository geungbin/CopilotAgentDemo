from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    def handle(self, *args, **options):
        # 데이터 삭제
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # 팀 생성
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # 유저 생성
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel)
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team=dc)

        # 활동 생성
        Activity.objects.create(user=ironman, type='run', duration=30)
        Activity.objects.create(user=batman, type='cycle', duration=45)

        # 리더보드 생성
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=batman, score=90)

        # 운동 생성
        Workout.objects.create(name='Push Up', description='Upper body', difficulty='Easy')
        Workout.objects.create(name='Squat', description='Lower body', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('테스트 데이터가 성공적으로 입력되었습니다.'))
