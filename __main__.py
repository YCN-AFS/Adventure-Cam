import time
from ninja_game.game import Game


def game_theard():
    global game
    game = Game()
    game.run()

def update_thread():
    while True:
        time.sleep(0.2)
        game.movement = test.character_control
        print(test.character_control)


def keyboard_theard():
    global test
    test = ReceiveAction()
    game.movement = test.character_control
    test.Run_the_process()


if __name__ == '__main__':
    from control.camera_control import ReceiveAction
    import threading


    threading.Thread(target=game_theard).start()
    threading.Thread(target=keyboard_theard, daemon=True).start()
    threading.Thread(target=update_thread, daemon=True).start()





