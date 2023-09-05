# write your code here
def padel_court_cost(court_type):
    if court_type == "indoor":
        return(30)
    elif court_type == "outdoor":
        return(20)
    else:False

def rackets_cost(racket_brand):
    if racket_brand==("bullpadel"):
        return(100)
    if racket_brand==("nox"):
        return(140)
    if racket_brand==("slux"):
        return(200)
    
def padel_balls_cost(ball_boxes):
    if ball_boxes==1:
        return(2)
    elif ball_boxes==2:
        return (3.5)
    elif ball_boxes==3:
        return (5)
    
def padel_game_cost():

court_type = input("court type indoor: / outdoor")
rackets_brand= input("racket_brand : nox / slux /bullpadel")
ball_boxes = int(input("number of ball boxes: 1/ 2 / 3"))
print= padel_court_cost(court_type)+ rackets_cost(rackets_brand)+ padel_balls_cost(ball_boxes)
return print

print(padel_game_cost())
