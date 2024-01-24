class StringUtils: # 정적 메서드 # 클래스가 호출(클래스메서드, 스태틱메서드)
    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def capitalize_string(string):
        return string.capitalize()


text = 'hello, world'

reversed_text = StringUtils.reverse_string(text)
print(reversed_text)  # dlrow ,olleh

capitalized_text = StringUtils.capitalize_string(text)
print(capitalized_text)  # Hello, world
