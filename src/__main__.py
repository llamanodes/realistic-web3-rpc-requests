import asyncio
import sys
import time
import logging

# TODO: 4byte? cg? fei? gnosis? llama? rari?
from . import (
    aave_v2,
    balancer,
    chainlink,
    compound,
    curve,
    dao,
    ens,
    erc20,
    uniswap,
    yearn,
)


async def main() -> int:
    await aave_v2.example()
    await balancer.example()
    await chainlink.example()
    await compound.example()
    await curve.example()
    await dao.example()
    await ens.example()
    # await erc20_holdings.example()
    await uniswap.example()
    await yearn.example()

    return 0


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )

    t1 = time.perf_counter()

    exit_code = asyncio.run(main())

    t2 = time.perf_counter()

    logging.info(f"Total time elapsed: {t2-t1:0.2f} seconds")

    sys.exit(exit_code)
