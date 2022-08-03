class SuperStr(str):
    def __init__(self, s=''):
        self.s = s

    def is_repeatance(s):
        if s == input('Line s - ').lower() in input('Enter a line - ').lower():
            print(True)
        else:
            print(False)

    def is_palindrom(self):
        s = input('Enter a line - ').lower()
        if s == s[::-1]:
            print(True)
        else:
            print(False)


SuperStr(input('Enter a line - ').lower()).is_repeatance()
SuperStr().is_palindrom()
