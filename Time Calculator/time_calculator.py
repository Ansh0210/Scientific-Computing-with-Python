def add_time(start, duration, starting_day=None):
    # Days of the week list for reference
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Convert starting day to a uniform format
    if starting_day:
        starting_day = starting_day.lower().capitalize()
    
    # Splitting the start time into hours, minutes, and AM/PM
    start_hours, start_minutes_ampm = start.split(":")
    start_minutes, am_pm = start_minutes_ampm.split(" ")
    
    # Convert start time into 24-hour format
    start_hours = int(start_hours) + (12 if am_pm == "PM" and int(start_hours) != 12 else 0) - (12 if am_pm == "AM" and int(start_hours) == 12 else 0)
    start_minutes = int(start_minutes)
    
    # Splitting the duration time into hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(":"))
    
    # Adding duration to start time
    end_minutes = start_minutes + duration_minutes
    end_hours = start_hours + duration_hours + (end_minutes // 60)
    end_minutes %= 60
    days_passed = end_hours // 24
    end_hours %= 24
    
    # Converting back to 12-hour format
    am_pm = "PM" if 12 <= end_hours < 24 else "AM"
    end_hours = end_hours if 1 <= end_hours <= 12 else end_hours - 12 if end_hours > 12 else end_hours + 12
    
    # Formatting the result
    end_time = f"{end_hours}:{end_minutes:02d} {am_pm}"
    
    # Adding the day of the week if provided
    if starting_day:
        day_index = (days_of_week.index(starting_day) + days_passed) % 7
        end_time += f", {days_of_week[day_index]}"
    
    # Adding information about the number of days later
    if days_passed == 1:
        end_time += " (next day)"
    elif days_passed > 1:
        end_time += f" ({days_passed} days later)"
    
    return end_time
