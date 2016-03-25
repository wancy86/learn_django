
#test code in: python manage.py shell
from polls.models import Question, Choice
Question.objects.all()

from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
q.question_text
q.pub_date
q.question_text = "What's up?"
q.save()
Question.objects.all()


#create admin user
#name: admin
#pwd: admin123
python manage.py createsuperuser

#commands
# python manage.py migrate
# python manage.py shell
# python manage.py runserver



