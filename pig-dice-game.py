from random import randint
class Pig_dice_game:
    def __init__(self):
        self.TotalScore=0

    def new_game(self):
        print("********************")
        print("********************")
        print("**** GAME START ****")
        print("********************")
        print("********************")
        self.turn()

    def roll_dice(self):
        pass
    
    def turn(self):
        #TOTAL_SCORE가 100이상이면 Win 메소드로 이동
        if self.TotalScore>=100:
            self.Win()
        else:
            #주사위를 굴린다.
            self.roll_dice()
    
    def bank(self):
        if self.TotalScore == current_score:
            self.turn()

    def Win(self):
        pass
    

player1=Pig_dice_game()

#게임 시작
player1.new_game()

#이후 컴퓨터 진행