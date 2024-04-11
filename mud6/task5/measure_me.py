import datetime
import logging
import random
from typing import List

logger = logging.getLogger(__name__)


def get_data_line(sz: int) -> List[int]:
    try:
        logger.info("Enter get_data_line")
        return [random.randint(-(2 ** 31), 2 ** 31 - 1) for _ in range(sz)]
    finally:
        logger.info("Leave get_data_line")


def measure_me(nums: List[int]) -> List[List[int]]:
    logger.info("Enter measure_me")
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        logger.info(f"Iteration {i}")
        left = i + 1
        right = len(nums) - 1
        target = 0 - nums[i]
        if i == 0 or nums[i] != nums[i - 1]:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    logger.debug(f"Found {target}")
                    results.append([nums[i], nums[left], nums[right]])
                    logger.debug(
                        f"Appended {[nums[i], nums[left], nums[right]]} to result"
                    )
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s < target:
                    logger.debug(f"Increment left (left, right) = {left, right}")
                    left += 1
                else:
                    logger.debug(f"Decrement right (left, right) = {left, right}")

                    right -= 1

    logger.debug("Leave measure_me")

    return results


def measure_time():
    with open('logger.txt', 'r') as file:
        log_data = file.readlines()

    last = log_data[-1].split(' ')[0]
    first = log_data[0].split(' ')[0]

    obj_time = datetime.datetime.strptime(last, "%M:%S.%f")
    obj_time_2 = datetime.datetime.strptime(first, "%M:%S.%f")

    last_ms = (obj_time_2.minute * 60 + obj_time_2.second) * 1000 + obj_time_2.microsecond / 1000
    first_ms = (obj_time.minute * 60 + obj_time.second) * 1000 + obj_time.microsecond / 1000
    result = last_ms - first_ms

    print(
        f"Среднее время выполнение функции measure_me: {abs(round(result, 2))} миллисекунд или {abs(result / 1000)} секунд ")


if __name__ == "__main__":
    logging.basicConfig(
        level="INFO",
        filename='logger.txt',
        filemode='w',
        format="%(asctime)s.%(msecs)03d - %(message)s",
        datefmt='%M:%S'
    )

    for it in range(15):
        data_line = get_data_line(10 ** 3)
        measure_me(data_line)

    measure_time()