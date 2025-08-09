import os
from config import load_config
from utils.logger import setup_logging, log_info, log_error
from menus.main_menu import main_menu
from menus.downloads_menu import downloads_menu
from menus.management_menu import management_menu
from menus.automation_menu import automation_menu
from menus.tools_menu import tools_menu

if __name__ == "__main__":
    setup_logging()
    config = load_config()
    os.makedirs(config["output_dir"], exist_ok=True)

    while True:
        choice = main_menu()

        # Downloads Menu
        if choice == "Downloads Menu":
            downloads_menu(config)

        # Management Menu
        elif choice == "Management Menu":
            management_menu(config)

        # Automation Menu
        elif choice == "Automation Menu":
            automation_menu(config)

        # Tools Menu
        elif choice == "Tools Menu":
            tools_menu(config)

        # Exit
        elif choice == "Exit":
            log_info("Exiting program...")
            break

        else:
            log_error("Invalid choice.")
