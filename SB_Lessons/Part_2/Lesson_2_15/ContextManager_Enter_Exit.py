import time


class Timer:
    def __init__(self) -> None:
        print('Run-time: ', end='')
        self.start = None

    def __enter__(self) -> 'Timer':
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time.time() - self.start)
        if [exc_type, exc_val, exc_tb]:
            return True


with Timer() as t1:
    print('Part 1')
    val_1 = 100 * 100 ** 1000000
    val_1 += 'qwerty'
    # some another code

with Timer() as t2:
    print('Part 2')
    val_2 = 200 * 200 ** 2000000
    # some another code

with Timer() as t3:
    print('Part 3')
    val_3 = 300 * 300 ** 3000000
    # some another code
