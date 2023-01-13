from random import randint

class Pig_dice_game:
    def __init__(self, name):
        self.name=name
        self.TotalScore=0
        self.dice_number=0

    # 게임 시작
    def new_game(self):
        print("********************")
        print("********************")
        print("**** GAME START ****")
        print("********************")
        print("********************")
        # 시작을 했으므로 turn메소드로 넘어간다.
        self.name=input("당신의 이름은 무엇입니까? : ")
        self.turn()

    # 주사위를 굴리는 페이지
    def roll_dice(self):
        # 주사위 1번은 무조건 굴린다.
        current_score=0
        choose='y'
        self.dice_number=randint(1,6)
        print(f"{self.name}님의 주사위 숫자는 {self.dice_number}입니다!!")
        # 주사위 값이 1이 아니라면 
        if self.dice_number!=1:
            current_score+=self.dice_number
            print(f"현재 주사위 CURRENT SCORE = {current_score}")
            while choose!='y':
                choose=input("주사위를 더 돌린 건가요? (네=y/아니요=n): ")
                if choose=='y':      
                    self.dice_number=randint(1,6)
                    print(f"주사위 숫자는 = {self.dice_number}")
                elif choose=='n':
                    print(f"현재 총 주사위 숫자 {current_score} 을 BANK하겠습니다. ")
                    self.bank(current_score)
                else:
                    print("잘못 입력하셨습니다 y 또는 n을 입력해주세요")
            
    
    def turn(self):
        pass
    
    def bank(self, score):
        pass
    

player1=Pig_dice_game("user1")

#게임 시작
player1.new_game()

#이후 컴퓨터 진행