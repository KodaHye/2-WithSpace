from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# from taggit.managers import 

# 메인 페이지
def main(request):
    spaces=Space.objects.all()
    return render(request, 'main.html', {'spaces':spaces})

# 공간 운영자의 공간 등록 페이지 렌더링
def register_space(request):
    return render(request, 'register_space.html')

# 새로운 공간 등록 페이지 - 데이터 POST
def register(request):
    if request.method == "POST":
        new_space = Space()
        new_space.space_name = request.POST['space_name']
        new_space.space_type = request.POST['space_type']
        new_space.contact_number = request.POST['contact_number']
        new_space.price = request.POST['price']
        new_space.space_brief_detail = request.POST['space_brief_detail']
        new_space.space_detail = request.POST['space_detail']
        # new_space.tags = 
        new_space.address = request.POST['address']
        new_space.url = request.POST['url']
        new_space.space_likes = request.POST['space_likes']
        new_space.space_image = request.FILES['space_image']
        
        host_id = request.user.id
        user = User.objects.get(id=host_id)
        new_space.save()
        return redirect('main')
    else:
        return reneder(request, 'register_space.html')
        
'''
    contact_number = models.CharField(validators = [contactNumberRegex], max_length = 16, unique = True)
    price = models.IntegerField() # 시간당 가격
    space_brief_detail = models.CharField(max_length=200)
    space_detail = models.TextField()
    # tags
    address = models.charField(max_length=200, default='')
    url = models.URLField() # form widget = URLInput
    space_likes = models.IntegerField(default=0)
    space_image = models.ImageField(blank=True, null=True)
'''

# 공간 검색 페이지
def search_space(request):
    return render(request, 'search_space.html')

# 공간 검색 결과 페이지 (검색 필터링 구현 후 리다이렉팅으로 변경)
def search_result(request):
    return render(request, 'search_result.html')

# 공간 디테일 페이지 (공간 pk=id 값으로 페이지 렌더링)
def space(request):
    return render(request, 'space.html')

# 예약자의 공간 예약 페이지
def booker_booking(request):
    return render(request, 'booker_booking.html')

# 예약자의 공간 예약 리스트 페이지 (마이페이지 연동)
def booker_booking_list(request):
    return render(request, 'booker_booking_list.html')

# 공간 운영자의 공간에 대한 예약 리스트 페이지
def host_booking_list(request):
    return render(request, 'host_booking_list.html')

# 결제 페이지
def payment(request):
    return render(request, 'payment.html')
