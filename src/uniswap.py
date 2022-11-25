import asyncio
import logging

from ctc.protocols import uniswap_v2_utils


async def uniswap_pool_history(pool):
    # TODO: print pool tokens
    logging.info("pool %s:", pool)

    swaps_f = uniswap_v2_utils.async_get_pool_swaps(pool)
    mints_f = uniswap_v2_utils.async_get_pool_mints(pool)
    burns_f = uniswap_v2_utils.async_get_pool_burns(pool)

    (swaps, mints, burns) = await asyncio.gather(swaps_f, mints_f, burns_f)

    logging.info("num swaps: %s", len(swaps))
    logging.info("num mints: %s", len(mints))
    logging.info("num burns: %s", len(burns))


async def example():
    logging.info("Uniswap")

    # TODO: get a bunch of pools automatically
    pool = "0x94b0a3d511b6ecdb17ebf877278ab030acb0a878"

    await uniswap_pool_history(pool)
