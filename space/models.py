from django.db import models
from django.utils import timezone
from django.db.models.deletion import CASCADE
from django.core.validators import RegexValidator

# 1. Space      (fk- User<Host>)
# 2. Review    (fk- Space, User)
# 3. Question  (fk- Space, User)
# 4. Answer     (fk- Question, User<Host>)
# 4. Booking    (fk- Space, User)

class Space(models.Model):
    # space_id
    host_id = models.ForeignKey(user.User, on_delete=models.CASCADE, null=True)
    space_name = models.CharField(max_length=30)
    SPACE_TYPE_CHOICES = [
        (STUDY, '스터디룸'),
        (STUDIO, '촬영스튜디오'),
        (CAFE, '카페 단체석'),
        (RESTAURANT, '음식점 단체석'),
        (MEETING, '회의실'),
        (ETC, '기타')
    ]
    space_type = models.CharField(
        max_length=2,
        choices=SPACE_TYPE_CHOICES,
        default=STUDY
    )
    contactNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    contact_number = models.CharField(validators = [contactNumberRegex], max_length = 16, unique = True)
    price = models.IntegerField() # 시간당 가격
    space_brief_detail = models.CharField(max_length=200)
    space_detail = models.TextField()
    # tags
    address = models.charField(max_length=200, default='')
    url = models.URLField() # form widget = URLInput
    space_likes = models.IntegerField(default=0)
    space_image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.space_name


class Booking(models.Model):
    # booking_id
    space_id = models.ForeignKey(Space, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(user.User, on_delete=models.CASCADE, null=True)
    num_of_people = models.IntegerField()
    num_of_vaccinated = models.IntegerField()
    booking_date = models.DateField()
    # booking_time
    
    def __str__(self):
        return (self.space_id + "/" + self.user_id + "/" + self.num_of_people)
    
    
class Review(models.Model):
    # review_id
    space_id = models.ForeignKey(Space, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(user.User, on_delete=models.CASCADE, null=True)
    review_content = models.textField()
    
    def __str__(self):
        return self.review_content
    
    
class Question(models.Model):
    # question_id
    space_id = models.ForeignKey(Space, on_delete=models.CASCADE, null=True)
    writer = models.charField(max_length=50, default='')
    question_content = models.textField()
    # review_star
    
    def __str__(self):
        return self.question_content
    
    
class Answer(models.Model):
    # answer_id
    quesition_id = models.ForiengKey(Question, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(user.User, on_delete=models.CASCADE, null=True) # space의 host_id
    answer_content = models.textField()
    
    def __str__(self):
        return self.answer_content