import json
import subprocess
from collections import defaultdict
from itertools import groupby
from typing import Dict


def task1() -> Dict[str, int]:

    count_log_levels = {
        'DEBUG': 0,
        'INFO': 0,
        'WARNING': 0,
        'ERROR': 0,
        'CRITICAL': 0
    }
    for level_key, level_value in count_log_levels.items():
        cmd = f"""grep -c '"level": "{level_key}"' skillbox_json_messages.log"""
        count_log_levels[level_key] = int(subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode())
    return count_log_levels


def task2() -> int:

    hours = []
    for log_line in log_data:
        hours.append(log_line['time'][:2])
    groups = []
    unique_keys = []
    for k, g in groupby(hours):
        groups.append(len(list(g)))
        unique_keys.append(k)
    max_value = max(groups)
    max_value_index = groups.index(max_value)
    return int(unique_keys[max_value_index])


def task3() -> int:

    cmd = f"""grep -E '"level": "CRITICAL' skillbox_json_messages.log |
            grep -E '"time": "(05:([0-1][0-9]|19):[0-5][0-9])"' | wc -l"""
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode()
    return int(result)


def task4() -> int:

    cmd = f"""grep -E '"message": .+dog' skillbox_json_messages.log | wc -l"""
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode()
    return int(result)


def task5() -> str:

    warning_messages = []
    for log_level in log_data:
        if log_level['level'] == "WARNING":
            warning_messages.append(log_level['message'])

    temp = defaultdict(int)

    for message in warning_messages:
        for word in message.split():
            temp[word] += 1

    result = max(temp, key=temp.get)
    return result


if __name__ == '__main__':
    log_data = []

    with open('skillbox_json_messages.log', 'r') as file:
        for line in file.readlines():
            log_data.append(json.loads(line.rstrip()))

    tasks = (task1, task2, task3, task4, task5)
    for i, task_fun in enumerate(tasks, 1):
        task_answer = task_fun()
        print(f'{i}. {task_answer}')