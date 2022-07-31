import time


# x = a[-4:]
# y = a[:4]
# print(x)
# print(y)
#


class Palindrom():
    def __init__(self, text):
        self.text = text
    def go(self):
        index = 1
        while True:
            x = self.text[-index:]
            y = (self.text[:index])[::-1]
            str_len = len(self.text)
            str_len = str_len // 2
            index += 1
            # time.sleep(1)
            if x == y:
                if int(index) > int(str_len):
                    print("It is palindrom")
                    break

            else:
                print("It is no palindrom")
                break



emp1 = Palindrom("тутут")
emp1.go()