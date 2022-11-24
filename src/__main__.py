import asyncio
import sys
import time

from src import all_token_transfers, dao_proposals_and_votes


async def main() -> int:
    print("hello, world!")

    await asyncio.gather(all_token_transfers.example(), dao_proposals_and_votes.example())

    return 0


if __name__ == '__main__':
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
