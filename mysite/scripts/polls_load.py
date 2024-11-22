import csv 

import datetime
from django.utils import timezone

from polls.models import Question, Choice

def run():
    print("=== Polls Loader")

    Choice.objects.all().delete()
    Question.objects.all().delete()
    print("=== Objects deleted")

    fhand = open('scripts/dj4e_batch.csv')
    reader = csv.reader(fhand)
    next(reader)

    for row in reader:

        q = Question(question_text=row[0], pub_date=timezone.now())
        q.save()

        for data in row[1:]:
            c = Choice(question = q, choice_text = data)
            c.save()

    print("=== Load Complete")
