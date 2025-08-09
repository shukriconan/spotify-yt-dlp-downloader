import questionary
from utils.system import system_check
from utils.logger import log_info

def tools_menu(config):
    """
    Displays the Tools Menu for extra utilities.
    """
    choice = questionary.select(
        "🛠 Tools Menu — Select a tool:",
        choices=[
            "System check",
            "Help",
            "Back"
        ]
    ).ask()

    if choice == "System check":
        system_check()

    elif choice == "Help":
        log_info("Help: Use yt-dlp for YouTube downloads. Modify config.json to change settings.")
