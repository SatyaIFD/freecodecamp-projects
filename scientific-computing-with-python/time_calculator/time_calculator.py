def add_time(start_time, duration, start_day=None):
    # -----------------------------------------
    # 1. Parse the start time (e.g., "3:30 PM")
    # -----------------------------------------
    parts_of_start_time = start_time.split(" ")  # ['3:30', 'PM']
    time_str = parts_of_start_time[0]            # '3:30'
    am_pm_indicator = parts_of_start_time[1]     # 'PM'

    # Split '3:30' into hours and minutes
    time_components = time_str.split(":")        # ['3', '30']
    start_hour = int(time_components[0])         # 3
    start_min = int(time_components[1])          # 30

    # -----------------------------------------
    # 2. Convert 12-hour format to 24-hour format
    # -----------------------------------------
    # This is important for easier time calculations
    if am_pm_indicator == "PM" and start_hour != 12:
        start_hour += 12  # 3 PM → 15
    elif am_pm_indicator == "AM" and start_hour == 12:
        start_hour = 0    # 12 AM → 0

    # -----------------------------------------
    # 3. Parse the duration time (e.g., "2:12")
    # -----------------------------------------
    duration_components = duration.split(":")     # ['2', '12']
    duration_hour = int(duration_components[0])   # 2
    duration_min = int(duration_components[1])    # 12

    # -----------------------------------------
    # 4. Convert both times to minutes and add
    # -----------------------------------------
    start_total_min = start_hour * 60 + start_min           # Total minutes of start time
    duration_total_min = duration_hour * 60 + duration_min  # Total minutes of duration
    final_total_min = start_total_min + duration_total_min  # Sum = final time in minutes

    # -----------------------------------------
    # 5. Convert back to hours and minutes
    # -----------------------------------------
    new_min = final_total_min % 60                    # Final minutes after addition
    total_hours_from_start = final_total_min // 60    # Total hours after addition

    days_later_count = total_hours_from_start // 24   # Count how many full days later
    new_hour_24hr = total_hours_from_start % 24       # Hour in 24-hour format

    # -----------------------------------------
    # 6. Convert back to 12-hour format with AM/PM
    # -----------------------------------------
    if new_hour_24hr == 0:
        final_hour_12hr = 12
        final_am_pm_indicator = "AM"
    elif new_hour_24hr < 12:
        final_hour_12hr = new_hour_24hr
        final_am_pm_indicator = "AM"
    elif new_hour_24hr == 12:
        final_hour_12hr = 12
        final_am_pm_indicator = "PM"
    else:
        final_hour_12hr = new_hour_24hr - 12
        final_am_pm_indicator = "PM"

    # -----------------------------------------
    # 7. Handle the weekday (if provided)
    # -----------------------------------------
    weekday_str = ""
    if start_day:
        # List of days in order
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        # Normalize input (e.g., "monday" → "Monday")
        start_day_index = weekdays.index(start_day.capitalize())
        # Find the index of the new day after days have passed
        end_day_index = (start_day_index + days_later_count) % 7
        weekday_str = f", {weekdays[end_day_index]}"

    # -----------------------------------------
    # 8. Build the final time string
    # -----------------------------------------
    # Format the final time (e.g., "5:42 PM")
    new_time = f"{final_hour_12hr}:{str(new_min).zfill(2)} {final_am_pm_indicator}"

    # Add the day of the week if given
    if start_day:
        new_time += weekday_str

    # Add information about how many days later
    if days_later_count == 1:
        new_time += " (next day)"
    elif days_later_count > 1:
        new_time += f" ({days_later_count} days later)"

    # -----------------------------------------
    # 9. Return the final result
    # -----------------------------------------
    return new_time
