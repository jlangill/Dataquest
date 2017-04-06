def get_hour(time_stamp):
    get_date = parse(time_stamp)
    print(get_date)
    return get_date.hour

from dateutil.parser import *
from datetime import *
import pandas as pd
import read


if __name__ == "__main__":
    data = read.load_data()

    
    data["submission_hours"] = data["submission_time"].apply(get_hour)
    hours = data["submission_hours"].value_counts()
    print(hours)
