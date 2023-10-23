# https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printTask(taskString):
    print(f"{bcolors.OKBLUE}{bcolors.BOLD}TASK: {taskString}{bcolors.ENDC}")


def printWarning(warningString):
    print(f"{bcolors.WARNING}{bcolors.BOLD}WARNING: {warningString}{bcolors.ENDC}")


def printSucces(message):
    print(f"{bcolors.OKGREEN}{bcolors.BOLD}{message}{bcolors.ENDC}")