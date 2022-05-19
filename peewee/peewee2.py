#import peewee and datetime module 
import peewee
import datetime

db = peewee.SqliteDatabase('test_schedule.db')

class ExamSchedule(peewee.Model):

    text = peewee.CharField()
    created = peewee.DateField(default=datetime.date.today)

    class Meta:

        database = db
        db_table = 'schedule'


schedule = ExamSchedule.select()

for note in schedule:
    print('{} on {}'.format(note.text, note.created))
schedule = ExamSchedule.select()

#if my schedule got change and I want to delete my first schedule 
del_l = ExamSchedule.delete_by_id(1)
print(del_l)
