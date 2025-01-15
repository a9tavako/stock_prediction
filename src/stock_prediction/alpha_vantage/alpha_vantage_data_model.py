from datetime import date
from pydantic import BaseModel, Field, field_serializer
from typing import Dict


class DailyStockData(BaseModel):
    open: float = Field(alias="1. open")
    high: float = Field(alias="2. high")
    low: float = Field(alias="3. low")
    close: float = Field(alias="4. close")
    volume: int = Field(alias="5. volume")


class MetaData(BaseModel):
    information: str = Field(alias="1. Information")
    symbol: str = Field(alias="2. Symbol")
    last_refreshed: date = Field(alias="3. Last Refreshed")
    output_size: str = Field(alias="4. Output Size")
    time_zone: str = Field(alias="5. Time Zone")


class StockData(BaseModel):
    metadata: MetaData = Field(alias="Meta Data")
    time_series: Dict[date, DailyStockData] = Field(alias="Time Series (Daily)")

    @field_serializer("time_series")
    def serialize_time_series(self, time_series: Dict[date, DailyStockData]) -> Dict[str, DailyStockData]:
        return {key.isoformat(): value for key, value in time_series.items()}