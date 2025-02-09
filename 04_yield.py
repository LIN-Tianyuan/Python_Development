def my_generator():
    print("Start")
    yield 10
    print("Middle")
    yield 20
    print("End")

gen = my_generator()
print(next(gen))  # "Start" -> output 10