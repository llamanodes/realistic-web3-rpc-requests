import logging

from ctc.protocols import aave_v2_utils


async def example():
    logging.info("Aave")

    # don't do these in parallel since they print things
    await aave_v2_utils.aave_summaries.async_print_aave_addresses()
    await aave_v2_utils.async_print_token_markets_summary()
