import os
from dotenv import load_dotenv
import questionary
from rich.console import Console

load_dotenv()
console = Console()

THRESHOLD_DAYS = int(os.getenv("RENEWAL_THRESHOLD_DAYS", "30"))


def check_domains():
    console.print("TODO: проверка сроков доменов .ton")


def show_config():
    console.print(f"Порог продления: {THRESHOLD_DAYS} дн.")
    console.print(f"API key задан: {bool(os.getenv('TON_API_KEY'))}")


def main():
    while True:
        choice = questionary.select(
            "TON domains:",
            choices=[
                "Проверить домены",
                "Настройки",
                "Выход",
            ],
        ).ask()

        if choice == "Проверить домены":
            check_domains()
        elif choice == "Настройки":
            show_config()
        else:
            break


if __name__ == "__main__":
    main()
