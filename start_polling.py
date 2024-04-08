import asyncio

from commands import market_dp


async def start(dispatcher):
    event_loop.create_task(dispatcher.start_polling())


event_loop = asyncio.get_event_loop()
for dispatcher in [market_dp]:
    event_loop.run_until_complete(start(dispatcher))

event_loop.run_forever()
