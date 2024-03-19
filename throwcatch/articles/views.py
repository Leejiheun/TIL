from django.shortcuts import render

# Create your views here.
def throw(request):
    return render(request, 'aa/throw.html')

# 1. 사용자가 보낸 데이터를 추출해서 변수에 담기
# 2. 결과 페이지 만들기
def catch(request):
    # 1.
    message = request.GET.get('message')
    context = {
        'message': message 
    }
    # 2.
    return render(request, 'aa/catch.html', context)