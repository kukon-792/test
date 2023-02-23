#
# class base1:
#     def fun(self):
#         print("In Class Bose 1")
#
# class sub(base1):
#     pass
#     def fun(self):
#         print("In class sub")
#
#
# ob=sub()
# ob.fun()


class Phone:
    def make_Call(self):
        print("I am making a call")
    def play_game(self):
        print("I am playing a game")

p1=Phone()
p1.play_game()
p1.make_Call()