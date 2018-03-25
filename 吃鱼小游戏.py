import random as r
legal_x=[0,10]
legal_y=[0,10]

class Turtle:
    def __init__(self):
        self.power=100
        self.x=r.randint(legal_x[0],legal_x[1])
        self.y=r.randint(legal_y[0],legal_y[1])
    def move(self):
        new_x=self.x+r.choice([1,-1,2,-2])
        new_y=self.y+r.choice([1,-1,2,-2])

        if new_x>legal_x[1]:
            self.x=legal_x[1]-(new_x-legal_x[1])
        elif new_x<legal_x[0]:
            self.x=legal_x[0]-(new_x-legal_x[0])
        else:
            self.x=new_x
            
        if new_y>legal_y[1]:
            self.y=legal_y[1]-(new_y-legal_y[1])
        elif new_y<legal_y[0]:
            self.y=legal_y[0]-(new_y-legal_y[0])
        else:
            self.y=new_y
        self.power-=1
        return (self.x,self.y)

    def eat(self):
        self.power+=20
        if self.power>100:
            self.power=100
            
class Fish:
    def __init__(self):
        self.x=r.randint(legal_x[0],legal_x[1])
        self.y=r.randint(legal_y[0],legal_y[1])
    def move(self):
        new_x=self.x+r.choice([1,-1])
        new_y=self.y+r.choice([1,-1])

        if new_x>legal_x[1]:
            self.x=legal_x[1]-(new_x-legal_x[1])
        elif new_x<legal_x[0]:
            self.x=legal_x[0]-(new_x-legal_x[0])
        else:
            self.x=new_x
        if new_y>legal_y[1]:
            self.y=legal_y[1]-(new_y-legal_y[1])
        elif new_y<legal_y[0]:
            self.y=legal_y[0]-(new_y-legal_y[0])
        else:
            self.y=new_y
        return (self.x,self.y)
turtle=Turtle()
fish=[]
for i in range(10):
    new_fish=Fish()
    fish.append(new_fish)
while True:
    if not len(fish):
        print('鱼全部被吃完了,游戏结束鸟！')
        break
    
    if turtle.power<=0:
        print('乌龟体力耗尽，挂了')
        break
    pos=turtle.move()
    for each_fish in fish[:]:
        if each_fish.move()==pos:
            turtle.eat()
            fish.remove(each_fish)
            print('有一条鱼被吃掉了')
            
    
