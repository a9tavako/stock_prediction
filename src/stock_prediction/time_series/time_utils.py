from datetime import date, datetime
import pandas as pd
from typing import List

from .time_series_model import DataPoint, TimeSeries


def is_date_before(first_date_str, second_date_str, time_format):
    first_date = datetime.strptime(first_date_str, time_format)
    second_date = datetime.strptime(second_date_str, time_format)

    return first_date < second_date


def find_next_n_business_days(num_days: int, start_date: date) -> List[date]:
    ans = []
    current_datetime = pd.to_datetime(date_to_datetime(start_date))
    for _ in range(num_days):
        current_datetime = current_datetime + pd.offsets.BusinessDay()
        ans.append(current_datetime.date())

    return ans


def date_to_datetime(date_input: date) -> datetime:
    return datetime(date_input.year, date_input.month, date_input.day)


def timeseries_to_datapoints(time_series: TimeSeries) -> List[DataPoint]:
    if not time_series:
        raise ValueError(f"Invalid time_series: {time_series}")

    ans = []

    start_date = time_series.time_data_points[0].date_stamp
    for time_data_point in time_series.time_data_points:
        ans.append(
            DataPoint(
                x=(time_data_point.date_stamp - start_date).days,
                y=time_data_point.value
            )
        )

    return ans


def datapoints_to_timeseries(
    ref_date: date,
    data_points: List[DataPoint]
) -> TimeSeries:
    pass


def dates_to_day_counts(ref_date: date, dates: List[date]) -> List[int]:
    if not dates:
        return []

    return [(current_date - ref_date).days for current_date in dates]
