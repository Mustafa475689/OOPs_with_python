# Decorater
class Animal:
    @property # ye decorater obj ko call jiye bagheer bhi chla deta ha yani agar hum (obj.show() mian () nhi bhi lgay tu error hi ayga) iski example line numhber 8 pr ha.
    def show(self):
        print("hello how are you")

obj = Animal()
obj.show