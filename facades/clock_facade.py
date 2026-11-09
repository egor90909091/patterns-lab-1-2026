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
from interfaces.base_digital_clock import BaseDigitalClock

class ClockFacade:
    def __init__(
        self,
        clock: BaseDigitalClock | None = None,
        formatter: ClockFormatter | None = None,
        history: ClockHistory | None = None,
    ) -> None:
        self._clock = clock or ClockAdapter(AnalogClock())
        self._formatter = formatter or ClockFormatter()
        self._history = history or ClockHistory()

    def set_current_datetime(self, date: datetime) -> None:
        self._clock.set_date_time(date)
        self._history.add(date)

    def get_current_datetime(self) -> datetime:
        return self._clock.get_date_time()

    def get_formatted(self, fmt: str = "%d.%m.%Y %H:%M:%S") -> str:
        return self._formatter.format(self._clock.get_date_time(), fmt)

    def get_history(self) -> tuple[datetime, ...]:
        return self._history.all()
