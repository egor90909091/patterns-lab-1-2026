from datetime import datetime

from clocks import AnalogClock
from adapters.digital_clock_adapter import ClockAdapter
from consts import DayNightDivision


def test_morning_round_trip():
    """Утро: возвращает исходное время."""
    adapter = ClockAdapter(AnalogClock())
    dt = datetime(2024, 11, 9, 9, 30, 15)
    adapter.set_date_time(dt)
    assert adapter.get_date_time() == dt


def test_midnight():
    """Полночь 00:00:00 (AM)."""
    adapter = ClockAdapter(AnalogClock())
    dt = datetime(2024, 1, 1, 0, 0, 0)
    adapter.set_date_time(dt)
    assert adapter.get_date_time() == dt


def test_noon():
    """Полдень 12:00:00 (PM)."""
    adapter = ClockAdapter(AnalogClock())
    dt = datetime(2024, 6, 15, 12, 0, 0)
    adapter.set_date_time(dt)
    assert adapter.get_date_time() == dt


def test_afternoon():
    """PM-время: 15:45:30."""
    adapter = ClockAdapter(AnalogClock())
    dt = datetime(2024, 6, 15, 15, 45, 30)
    adapter.set_date_time(dt)
    assert adapter.get_date_time() == dt


def test_am_pm_set_correctly():
    """AM/PM правильно определяется и записывается."""
    adapter = ClockAdapter(AnalogClock())

    adapter.set_date_time(datetime(2024, 1, 1, 8, 0, 0))
    assert adapter._analog_clock.get_day_night_division() == DayNightDivision.AM

    adapter.set_date_time(datetime(2024, 1, 1, 20, 0, 0))
    assert adapter._analog_clock.get_day_night_division() == DayNightDivision.PM

