import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


delay = 0.001
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):
    def init(self, delay, button):
        super(ClickMouse, self).init()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()

delay: Они задерживаются между каждым щелчком мыши (в секундах)
button: Кнопка мыши для щелчка; Button.left | Button.middle | Button.right
start_stop_key: Они запускают и останавливают нажатие клавиши. Убедитесь, что это либо из класса Key, либо задано с помощью ключевого кода, как показано.
exit_key: Клавиша для остановки программы. Убедитесь, что это либо из класса Key, либо задано с помощью ключевого кода, как показано.
Код на автокликер на пайсон
