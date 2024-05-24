from ninja_game.game import Game
from control.camera_control import ReceiveAction
import threading
import time

move = None

def game_theard():
    global move
    game = Game()
    move = game.movement
    print(1)
    game.run()
    print(2)


def keyboard_theard():
    test = ReceiveAction()
    test.Run_the_process()
    pass


thread1 = threading.Thread(target=game_theard)
thread2 = threading.Thread(target=keyboard_theard, daemon=True)


if __name__ == '__main__':
    thread1.start()
    thread2.start()
    # for i in range(100):
    #     time.sleep(0.6)
    #     print(move)
    # thread1.join()
    # thread2.join()
