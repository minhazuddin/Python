import random


def streak_percent():
    number_of_streak = 0
    for i in range(10000):
        tossed_result = []
        head_count = 0
        tail_count = 0
        for x in range(100):
            tossed_result.append(random.choice(['H', 'T']))
        for y in tossed_result:
            if y == 'H':
                head_count += 1
            else:
                head_count = 0
            if y == "T":
                tail_count += 1
            else:
                tail_count = 0
            if head_count == 6 or tail_count == 6:
                number_of_streak += 1
                break
    return f"Streak count is {number_of_streak} and percent is {(number_of_streak / 100)}"


print(streak_percent())
