#
# def Welcome(str):
#     print("Welcome to the python, ",str)
#     return()
# Welcome(str="Kukon")

def print_users(user, *users):
    print('first user argument: ', user)
    for user in users:
        print('user received from variable leanth argument: ', user)
print_users('edureka','admin','ceo','manager','worker')