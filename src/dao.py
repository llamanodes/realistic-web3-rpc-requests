import logging

from ctc import evm


async def dao_history(dao_address):
    # TODO: print dao.name()
    logging.info("dao: %s", dao_address)

    proposals = await evm.async_get_events(
        contract_address=dao_address,
        event_name="ProposalCreated",
    )
    logging.info("num proposals: %s", len(proposals))

    votes = await evm.async_get_events(
        contract_address=dao_address,
        event_name="VoteCast",
        include_timestamps=True,
    )
    logging.info("num votes: %s", len(votes))


async def example():
    logging.info("DAO")

    dao_address = "0x0bef27feb58e857046d630b2c03dfb7bae567494"

    await dao_history(dao_address)
