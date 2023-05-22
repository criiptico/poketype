# print("Hello World!")


# Test code provided by AioPokeApi at https://beastmatser.github.io/aiopoke/
# Running this code to test how it works.

import asyncio
import aiopoke


async def main() -> None:
    print("Hello world!")
    async with aiopoke.AiopokeClient() as client:
        berry = await client.get_berry(1)
        print(berry)

        # An object can also have 'MinimalResources' as attributes
        # You can fetch those with .fetch(), for example:
        # item = await berry.item.fetch() # This is the line that is making the program crash on line 22. I don't know what's wrong with this, but it doesn't work.
        print(berry.item.name)
        growth = berry.growth_time
        print(growth)

print("Under here.")
asyncio.run(main())
print("Over here.")