import asyncio
import logging

from ctc.protocols import compound_utils


async def example():
    logging.info("Compound")

    # TODO: get addresses automatically
    c_dai = "0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643"
    c_usdc = "0x39AA39c021dfbaE8faC545936693aC917d5E7563"

    asyncio.gather(
        compound_utils.compound_crud.async_get_borrow_apy(c_dai),
        compound_utils.compound_crud.async_get_borrow_apy(c_usdc),
    )
