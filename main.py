import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Player creation
player = Player()

#Cars creation
car_manager = CarManager()

#Player Movement Code
screen.listen()
screen.onkey(player.move_up, "Up")


#Scoreboard
score_board = Scoreboard()
game_over = Scoreboard
score_board.update_scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # random car generation code
    car_manager.random_car_creation()
    car_manager.move_cars()


    # car collision detection code
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_over.game_over()
            game_is_on = False

    # successful passing detection code
    if player.is_at_finish_line():
        player.go_to_start()
        score_board.level += 1
        score_board.update_scoreboard()
        car_manager.increase_car_speed()


screen.exitonclick()




