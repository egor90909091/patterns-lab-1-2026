from datetime import datetime

from interfaces import BaseDigitalClock


class DigitalClock(BaseDigitalClock):
    """Готовый компонент. Изменять его интерфейс в рамках ЛР не требуется."""

    def __init__(self) -> None:
        self.date = datetime(200,1,1,0,0,0 )

    def set_date_time(self, date: datetime)-> None:
        self.date = date

    def get_date_time(self) -> datetime:
        return self.date