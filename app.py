from datetime import datetime

from adapters.digital_clock_adapter import ClockAdapter
from clocks import AnalogClock
from facades.clock_facade import ClockFacade
from services import ClockFormatter, ClockHistory


def main() -> None:
    facade = ClockFacade(ClockAdapter(AnalogClock()), ClockFormatter(), ClockHistory())
    print("ClockFacade создан.")

    now = datetime.now()
    facade.set_current_datetime(now)
    print(f"Установлено текущее время: {facade.get_current_datetime()}")
    print(f"Форматированное представление: {facade.get_formatted()}")
    print(f"История изменений: {facade.get_history()}")


if __name__ == "__main__":
    main()