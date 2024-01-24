class Person: # 클래스 메서드
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1
        # Person.add_count()

    # 이 클래스 메서드를 호출하는 class
    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.') # count cls는 모른다. 17째줄에 호출이 된다.
        print(f'인구수는 {Person.count}입니다.')

    @classmethod
    # count를 1 증가 시키는 클래스 메서드
    def add_count(cls):
        cls.count += 1


person1 = Person('iu')
person2 = Person('BTS')
Person.number_of_population()  # 인구수는 2입니다.
