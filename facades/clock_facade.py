"""
Здесь необходимо реализовать Facade.

Фасад должен скрывать работу как минимум с:
- цифровым адаптером;
- ClockFormatter;
- ClockHistory.
"""
from datetime import datetime

from adapters.digital_clock_adapter import ClockAdapter
from clocks import AnalogClock
from services import ClockFormatter, ClockHistory


class ClockFacade:
    def __init__(self) -> None:
        self._adapter = ClockAdapter(AnalogClock())
        self._formatter = ClockFormatter()
        self._history = ClockHistory()

    def set_current_datetime(self, date: datetime) -> None:
        self._adapter.set_date_time(date)
        self._history.add(date)

    def get_current_datetime(self) -> datetime:
        return self._adapter.get_date_time()

    def get_formatted(self, fmt: str = "%d.%m.%Y %H:%M:%S") -> str:
        return self._formatter.format(self._adapter.get_date_time(), fmt)

    def get_history(self) -> tuple[datetime, ...]:
        return self._history.all()
