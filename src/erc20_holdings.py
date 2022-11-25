from ctc import evm, rpc


async def get_holdings(erc20_addr, start_block, end_block):
    # get token transfers
    transfers = await evm.async_get_erc20_transfers(
        token=erc20_addr,
        event_name="Transfer",
        # start_block="",
        # end_block=end_block,
    )
    print("num transfers:", len(transfers))

    # get holdings of each address for a given block
    holdings = await evm.async_get_erc20_balances_from_transfers(
        transfers=transfers,
        # block=end_block,
    )
    print("num holdings:", len(holdings))

    raise NotImplementedError


async def example():
    fei_addr = "0x956f47f50a910163d8bf957cf5846d573e7f87ca"

    # TODO: use ctc to get the deploy block
    fei_deploy_block = 12125705

    head_block = await rpc.async_eth_block_number()
    print("head block:", head_block)

    await get_holdings(fei_addr, fei_deploy_block, head_block)
