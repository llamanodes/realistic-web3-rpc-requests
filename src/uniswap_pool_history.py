import asyncio

from ctc.protocols import uniswap_v2_utils


async def uniswap_pool_history(pool):
    # TODO: print pool tokens
    print("pool:", pool)

    swaps_f = uniswap_v2_utils.async_get_pool_swaps(pool)
    mints_f = uniswap_v2_utils.async_get_pool_mints(pool)
    burns_f = uniswap_v2_utils.async_get_pool_burns(pool)

    (swaps, mints, burns) = await asyncio.gather(swaps_f, mints_f, burns_f)

    print("num swaps:", len(swaps))
    print("num mints:", len(mints))
    print("num burns:", len(burns))


async def example():
    pool = "0x94b0a3d511b6ecdb17ebf877278ab030acb0a878"

    await uniswap_pool_history(pool)
