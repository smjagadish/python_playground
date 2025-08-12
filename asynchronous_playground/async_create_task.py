import asyncio
import random


async def doJob(val:int)->int :
    new_val = val * random.randint(10,65)
    print(f' async task generated new_val : {new_val}')
    await asyncio.sleep(5) # pauses the co-routine and event loop picks any other co-routine for execution
    return new_val

async def main():
    data = input('enter the values in comma separated format')
    vals_data = [int(v) for v in data.split(sep=',')]
    outputs = [asyncio.create_task(doJob(val)) for val in vals_data] # scheduled and run immediately by the event loop
    results = await asyncio.gather(*outputs) # awaiting the tasks to be completed and results gathered. if not done, no guarantee the co-routines ran to completion
    print(results)

if __name__ == '__main__':
    asyncio.run(main()) # starts the main event loop

