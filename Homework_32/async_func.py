import asyncio
import aiohttp


async def async_get_request(delay):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://httpbin.org/delay/{delay}') as response:
            result = await response.text()
            print(f"request with delay {delay} second DONE")
            return result


async def first_coroutines(delay):
    print(f"first_coroutines started with delay {delay}")
    result = await async_get_request(delay)
    result = "result from first_coroutines " + result
    print(result)


async def second_coroutines(delay):
    print(f"second_coroutines started with delay {delay}")
    result = await async_get_request(delay)
    result = "result from second_coroutines " + result
    print(result)
    first_future.set_result(12)


async def third_coroutines():
    print(f"third_coroutines started and wait for second_coroutines")
    delay = await first_future
    result = await async_get_request(delay)
    result = "result from third_coroutines " + result
    print(result)
    second_future.set_result(1)


async def fourth_coroutines():
    print(f"fourth_coroutines started and wait for third_coroutines")
    delay = await second_future
    result = await async_get_request(delay)
    result = "result from fourth_coroutines " + result
    print(result)


async def fifth_coroutines(event_loop, delay):
    print(f"fifth_coroutines started with delay {delay}")
    result = await async_get_request(delay)
    result = "result from five_coroutines " + result
    print(result)
    event_loop.stop()


event_loop = asyncio.get_event_loop()

first_future = asyncio.Future()
second_future = asyncio.Future()

event_loop.create_task(first_coroutines(2))
event_loop.create_task(second_coroutines(20))
event_loop.create_task(third_coroutines())
event_loop.create_task(fourth_coroutines())
event_loop.create_task(fifth_coroutines(event_loop, 10))

event_loop.run_forever()
