import logging
import asyncio

from ctc.protocols import ens_utils


async def example():
    logging.info("ENS")

    # TODO: get a bunch of names automatically

    await asyncio.gather(
        ens_utils.async_resolve_name("vitalik.eth"),
        ens_utils.async_resolve_name("satoshiandkin.eth"),
        ens_utils.async_resolve_name("flashprofits.eth"),
    )
