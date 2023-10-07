from datetime import datetime

def get_datetime_from_str(datetime_str:str) -> datetime:
    try:
        today = datetime.today()
        search_dt = (datetime
                        .strptime(datetime_str,"%H:%M:%S")
                        .replace(
                            year=today.year,
                            month=today.month,
                            day=today.day + 1 # Get a day in the future
                        )) # Replace because it defaults to 1990-01-01. Get most up to date info
        
        return search_dt
    except Exception as e:
        raise e