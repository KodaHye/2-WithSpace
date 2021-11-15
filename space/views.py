from django.shortcuts import render, redirect, get_object_or_404
from .models import *

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
        new_space.address = request.POST['address']
        new_space.url = request.POST['url']
        new_space.space_image = request.FILES.get('space_image')
        
        host_id = request.user.id
        user = User.objects.get(id=host_id)
        new_space.save()
        
        tags = request.POST.get('tags', '').split(',')
        for tag in tags:
            tag = tag.strip()
            new_space.tags.add(tag)
        return redirect('main')
    else:
        return render(request, 'register_space.html')


# 공간 검색 페이지
def search_space(request):
    return render(request, 'search_space.html')

# 공간 검색 결과 페이지 (검색 필터링 구현 후 리다이렉팅으로 변경)
def search_result(request):
    return render(request, 'search_result.html')

# 공간 디테일 페이지 (공간 pk=id 값으로 페이지 렌더링)
def space(request, id):
    if request.method == 'POST':
        pk = request.POST.get('pk', None)
        space = get_object_or_404(Space, pk=pk)
    else:
        space = get_object_or_404(Space, pk=id)
        space_id = id
        return render(request, 'space.html', {'space':space, 'space_id':space_id})

# 예약자의 공간 예약 페이지
def booker_booking(request, id):
    space_id = id
    space = get_object_or_404(Space, pk=space_id)
    # return render(request, 'booking_page.html', {'space:':space, 'space_id':space_id})
    return render(request, 'booking_page.html', {'space': space})

def book(request, id):
    space_id = id
    space = get_object_or_404(Space, pk = space_id)
    if request.method == "POST":
        new_booking = Booking()
        new_booking.space_id = space
        new_booking.booker_name = request.POST['booker_name']
        new_booking.phoneNumber = request.POST['phoneNumber']
        new_booking.num_of_people = request.POST['num_of_people']
        new_booking.num_of_vaccinated = request.POST['num_of_vaccinated']
        new_booking.booking_date = request.POST['booking_date']
        
        # user_id = request.user.id
        # user = User.objects.get(id=user_id)
        new_booking.save()
        return redirect('booker_booking_list')
    else:
        return render(request, 'booking_page.html', {'space':space, 'space_id':space_id})
    
# 예약자의 공간 예약 리스트 페이지 (마이페이지 연동)
def booker_booking_list(request):
    book=Booking.objects.all()
    return render(request, 'booker_booking_list.html', {'book':book})

# 공간 운영자의 공간에 대한 예약 리스트 페이지
def host_booking_list(request):
    return render(request, 'host_booking_list.html')

# 결제 페이지
def payment(request):
    return render(request, 'payment.html')
