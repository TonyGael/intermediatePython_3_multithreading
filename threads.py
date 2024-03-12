import threading


# def hey_you():
#     print('Hi you! Welcome to Python :-)')
#
#
# t1 = threading.Thread(target=hey_you)
# t1.start()

# def function_one():
#     for x in range(10000):
#         print('one')
#
#
# def function_two():
#     for x in range(10000):
#         print('two')
#
#
# # function_one()
# # function_two()
#
# t1 = threading.Thread(target=function_one)
# t2 = threading.Thread(target=function_two)
#
# t1.start()
# t2.start()

def hey_you():
    for x in range(50):
        print('Hey you"')


t1 = threading.Thread(target=hey_you)
t1.start()

t1.join()

print('Another foo...')
