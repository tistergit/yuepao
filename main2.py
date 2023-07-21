import asyncio

async def q():
    print("Why can't programmers tell jokes?")
    await asyncio.sleep(3)
    print("q 2")

async def a():
    print("Timing!")

async def main():
    await asyncio.gather(q(), a())

asyncio.run(main())