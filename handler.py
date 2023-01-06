import os


if os.environ.get("IS_OFFLINE") == "true" and os.environ.get("LOCAL_DEBUG") == "true":
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()


def get_stock(event, context):
    return {"symbol": event["arguments"]["symbol"]}
