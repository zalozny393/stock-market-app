import logging
import os

log = logging.getLogger(__name__)


log.warning("Debugger is used")
if os.environ.get("IS_OFFLINE") == "true" and os.environ.get("LOCAL_DEBUG") == "true":
    import debugpy

    debugpy.listen(5678)
    debugpy.wait_for_client()
