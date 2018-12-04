import re
from datetime import datetime


class Guard():
    def __init__(self, id):
        self.id = id
        self.sleeping_times = []
        self.total_sleeping_minutes = -1
        self.sleepiest_minute = -1
        self.sleep_count_in_sleepiest_minute = -1

    def add_sleeping_time(self, date1, date2):
        self.sleeping_times.append((date1, date2))

    def calculate_total_sleeping_time(self):
        for start_date, end_date in self.sleeping_times:
            self.total_sleeping_minutes += (end_date-start_date).total_seconds() / 60.0

    def find_most_sleepiest_minute(self):
        minute_list = [0 for _ in range(60)]

        for start_date, end_date in self.sleeping_times:
            for i in range(start_date.minute - 1, end_date.minute - 1):
                minute_list[i] += 1

        self.sleepiest_minute = minute_list.index(max(minute_list)) + 1
        self.sleep_count_in_sleepiest_minute = max(minute_list)


def read_records():
    with open('input.txt') as f:
        records = []

        for line in f:
            records.append(line)

        records.sort()

        return records


def process_sleep_times(records):
    guard_dict = {}
    date_format = '%Y-%m-%d %H:%M'

    for record in records:
        time_str = record[record.find("[") + 1:record.find("]")]

        # guard begins a shift
        if 'Guard' in record:
            current_guard_id = int(re.search('#(\d+)', record).group(1))
        # guard falls a sleep
        elif 'falls' in record:
            current_start_time = datetime.strptime(time_str, date_format)
        # guard wakes up
        elif 'wakes' in record:
            end_time = datetime.strptime(time_str, date_format)

            if current_guard_id not in guard_dict:
                guard = Guard(current_guard_id)
                guard_dict[current_guard_id] = guard
            else:
                guard = guard_dict[current_guard_id]

            guard.add_sleeping_time(current_start_time, end_time)

    return guard_dict


def calculate_total_sleep_times(guard_dict):
    for guard_id, guard in guard_dict.items():
        guard.calculate_total_sleeping_time()


def find_sleepiest_guard(guard_dict):
    max_total_minutes = 0
    sleepy_guard = None

    for guard_id, guard in guard_dict.items():
        if guard.total_sleeping_minutes > max_total_minutes:
            max_total_minutes = guard.total_sleeping_minutes
            sleepy_guard = guard

    return sleepy_guard


def calculate_sleepiest_minutes(guard_dict):
    for guard_id, guard in guard_dict.items():
        guard.find_most_sleepiest_minute()


def find_sleepiest_minute_record(guard_dict):
    max_sleepiest_minute_count = -1

    for guard_id, guard in guard_dict.items():
        if guard.sleep_count_in_sleepiest_minute > max_sleepiest_minute_count:
            max_sleepiest_minute_count = guard.sleep_count_in_sleepiest_minute
            max_guard = guard

    return max_guard


def get_score(guard):
    return guard.id * guard.sleepiest_minute


if __name__ == '__main__':
    records = read_records()

    guard_dict = process_sleep_times(records)
    calculate_total_sleep_times(guard_dict)
    sleepy_guard = find_sleepiest_guard(guard_dict)
    calculate_sleepiest_minutes(guard_dict)
    sleepiest_minute_record_guard = find_sleepiest_minute_record(guard_dict)

    print(get_score(sleepy_guard))
    print(get_score(sleepiest_minute_record_guard))
