from django.db import models
from account.models import User
from django.utils import timezone
from django.db.models.deletion import CASCADE
from django.core.validators import RegexValidator
from taggit.managers import TaggableManager
from datetime import datetime

# 1. Space      (fk- User<Host>)
# 2. Review    (fk- Space, User)
# 3. Question  (fk- Space, User)
# 4. Answer     (fk- Question, User<Host>)
# 4. Booking    (fk- Space, User)

class Space(models.Model):
    # space_id
    host_id = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True)
    space_name = models.CharField(max_length=30)
    SPACE_TYPE_CHOICES = [
        ('STUDY', '스터디룸'),
        ('STUDIO', '촬영스튜디오'),
        ('CAFE', '카페 단체석'),
        ('RESTAURANT', '음식점 단체석'),
        ('MEETING', '회의실'),
        ('ETC', '기타')
    ]
    space_type = models.CharField(
        max_length=10,
        choices=SPACE_TYPE_CHOICES,
        default='STUDY'
    )
    contactNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})')
    contact_number = models.CharField(validators = [contactNumberRegex], max_length = 11, unique = True)
    price = models.IntegerField() # 시간당 가격
    space_brief_detail = models.CharField(max_length=200)
    space_detail = models.TextField()
    tags = TaggableManager(blank=True)
    address = models.CharField(max_length=200, default='')
    url = models.URLField()
    space_likes = models.IntegerField(default=0)
    space_image = models.ImageField(upload_to="space/", blank=True, null=True)

    
    def __str__(self):
        return self.space_name


class Booking(models.Model):
    # booking_id
    space_id = models.ForeignKey(Space, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True)
    booker_name = models.CharField(max_length = 50, default='')
    phoneNumberRegex = RegexValidator(regex = r'^01([0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})')
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 11, unique = True)
    num_of_people = models.IntegerField()
    num_of_vaccinated = models.IntegerField()
    booking_date = models.DateField()
    booking_start = models.TimeField()
    booking_end = models.TimeField()
    
    def __str__(self):
        return self.booker_name
    
    def hour(self):
        h = self.booking_end.hour - self.booking_start.hour
        return h
    
    def time(self):
        h = self.booking_end.hour - self.booking_start.hour
        m = self.booking_end.minute - self.booking_start.minute
        return h*60 + m
    
    def payment(self):
        return int(self.time()/6) * self.space_id.price
    
class Review(models.Model):
    # review_id
    space_id = models.ForeignKey(Space, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True)
    review_content = models.TextField()
    RATING_TYPE_CHOICES = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5)       
    ]
    review_star = models.CharField(
        max_length = 5,
        choices = RATING_TYPE_CHOICES,
        default = '1'
    )
    
    def __str__(self):
        return self.review_content
    
    def time(self):
        return int((self.booking_end - self.booking_start).seconds / 60)
    
class Question(models.Model):
    # question_id
    space_id = models.ForeignKey(Space, on_delete=models.CASCADE, null=True)
    writer = models.CharField(max_length=50, default='')
    question_content = models.TextField()
    
    def __str__(self):
        return self.question_content


class Answer(models.Model):
    # answer_id
    question_id =models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey('account.User', on_delete=models.CASCADE, null=True) # space의 host_id
    answer_content = models.TextField()
    
    def __str__(self):
        return self.answer_content