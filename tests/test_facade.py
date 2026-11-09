from datetime import datetime

from facades.clock_facade import ClockFacade
from clocks.analog_clock import AnalogClock
from adapters.digital_clock_adapter import ClockAdapter
from services import ClockFormatter, ClockHistory

def test_facade_set_and_get():
    """Фасад корректно устанавливает и возвращает время"""
    facade = ClockFacade(ClockAdapter(AnalogClock()),ClockFormatter(),ClockHistory())
    dt = datetime(2024, 11, 9, 15, 30, 0)
    facade.set_current_datetime(dt)
    assert facade.get_current_datetime() == dt


def test_facade_formatted():
    """Фасад возвращает форматированное представление"""
    facade = ClockFacade(ClockAdapter(AnalogClock()), ClockFormatter(), ClockHistory())
    facade.set_current_datetime(datetime(2024, 11, 9, 15, 30, 0))
    assert facade.get_formatted() == "09.11.2024 15:30:00"


def test_facade_custom_format():
    """Фасад принимает пользовательский формат"""
    facade = ClockFacade(ClockAdapter(AnalogClock()), ClockFormatter(), ClockHistory())
    facade.set_current_datetime(datetime(2024, 11, 9, 15, 30, 0))
    assert facade.get_formatted("%H:%M") == "15:30"


def test_facade_history_grows():
    """История растёт после каждой установки"""
    facade = ClockFacade(ClockAdapter(AnalogClock()), ClockFormatter(), ClockHistory())
    facade.set_current_datetime(datetime(2024, 1, 1, 0, 0, 0))
    facade.set_current_datetime(datetime(2024, 1, 2, 12, 0, 0))
    facade.set_current_datetime(datetime(2024, 1, 3, 18, 30, 0))
    assert len(facade.get_history()) == 3


def test_facade_history_preserves_order():
    """История хранит значения в порядке добавления"""
    facade = ClockFacade(ClockAdapter(AnalogClock()), ClockFormatter(), ClockHistory())
    dt1 = datetime(2024, 1, 1, 0, 0, 0)
    dt2 = datetime(2024, 1, 2, 12, 0, 0)
    facade.set_current_datetime(dt1)
    facade.set_current_datetime(dt2)
    assert facade.get_history() == (dt1, dt2)


def test_facade_full_workflow():
    """Полный цикл установки и истории"""
    facade = ClockFacade(ClockAdapter(AnalogClock()), ClockFormatter(), ClockHistory())
    dt = datetime(2024, 6, 15, 12, 0, 0)
    facade.set_current_datetime(dt)

    assert facade.get_current_datetime() == dt
    assert facade.get_formatted() == "15.06.2024 12:00:00"
    assert facade.get_history() == (dt,)