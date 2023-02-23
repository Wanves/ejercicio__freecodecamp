def add_time(start, duration, day=None):
    # Parsear la hora de inicio y la duración
    start_time, period = start.split()
    start_hour, start_min = map(int, start_time.split(':'))
    dur_hour, dur_min = map(int, duration.split(':'))

    # Convertir la hora de inicio en formato de 24 horas
    if period == 'PM' and start_hour != 12:
        start_hour += 12

    # Sumar las horas y los minutos de la duración a la hora de inicio
    total_min = start_min + dur_min
    total_hour = start_hour + dur_hour + total_min // 60
    total_min %= 60
    total_hour %= 24

    # Convertir la hora resultante de nuevo a formato de 12 horas
    period = 'AM' if total_hour < 12 else 'PM'
    display_hour = total_hour % 12 or 12
    display_min = f'{total_min:02d}'

    # Actualizar la salida con el número de días adicionales si es necesario
    day_suffix = ''
    if day:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        start_day = days.index(day.lower())
        end_day = (start_day + total_hour // 24) % 7
        day_suffix = f', {days[end_day].capitalize()}'
    days_passed = total_hour // 24
    if days_passed == 1:
        day_suffix = ' (next day)' + day_suffix
    elif days_passed > 1:
        day_suffix = f' ({days_passed} days later)' + day_suffix

    # Devolver la hora resultante en formato de cadena
    return f'{display_hour}:{display_min} {period}{day_suffix}'


print(add_time('8:30 PM', '1:45'))

