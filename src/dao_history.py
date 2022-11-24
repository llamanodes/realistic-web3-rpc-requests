from ctc import evm


async def dao_history(dao_address):
    # TODO: print dao.name()
    print("dao:", dao_address)

    proposals = await evm.async_get_events(
        contract_address=dao_address,
        event_name="ProposalCreated",
    )
    print("num proposals:", len(proposals))

    votes = await evm.async_get_events(
        contract_address=dao_address,
        event_name="VoteCast",
        include_timestamps=True,
    )
    print("num votes:", len(votes))


async def example():
    dao_address = "0x0bef27feb58e857046d630b2c03dfb7bae567494"

    await dao_history(dao_address)
