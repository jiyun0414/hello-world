# 불리언 2nd
# 불리언 2nd
# 여러줄 주석  Shift + Alt + A
# 한줄한줄 Ctrl + / 

x = 3

# 1)
if x > 2:                     # x 가 2보다 크면 Hello라고 출력
    print("Hello","\n")
    
# 2)
if x > 5:
    print("Hello", "\n")      # x가 5보다 크면 Hello라고 출력하고
else:                          # 그게 아니라면
    print("Hi","\n")          # Hi라고 출력해라
    
# 3)
if x > 5:
    print("Hello","\n")      # x가 5보다 큰지 보구
elif x == 3:                  # x가 3인지 보구
    print("Bye","\n")
else:                        # 그게 아니라면
    print("Hi","\n")         # Hi로 간다.
