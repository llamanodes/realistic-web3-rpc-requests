import logging

from ctc.protocols import chainlink_utils


async def chainlink_feed_history(feed):
    # TODO: print feed description
    logging.info("feed: %s", feed)

    data = await chainlink_utils.async_get_feed_data(feed)
    logging.info("num data: %s", len(data))


async def example():
    logging.info("Chainlink")

    # TODO: get a bunch of feeds automatically
    feed = "0x31e0a88fecb6ec0a411dbe0e9e76391498296ee9"

    await chainlink_feed_history(feed)
