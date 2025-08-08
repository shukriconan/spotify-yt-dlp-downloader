import logging
from colorama import Fore, Style, init

init(autoreset=True)

def setup_logging():
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def log_info(msg):
    print(Fore.CYAN + msg)
    logging.info(msg)

def log_success(msg):
    print(Fore.GREEN + msg)
    logging.info(msg)

def log_error(msg):
    print(Fore.RED + msg)
    logging.error(msg)

def log_warning(msg):
    print(Fore.YELLOW + msg)
    logging.warning(msg)
