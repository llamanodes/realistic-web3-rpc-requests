import asyncio
import sys
import time

from . import chainlink_feed_history, dao_history, erc20_holdings, uniswap_pool_history


async def main() -> int:
    await asyncio.gather(
        chainlink_feed_history.example(),
        dao_history.example(),
        erc20_holdings.example(),
        uniswap_pool_history.example(),
    )

    return 0


if __name__ == "__main__":
    # TODO: configure logging

    t1 = time.perf_counter()

    exit_code = asyncio.run(main())

    t2 = time.perf_counter()

    print(f"Total time elapsed: {t2-t1:0.2f} seconds")

    sys.exit(exit_code)
