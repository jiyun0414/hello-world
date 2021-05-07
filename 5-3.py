x = 2
y = 1
z = 0

if x > y :                                                                                       # 2가 1보다 크면
    print("x(2)는 y(1)보다 크다")                                                                 # 출력이 된다.
ptint("x가 y보디 크기(True)때문에 출력된다.","\n")

if x < y :                                                                                        # y가 x보다 크지 않다.
    print("x보다 y가 크다")                                                                       # 출력이 안된다. 
print("y가 x보다 크지 않기(False)때문에 출력 안된다.","\n")                                         

if not x < y:                                                                                     # y가 x보다 크지 않다(True).
    print("x보다 y가 크지 않다.","\n")                                                             # 출력이 된다.
print("not이 붙어서 True이기 때문에 출력된다." ,"\n")

if x > z and x> y :                                                                                # x가 z보다 크고 x가 y보다 크면
    print("y가 z보다 크고 x가 y보다 크다.")                                                         
print("두가지 모두 맞으면 (Ture) 출력된다.","\n")

if z > y and x > y :
    print("z가 y보다 크다(False) 그리고 x가 y보다 크다.(True")                                        # 하나라도 틀리면(False) 출력 안된다.
print("z가 y보다 크다(Flase), x가 y보다 크다(True) 두가지 모두 맞아야 (True) 출력된다", "\n")

if z > y or x > y :                                                                                  # 0이 1보다 크거나 또는 2가 1보다 크면
    print("z가 y보다 크거나(False) 또는 x가 y보다 크다.(True")
print("두 가지 중 하나만 맞으면 (True) 출력된다.","\n")

# 여러줄 주석 Shift + Alt + A
# 한줄한줄 Ctrl + /     
