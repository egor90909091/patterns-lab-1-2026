"""
Здесь необходимо реализовать Adapter.

Класс должен реализовать interfaces.BaseDigitalClock и использовать
существующий clocks.AnalogClock через композицию.
"""
from datetime import datetime

from consts import DayNightDivision
from interfaces import BaseDigitalClock
from clocks import AnalogClock


class ClockAdapter(BaseDigitalClock):
    def __init__(self, analog_clock: AnalogClock):
        self._analog_clock= analog_clock

    def set_date_time(self, date: datetime) -> None:
        year = date.year
        month = date.month
        day = date.day
        hour = date.hour
        minute = date.minute
        second = date.second

        hour_angle=(hour % 12) * 30 + minute * 0.5
        minute_angle= minute * 6
        second_angle= second * 6

        day_night_division=(
            DayNightDivision.AM if hour < 12
            else DayNightDivision.PM
            )
        self._analog_clock.set_date_time(
            year,
            month,
            day,
            hour_angle,
            minute_angle,
            second_angle,
            day_night_division
        )

    def get_date_time(self) -> datetime:
        year=self._analog_clock.get_year()
        month=self._analog_clock.get_month()
        day=self._analog_clock.get_day()
        hour_angle=self._analog_clock.get_hour_angle()
        minute_angle=self._analog_clock.get_minute_angle()
        second_angle=self._analog_clock.get_second_angle()
        day_night_division=self._analog_clock.get_day_night_division()

        hour = int((hour_angle / 30) % 12)
        minute=int(minute_angle/6)
        second=int(second_angle/6)

        if day_night_division==DayNightDivision.PM:
            hour+=12

        if day_night_division==DayNightDivision.AM and hour == 12:
            hour=0

        return datetime(year,month,day,hour,minute,second)