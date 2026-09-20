def add_time(start, duration, starting_day=''):
    dp = duration.find(':')
    if len(duration[dp+1:]) > 2 or int(duration[dp+1:]) >= 60:
        return None
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if starting_day and not starting_day.lower().title() in days:
        return None
    n = 0
    a = start.find(':')
    hours, minutes, part_day = int(start[:a]), int(start[a+1: a+3]), start[-1:-3:-1][::-1]
    hours_to_add, minutes_to_add = int(duration[:dp]), int(duration[dp+1:])
    new_minutes = minutes + minutes_to_add
    if (part_day == 'PM' and hours < 12) or (part_day == 'AM' and hours == 12):
        hours += 12
    new_hours = hours + hours_to_add    
    if new_minutes >= 60:
        new_minutes -= 60
        new_hours += 1
    if new_hours > 24:
        n = new_hours // 24
        new_hours %= 24
        if new_hours == 0:
            new_hours = 24
    if new_hours < 12 or new_hours == 24:
        new_part_day = 'AM'
        if new_hours == 24:
            new_hours -= 12
    else:
        new_part_day = 'PM'
        if new_hours != 12:
            new_hours -= 12
    if new_minutes >= 10:
        new_time = str(new_hours) + ':' + str(new_minutes) + ' ' + new_part_day
    else:
        new_time = str(new_hours) + ':0' + str(new_minutes) + ' ' + new_part_day
    if starting_day:
        index = days.index(starting_day.lower().title())
        new_day = days[(n + index) % 7]
        new_time += f', {new_day}'
    if n == 1:
        new_time += ' (next day)'
    elif n > 1:
        new_time += f' ({n} days later)'
    return new_time