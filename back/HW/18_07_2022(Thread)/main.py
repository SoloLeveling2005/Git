import asyncio
import multiprocessing
import threading
import time
import aiohttp
import requests
import json


def get_data(int_data):
    url = "https://jsonplaceholder.typicode.com/posts/" + str(int_data)
    response = requests.get(url)
    json_data = response.content.decode()
    return json_data

async def async_get_data(int_data):
    url = "https://jsonplaceholder.typicode.com/posts/" + str(int_data)
    response = requests.get(url)
    json_data = response.content.decode()
    return json_data


def get_time(func):
    def decorator(*args, **kwargs):
        time_start = time.perf_counter()
        res = func(*args, **kwargs)  # ядро декорируемой функции
        print(f'функция потратила времени: {time.perf_counter() - time_start}')
        return res


    return decorator

# @get_time
def one(i):
    x = get_data(i)
    print(x)
    with open('data.json', 'w') as f:
        json.dump(x, f)
    return x




# one()
@get_time
def two():
    thread_list = [threading.Thread(target=one, args=(x,), kwargs={}) for x in range(1, 11)]
    for i in thread_list:
        i.start()
    for i in thread_list:
        i.join()



@get_time
def three():
    process_list = [multiprocessing.Process(target=one, args=(x,), kwargs={}) for x in range(1, 11)]
    for i in process_list:
        i.start()
    for i in process_list:
        i.join()

response_list = []
async def async_download_image(i):

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://jsonplaceholder.typicode.com/posts/"+i, headers=headers) as await_response:
            response = await await_response.json()
            print(response)
            response_list.append(response)

    with open('data.json', 'w') as f:
        json.dump(response_list, f)

@get_time
def four():
    print("Выдает ошибку но работает \n")
    async def tasks_generator():  # корутины - coro  - задачи с задержкой по выполнению и возврату
        await asyncio.gather(
            *[async_download_image(f"{x}") for x in range(1, 10)]
        )

    loop = asyncio.get_event_loop()  # Выдает ошибку но работает
    loop.run_until_complete(tasks_generator())  # Выдает ошибку но работает


if __name__ == "__main__":
    # one(1)
    # two()
    # three()
    # four()
    pass

