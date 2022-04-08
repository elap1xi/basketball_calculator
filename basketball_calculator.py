"""
1. 발사각, 원하는 사거리 -> 필요한 힘, 최고점의 높이, 수평도달거리, 체공시간
2. 힘, 원하는 사거리 -> 발사각, 최고점의 높이, 수평도달거리, 체공시간
3. 발사각, 힘 -> 최고점의 높이, 수평도달거리, 체공시간
"""

import math
import matplotlib.pyplot as plt


g = 9.80665
working = True

def equation(x):
    y = x*math.tan(InputAngle) - g*x**2/2/InputSpeed**2/math.cos(InputAngle)**2
    return y

def H(a, b): #최고점의 높이 구하는 함수, a는 발사속도 b는 발사각
     H = a**2*math.sin(b)**2/2/g
     return H
    
def R(a, b): #사거리(수평도달거리) 구하는 함수 a는 발사속도 b는 발사각
    R = a**2*math.sin(2*b)/g
    return R

def T(a, b): #체공시간 구하는 함수
    T = 2*a*math.sin(b)/g
    return T

def A(a, b): #발사각 구하는 함수 a는 발사속도 b는 원하는 사거리
    A = math.asin(b*g/a**2)/2
    return A

def S(a, b): #발사속도 구하는 함수 a는 발사각 b는 원하는 사거리
    S = math.sqrt(b*g/math.sin(2*a))
    return S


while working == True:
    try:
        WV = input("구하려는 값을 입력해 주세요 \n 1.발사각 2.필요한 힘 3.발사각과 필요한 힘이 정해졌을 때의 탄도 4.프로그램 종료\n")
        if WV == "1":
            InputSpeed = int(input("발사속도를 입력해 주세요(단위: m/s) \n"))
            InputWS = int(input("원하는 사거리를 입력해 주세요(단위: m) \n"))
            InputAngle = A(InputSpeed, InputWS)
            print("발사각:", math.degrees(InputAngle))
            print("최고점의 높이:", H(InputSpeed, InputAngle))
            print("수평도달거리:", R(InputSpeed, InputAngle))
            print("체공시간:", T(InputSpeed, InputAngle))
            x = [a for a in range(0, int(R(InputSpeed, InputAngle)))]
            y = [equation(b) for b in range(0,  int(R(InputSpeed, InputAngle)))]
            plt.plot(x, y)
            plt.show()
        elif WV == "2" :
            InputAngle = int(input("발사각을 입력해주세요(단위: °) \n"))
            InputWS = int(input("원하는 사거리를 입력해 주세요(단위: m) \n"))
            InputSpeed = S(InputAngle, InputWS)
            print("발사속도:", InputSpeed)
            print("최고점의 높이:", H(InputSpeed, InputAngle))
            print("수평도달거리:", R(InputSpeed, InputAngle))
            print("체공시간:", T(InputSpeed, InputAngle))
            x = [a for a in range(0, int(R(InputSpeed, InputAngle)))]
            y = [equation(b) for b in range(0,  int(R(InputSpeed, InputAngle)))]
            plt.plot(x, y)
            plt.show()
        elif WV == "3" :
            InputAngle = math.radians(int(input("발사각을 입력해 주세요(단위:  °) \n")))
            InputSpeed = int(input("발사속도를 입력해 주세요(단위: m/s) \n"))
            print("최고점의 높이:", H(InputSpeed, InputAngle))
            print("수평도달거리:", R(InputSpeed, InputAngle))
            print("체공시간:", T(InputSpeed, InputAngle))
            x = [a for a in range(0, int(R(InputSpeed, InputAngle)))]
            y = [equation(b) for b in range(0,  int(R(InputSpeed, InputAngle)))]
            plt.plot(x, y)
            plt.show()
        elif WV == "4":
            working = False
        else :
            print("입력값이 잘못되었습니다 다시 입력해주세요")
    except ValueError:
        print("입력값이 잘못되었습니다.")
    except Exception:
        print("알 수 없는 오류가 발생하였습니다.")