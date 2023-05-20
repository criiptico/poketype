# print("Hello World!")


# Test code provided by AioPokeApi at https://beastmatser.github.io/aiopoke/
# Running this code to test how it works.

import asyncio
import aiopoke


async def main() -> None:
    async with aiopoke.AiopokeClient() as client:
        berry = await client.get_berry(1)
        print(berry)

        # An object can also have 'MinimalResources' as attributes
        # You can fetch those with .fetch(), for example:
        item = await berry.item.fetch()


asyncio.run(main())