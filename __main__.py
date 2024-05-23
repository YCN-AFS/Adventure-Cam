from ninja_game.game import Game
import threading

def game_theard():
    game = Game()
    game.run()
def keyboard_theard():
    #from control import test1
    pass



thread1 = threading.Thread(target=game_theard)
thread2 = threading.Thread(target=keyboard_theard)


if __name__ == '__main__':
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()







