import asyncio

async def count(x):
    print(x)
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(count(3), count(2), count(1))

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Executed in {elapsed:0.2f} seconds.")