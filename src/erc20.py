import logging

from ctc import evm


async def get_holdings(erc20_addr):
    # TODO: this gives an error
    transfers = await evm.async_get_erc20_transfers(
        token=erc20_addr,
        event_name="Transfer",
    )
    logging.info("num transfers: %s", len(transfers))

    holdings = await evm.async_get_erc20_balances_from_transfers(
        transfers=transfers,
    )
    logging.info("num holdings: %s", len(holdings))

    raise NotImplementedError


async def example():
    logging.info("ERC20")

    fei_addr = "0x956f47f50a910163d8bf957cf5846d573e7f87ca"
    logging.info("fei: %s", fei_addr)

    await get_holdings(fei_addr)
