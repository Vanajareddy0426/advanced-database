#import peewee and date module 
import peewee
import datetime

db = peewee.SqliteDatabase('test_schedule.db')   

class ExamSchedule(peewee.Model):

    text = peewee.CharField()       #description about my test schedule 
    created = peewee.DateField(default=datetime.date.today)    #schedule data

    class Meta:

        database = db
        db_table = 'schedule'


ExamSchedule.create_table()

exam1 = ExamSchedule.create(text='\nAdvance database project submission deadline\t',
        created=datetime.date(2022, 5, 11))
exam1.save()

exam2 = ExamSchedule.create(text='Systems Programming final Project submission\t ',
        created=datetime.date(2022, 5, 10))
exam2.save()

exam3 = ExamSchedule.create(text='Machine learning and Deep learning Project submission \t',
        created=datetime.date(2022, 5, 9))
exam3.save()

exam4 = ExamSchedule.create(text='Once exams completed , Book movie tickets and have fun\t',
        created=datetime.date(2022, 5, 12) )
exam4.save()
