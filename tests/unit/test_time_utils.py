from datetime import date, datetime
import pandas as pd

from stock_prediction.time_series.time_series_model import TimeSeries, TimeDataPoint, DataPoint
from stock_prediction.time_series.time_utils import find_next_n_business_days, date_to_datetime, timeseries_to_datapoints, dates_to_day_counts
from typing import List


def test_find_next_n_business_days():
    initial_date = date(2024, 11, 14)
    num_days = 3
    expected_days = [
        date(2024, 11, 15),
        date(2024, 11, 18),
        date(2024, 11, 19),
    ]

    next_business_days = find_next_n_business_days(num_days, initial_date)
    assert expected_days == next_business_days


def test_timeseries_to_datapoints():
    time_series = TimeSeries([
        TimeDataPoint(date(2024, 8, 9), 191.4500),
        TimeDataPoint(date(2024, 8, 12), 189.4800),
        TimeDataPoint(date(2024, 8, 13), 190.9900)
    ])

    expected_data_points = [
        DataPoint(0, 191.45),
        DataPoint(3, 189.48),
        DataPoint(4, 190.99),
    ]
    data_points = timeseries_to_datapoints(time_series)
    assert data_points == expected_data_points


def test_dates_to_day_diffs():
    ref_date = date(2024, 8, 8)
    dates = [
        date(2024, 8, 9),
        date(2024, 8, 11),
        date(2024, 8, 13),
        date(2024, 8, 16)
    ]
    expected_diffs = [1, 3, 5, 8]

    assert dates_to_day_counts(ref_date, dates) == expected_diffs
