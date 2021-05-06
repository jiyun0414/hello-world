def sayHello(name, age):
    if age < 10:
        print("안녕, "+ name)
    elif age <=20 and age >= 10:
        print("안녕하세요,"+ name)
    else:
        print("안녕하십니까?"+ name)

sayHello("태희", 10)
sayHello("정수", 22)
sayHello("철수", 6)
sayHello("영희", 40)
