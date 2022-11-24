from ctc.protocols import chainlink_utils


async def chainlink_feed_history(feed):
    # TODO: print feed description
    print("feed:", feed)

    data = await chainlink_utils.async_get_feed_data(feed)
    print("num data:", len(data))


async def example():
    feed = "0x31e0a88fecb6ec0a411dbe0e9e76391498296ee9"

    await chainlink_feed_history(feed)
