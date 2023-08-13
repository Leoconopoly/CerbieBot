import datetime

def convert_to_timestamp(time_str: str) -> datetime.datetime:
    """
    Convert a time string like "10 minutes" or "2 hours" into a future datetime object.
    """
    # Split the input string into value and unit
    value, unit = time_str.split()

    # Convert the value to an integer
    value = int(value)

    # Get the current time
    now = datetime.datetime.now()

    # Calculate the future time based on the unit
    if "minute" in unit:
        return now + datetime.timedelta(minutes=value)
    elif "hour" in unit:
        return now + datetime.timedelta(hours=value)
    elif "day" in unit:
        return now + datetime.timedelta(days=value)
    else:
        raise ValueError(f"Unsupported time unit: {unit}")
