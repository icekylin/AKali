from colorama import init, Fore, Back, Style

init(autoreset=True)

def current_time():
    import time
    return time.strftime("%H:%M:%S", time.localtime())


class Output:

    def __init__(self):
        pass
        
    def info(self, msg="NULL"):
        print(f'{Fore.GREEN}{current_time()} [INFO] {msg}')

    def error(self, msg="NULL"):
        print(f'{Fore.RED}{current_time()} [ERROR] {msg}')