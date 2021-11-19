from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Q

"""
Main Page
"""
def main(request):
    spaces = Space.objects.all()
    return render(request, 'main.html', {'spaces': spaces})


"""
Space Model
"""
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
        new_space.host_id = User.objects.get(id=host_id)
        new_space.save()
        
        tags = request.POST.get('tags', '').split(',')
        for tag in tags:
            tag = tag.strip()
            new_space.tags.add(tag)
        return redirect('main')
    else:
        return render(request, 'register.html')


# 공간 검색 페이지
def search_space(request):
    if request.method == 'POST':
        keyword = request.POST.get('search_button') # keyword를 입력받음
        
        hashtag_q = Q(tags__icontains = keyword)
        space_name_q = Q(space_name__icontains = keyword)
        space_type_q = Q(space_type__icontains = keyword)
        address_q = Q(address__icontains = keyword)
        detail_q = Q(space_detail__icontains = keyword)
        
        space = Space.objects.filter(address_q | space_name_q | space_type_q | detail_q)

        return render(request, 'search_result.html', {'space':space, 'keyword':keyword})
    elif request.method == 'GET':
        return redirect('/')

    
# 공간 검색 결과 페이지 (검색 필터링 구현 후 리다이렉팅으로 변경)
def search_result(request):
    return render(request, 'search_result.html')

def search(request):
    return render(request, 'search_space.html')

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
    return render(request, 'booking_page.html', {'space': space})


"""
Review Model
"""
# 리뷰 생성
def create_review(request, space_id):
    if request.method == 'POST':
        review = Review()
        review.space_id = get_object_or_404(Space, pk=space_id)
        
        user_id = request.user.id
        review.user_id = User.objects.get(id=user_id)
        review.review_content = request.POST['review_content']
        review.review_star = request.POST['review_star']
        review.save()
        return redirect('space', space_id)


# 리뷰 삭제
def delete_review(request, space_id, review_id):
    my_review = Review.objects.get(pk=review_id)
    my_review.delete()
    return redirect('space', space_id)


"""
Question Model
"""
# 질문 생성
def create_question(request, id):
    space_id = id
    if request.method == 'POST':
        question = Question()
        question.space_id = get_object_or_404(Space, pk=space_id)
        question.writer = request.POST['writer']
        question.question_content = request.POST['question_content']
        question.save()
        return redirect('space', space_id)
    

"""
Answer Model
"""
# 질문에 대한 답변 달기
def create_answer(request, space_id, question_id):
    if request.method == 'POST':
        answer = Answer()
        answer.space_id = get_object_or_404(Space, pk=space_id)
        answer.question_id = get_object_or_404(Question, pk=question_id)
        answer.answer_content = request.POST['answer_content']
        answer.save()
        return redirect('space', space_id)


"""
Booking Model
"""
# 새로운 예약 생성
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
        new_booking.booking_start = request.POST.get('booking_start')
        new_booking.booking_end = request.POST.get('booking_end')
        
        user_id = request.user.id
        new_booking.user_id = User.objects.get(id=user_id)
        new_booking.save()
        return redirect('booker_booking_list')
    else:
        return render(request, 'booking_page.html', {'space':space, 'space_id':space_id})
    

# 예약자의 공간 예약 리스트 페이지 (마이페이지 연동)
def booker_booking_list(request):
    book = Booking.objects.all()
    return render(request, 'booker_booking_list.html', {'book':book})


# 공간 운영자의 공간에 대한 예약 리스트 페이지
def host_booking_list(request):
    space = Space.objects.all()
    book = Booking.objects.all()
    return render(request, 'host_booking_list.html', {'book':book, 'space':space})


# 결제 페이지
def payment(request):
    return render(request, 'payment.html')