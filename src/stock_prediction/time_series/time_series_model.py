from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class DataPoint:
    x: int
    y: float

    def __init__(self, x: int, y: float):
        self.x = x
        self.y = y


@dataclass
class TimeDataPoint:
    date_stamp: date
    value: float

    def __init__(self, date_stamp: date, value: float):
        self.date_stamp = date_stamp
        self.value = value


@dataclass
class TimeSeries:
    time_data_points: List[TimeDataPoint]

    def __init__(self, data_points: List[TimeDataPoint]):
        self.time_data_points = data_points

    def add_data_point(self, date_stamp: date, value: float):
        self.time_data_points.append(
            TimeDataPoint(date_stamp, value)
        )
