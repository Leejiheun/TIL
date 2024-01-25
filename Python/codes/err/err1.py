try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자 넣어줘')
except ZeroDivisionError:
    print('0으로 나누기가 될 거 같아?')
except:
    print( '알 수 없는 에러가 발생 했음')

# try:
#     num = int(input('100으로 나눌 값을 입력하시오 : '))
# except (ValueError, ZeroDivisionError):
#     print('에러 발생')
# except:
#     print( '알 수 없는 에러가 발생 했음')
    
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except BaseException: # 상위 클래스가 나오면 상위에서 다 걸려버림 # 하위부터 작성하기!
    print('숫자 넣어줘')
except ZeroDivisionError:
    print('0으로 나누기가 될 거 같아?')
except:
    print( '알 수 없는 에러가 발생 했음')
