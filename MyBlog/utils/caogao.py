from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio


async def async_job():
    while True:
        print(1111)
        await asyncio.sleep(1)



# 创建异步调度器对象
scheduler = AsyncIOScheduler()

scheduler.add_job(async_job, 'interval', seconds=5)

scheduler.start()


async def run_scheduler():
    while True:
        await asyncio.sleep(1)
        scheduler.print_jobs()


loop = asyncio.get_event_loop()
loop.run_until_complete(run_scheduler())
