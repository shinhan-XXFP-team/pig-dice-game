from random import randint

User_name=""
User_TotalScore=0
User_dice_number=0

# 게임 시작
def new_game():
    print("********************")
    print("********************")
    print("**** GAME START ****")
    print("********************")
    print("********************")
    # 시작을 했으므로 turn메소드로 넘어간다.
    User_name=input("당신의 이름은 무엇입니까? : ")
    turn()

    # 주사위를 굴리는 페이지
def roll_dice():
    # 주사위 1번은 무조건 굴린다.
    current_score=0
    choose='y'
    print(f"현재 {User_name}님의 차례입니다.")
    dice_number=randint(1,6)
    print(f"{User_name}님의 주사위 숫자는 {dice_number}입니다!!")
    # 주사위 값이 1이 아니라면 
    if dice_number!=1:
        current_score+=dice_number
        print(f"현재 주사위 CURRENT SCORE = {current_score}")
        #y를 선택했다면 반복
        while choose=='y':
            choose=input("주사위를 더 돌린 건가요? (네=y/아니요=n): ")
            if choose=='y':      
                dice_number=randint(1,6)
                print(f"주사위 숫자는 = {dice_number}")
                if dice_number==1:
                    print(f"주사위 값이 {dice_number}이기 때문에 차례를 종료하겠습니다.")
                    turn()
                else:
                    current_score+=dice_number
                    print(f"현재 총 주사위 숫자 : {current_score}")
            elif choose=='n':
                bank(current_score)
            else:
                print("잘못 입력하셨습니다 y 또는 n을 입력해주세요")
    # 주사위 값이 1이라면
    else:
        print(f"주사위 값이 {dice_number}이기 때문에 차례를 종료하겠습니다.")
        turn()
        
def turn():
    #TOTAL_SCORE가 100이상이면 Win 메소드로 이동

    if User_TotalScore>=100:
        Win()
    elif Computer_TotalScore>=100:
        Com_Win(0)
    else:
        #주사위를 굴린다.
        roll_dice()

def bank(current_score):                 
    print(f"현재 총 주사위 숫자 {current_score} 을 BANK하겠습니다.")
    User_TotalScore += current_score
    print(f"현재 User_TotalScore= {User_TotalScore}")
    turn()
    
def Win():
    print(f"{User_name}님이 {User_TotalScore} 이기셨습니다.")

def Com_Win():
    pass

#게임 시작
new_game("user1")


#이후 컴퓨터 진행