from random import randint

User_TotalScore=0
Computer_TotalScore=0
Current_Score=0
Roll_number=0

# 게임 시작
print("********************")
print("********************")
print("**** GAME START ****")
print("********************")
print("********************")

User_name=input("당신의 이름은 무엇입니까? : ")

def User_Turn():
    roll = randint(1,6)
    print(f"{User_name}님의 주사위 숫자는 {roll}입니다!!")
    return roll

def Computer_Turn():
    roll = randint(1,6)
    print(f"컴퓨터의 주사위 숫자는 {roll}입니다!!")
    return roll

def User_Win():
    print(f"{User_name}님이 이겼습니다.")
    print(f"User Score = {User_TotalScore} Computer Score={Computer_TotalScore}")

def Computer_Win():
    print("컴퓨터가 이겼습니다.")
    print(f"Computer Score={Computer_TotalScore} User Score = {User_TotalScore}")

while User_TotalScore<100 and Computer_TotalScore<100:
    # 유저 차례
    Current_Score=0
    UserScore = User_Turn()
    while(UserScore != 1):        
        Current_Score += UserScore
        print(f"현재 {User_name} 주사위 합 점수 {Current_Score}")
        choose=input("주사위를 더 돌린 건가요? (네=y/아니요=n): ") 
        if choose=='n':
            User_TotalScore+=Current_Score
            print(f"현재 {User_name} 의 총합점수 = {User_TotalScore}")
            UserScore=1
            break
        UserScore = User_Turn()     
    Current_Score=0
    if UserScore==1:
        print(f"{User_name}님 차례를 종료하겠습니다.")
        
        ComputerScore = Computer_Turn()
        count=0
        # 컴퓨터 주사위 점수가 1이 아니고 Roll은 3번만
        while(ComputerScore != 1 and count<3):
            print(f"+{ComputerScore}")
            Current_Score = Current_Score + ComputerScore
            print(f"현재 Computer의 주사위 합 점수 {Current_Score}")
            count+=1        
            ComputerScore = Computer_Turn()
        if ComputerScore == 1:
            print(f"컴퓨터 주사위가 1이기 때문에 종료하겠습니다.")
        else:
            Computer_TotalScore+=Current_Score
            print(f"현재 컴퓨터의 총합점수 = {Computer_TotalScore}")

if User_TotalScore > Computer_TotalScore:
    User_Win()
else:
    Computer_Win()