import asyncio
import time
import os

CONST = 0.01


async def f(*data):
    for d in data:
        print(f"{d[0]} started the 1 task.")
        await asyncio.sleep(CONST * d[1])
        print(f"{d[0]} moved on to the defense of the 1 task.")
        await asyncio.sleep(CONST * d[2])
        print(f"{d[0]} completed the 1 task.")
        print(f"{d[0]} is resting.")
        await asyncio.sleep(CONST * 5)
        print(f"{d[0]} started the 2 task.")
        await asyncio.sleep(CONST * d[3])
        print(f"{d[0]} moved on to the defense of the 2 task.")
        await asyncio.sleep(CONST * d[4])
        print(f"{d[0]} completed the task 2.")


async def interviews(*data):
    tasks = [asyncio.create_task(f(d)) for d in data]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    if os.name == "nt":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
t0 = time.time()
asyncio.run(interviews(*data))
print(time.time() - t0)
