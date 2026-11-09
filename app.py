from datetime import datetime

from facades.clock_facade import ClockFacade


def main() -> None:
    facade = ClockFacade()
    print("ClockFacade создан.")

    now = datetime.now()
    facade.set_current_datetime(now)
    print(f"Установлено текущее время: {facade.get_current_datetime()}")
    print(f"Форматированное представление: {facade.get_formatted()}")
    print(f"История изменений: {facade.get_history()}")


if __name__ == "__main__":
    main()