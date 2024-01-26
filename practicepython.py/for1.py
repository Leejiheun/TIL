# # 131
# 과일 = ["사과", "귤", "수박"]
# for 변수 in 과일:
#     print(변수)
# '''
# 사과
# 귤
# 수박
# '''

# # 132
# fru = ["사과", "귤", "수박"]

# for 변수 in fru:
#     print("#####")
# '''
# #####
# #####
# #####
# '''

# # 133
# for i in ["A", "B", "C"]:
#     print(i)

# print("A")
# print("B")
# print("C")

# # 134
# for i in ["A", "B", "C"]:
#   print("출력:", i)

# 출력: A
# 출력: B
# 출력: C

# print("출력 : A")
# print("출력 : B")
# print("출력 : C")

# 135
# for i in ["A", "B", "C"]:
#   b = i.lower()
#   print("변환:", b)

# print("변환: a")
# print("변환: b")
# print("변환: c")

# # 136
# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)

# for i in [10,20,30]:
#   print(i)

# #137
# print(10)
# print(20)
# print(30)

# 138
# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")

# for i in [10,20,30]:
#     print(i)
#     print("-------")

# 139
# print("++++")
# print(10)
# print(20)
# print(30)

# print("++++")
# for i in [10,20,30]:
#     print(i)

# 141
# a = [100, 200, 300]
# 110
# 210
# 310
# for i in a:
#     print(i + 10)

# 142
# a = ["김밥", "라면", "튀김"]
# # 오늘의 메뉴: 김밥
# # 오늘의 메뉴: 라면
# # 오늘의 메뉴: 튀김

# for i in a:
#     print("오늘의 메뉴:", i)

# 143
# list = ["SK하이닉스", "삼성전자", "LG전자"]
# for i in list:
#     print(len(i))

# 144
# list = ['dog', 'cat', 'parrot']
# # dog 3
# # cat 3
# # parrot 6
# for i in list:
#     print(i, len(i))

# 145
# list = [1, 2, 3]
# # 3 x 1
# # 3 x 2
# # 3 x 3
# for i in list:
#     print('3 x', i)

# # 147
# list = [1, 2, 3]
# # 3 x 1 = 3
# # 3 x 2 = 6
# # 3 x 3 = 9
# for i in list:
#     print('3 x', i, '=', 3*i)

# 148
# list = ["가", "나", "다", "라"]
# # 나
# # 다
# # 라
# list2 = list[1:]
# for i in list2:
#     print(i)

# 151
# list = [3, -20, -3, 44]
# for i in list:
#     if i < 0:
#         print(i)

# 152
# list = [3, 100, 23, 44]
# for i in list:
#     if i % 3 == 0:
#         print(i)

# 153
# list = [13, 21, 12, 14, 30, 18]
# for i in list:
#     if i < 20 and i % 3 == 0:
#         print(i)

# 154
# list = ["I", "study", "python", "language", "!"]
# for i in list:
#     if len(i) >= 3:
#         print(i)

# # 155
# list = ["A", "b", "c", "D"]
# for i in list:
#     if i.isupper():
#         print(i)

# 156
# list = ["A", "b", "c", "D"]
# for i in list:
#     if i.islower():
#         print(i)

# 157
# list = ['dog', 'cat', 'parrot']
# for i in list :
#     print(i[0].upper()+i[1:])

# 158
# list = ['hello.py', 'ex01.py', 'intro.hwp']
# for i in list:
#     print(i.split('.')[0])

#159
# list = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in list:
#     if i.split('.')[-1] == 'h':
#         print(i)

# 160
# list = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in list:
#     if i.split('.')[-1] == 'h' or i.split('.')[-1] == 'c':
#         print(i)

# 161
# for i in range(100):
#     print(i)

# 162
# for i in range(2002, 2051, 4):
#     print(i)

# 163
# for i in range(1,31):
#     if i % 3 == 0:
#         print(i)

# # 164
# for i in range(100):
#     print(99 - i)

# # 165
# for i in range(10):
#     print(i/10)

# 166
# for i in range(1,10):
#     print(f'3x{i} = {3*i}')

# # 167
# for i in range(1,10,2):
#     print(f'3x{i} = {3*i}')

# 168
nums = 0
for i in range(1,11):
    nums += i
print(nums)

# # 169
# nums = 0
# for i in range(1,11,2):
#     nums += i
# print(nums)

# 170
# num = 1
# for i in range(1,11):
#     num *= i
# print(num)

# 171
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

# 172
price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(f'{i} {price_list[i]}')
for i, data in enumerate(price_list):
    print(i, data)

# 173
price_list = [32100, 32150, 32000, 32500]

# 174
# price_list = [32100, 32150, 32000, 32500]
# for i in range(1,4):
#     print(100+(i-1)*10,price_list[i])

#175
# my_list = ["가", "나", "다", "라"]
# for i in range(1,4):
#     print(my_list[i-1], my_list[i])

# 176
# my_list = ["가", "나", "다", "라", "마"]
# for i in range(3,6):
#     print(my_list[i-3], my_list[i-2], my_list[i-1])

# 177
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1):
    print(my_list[len(my_list)-(i+1)],my_list[len(my_list)-(i+2)])

# 178
my_list = [100, 200, 400, 800]

# # 179
# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(3,7):
#     print((my_list[i-3]+my_list[i-2]+my_list[i-1])/3)

# 180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(5):
    volatility.append(high_prices[i]-low_prices[i])
print(volatility)


# 182
# stock = [['시가',100,200,300],['종가',80,210,330]]

# # 183
# value = {'시가':[100, 200, 300],'종가':[80,210,330]}

# # 184
# stock = {'10/10':[80,110,70,90],'10/11':[210,230,190,200]}

#185
apart = [ [101, 102], [201, 202], [301, 302] ]
for x in apart:
    for y in x:
        print(y,'호')

#186
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i:
        print(j,'호')

# # 187
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart[::-1]:
#     for j in i[::-1]:
#         print(j,'호')

# 188
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(f'{j} 호\n-----')

# 189
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j,'호')
    print('-----')
# 190
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in apart:
#     for j in i:
#         print(j,'호')
# print('-----')
    
# 191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
# for i in data:
#     for j in i:
#         print(j + j * 0.00014)

for line in data:
    for column in line:
        print(column * 1.00014)

# 192
for line in data:
    for column in line:
        print(column * 1.00014)
    print('-----')
# **194 **
resulte = []
for line in data:
    sub = []
    for column in line:
        sub.append(column * 1.00014)

# 194
        
# 197
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
# for i in range(1,4):
#     if ohlc[i][3]>150:
#         print(ohlc[i][3])

# 197
# for i in range(1,4):
#     if ohlc[i][0] <= ohlc[i][3]:
#         print(ohlc[i][3])

# 198
volatility = []
for i in ohlc[1:]:
    volatility.append(i[1]-i[2])
print(volatility)

# 199
# for i in ohlc[1:]:
#     if i[3] > i[0]:
#         print(i[1]-i[2])

# 200
# bene = 0
# for i in ohlc[1:]:
#     bene += i[3]-i[0]
# print(bene)

# # 201
# def print_coin():
#     print("비크코인")

# # 202
# print_coin()

# # 203
# for i in range(100):
#     print_coin()

# 204
def print_coin():
    for i in range(100):
        print("비트코인")
# print_coin()

# 215
def print_with_smile(str):
    print(str + ':D')

# # 215
# def print_with_smile(str):
#     print(str + ':D')

# print_with_smile('안녕하세요')
    
# 217
def print_upper_price(price):
    print(price * 0.3)

# 218
def print_sum(x,y):
    print(x+y)

#219
def print_arithmetic_operation(x, y):
    print(f'{x} + {y} = {x+y}')
    print(f'{x} - {y} = {x-y}')
    print(f'{x} * {y} = {x*y}')
    print(f'{x} / {y} = {x/y}')

# 220
# def print_max(x,y,z):
#     if x > y:
#         if x > z:
#             print(x)
#         else:
#             print(z)
#     elif y > z:
#         print(y)
#     else:
#         print(z)
# print_max(1,2,3)
# # 220
# def prin_max(a,b,c):
#     max_a = 0
#     if a > max_a:
#         a = max_a
#     if b > max_a:
#         b = max_a
#     if c > max_a:
#         c = max_a
#     print(max_a)
# prin_max(1,2,3)

def print_max(a, b, c) :
    max_val = 0
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    print(max_val)
print_max(1,2,3)

# 221
def print_reverse(i):
    print(i[::-1])
print_reverse('python')

# 222
def print_score(n_list):
    print(sum(n_list)/len(n_list))

# 223
# def print_even(n2_list):
#     for i in len(n2_list):
#         if n2_list[i] % 2 == 0:
#             print(n2_list[i])
# print_even ([1, 3, 2, 10, 12, 11, 15])

#223
def print_even(n2_list):
    for i in n2_list:
        if i % 2 == 0:
            print(i)
print_even ([1, 3, 2, 10, 12, 11, 15])

#224
def print_keys(dic):
    for i in dic.keys():
        print(i)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225
def print_value_by_key(my_dict, ohlc):
    print(my_dict[ohlc])

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

print_value_by_key  (my_dict, "10/26")

# 226
# def print_5xn(string):
#     print(string[:5])
#     print(string[5:10])
# print_5xn("아이엠어보이유알어걸")

#227
def print_mxn(str, i):
    print(str[:i])

# #232
# def make_url(url):
#     print(f'ww.{url}.com')
# make_url("naver")

# 233
def make_list(list):
    new_list = []
    for i in list:
        new_list.append(i)
    print(new_list)

make_list("abcd")

# 234
def pickup_even(list):
    new_list2 = []
    for i in list:
        if i % 2 == 0:
            new_list2.append(i)
    print(new_list2)
pickup_even([3, 4, 5, 6, 7, 8])

# 235
def convert_int():
    
