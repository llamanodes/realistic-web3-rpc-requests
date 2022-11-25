import asyncio
import logging

from ctc.protocols import curve_utils


async def example():
    logging.info("Curve")

    await asyncio.gather(
        curve_utils.async_get_base_pools(),
        curve_utils.async_get_plain_pools(),
        curve_utils.async_get_meta_pools(),
    )
