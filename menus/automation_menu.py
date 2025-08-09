import questionary
from managers.resume_manager import resume_batch
from managers.schedule_manager import schedule_download

def automation_menu(config):
    """
    Displays the Automation Menu and runs automation tasks.
    """
    choice = questionary.select(
        "🤖 Automation Menu — Choose an option:",
        choices=[
            "Resume paused batch download",
            "Schedule a download job",
            "Back"
        ]
    ).ask()

    if choice == "Resume paused batch download":
        resume_batch(config)

    elif choice == "Schedule a download job":
        schedule_download(config)
