import logging

# 5 levels of looging
# debug
# info
# warn (default)
# error
# critical

print(logging.getLogger())#<RootLogger root (WARNING)>
logging.basicConfig(filename="test1.txt", filemode="a", level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s %(created)s")

logger = logging.getLogger()
# logger.setLevel(logging.CRITICAL)

print(logging.getLogger())
logging.debug("this is debug")
logging.info("this is info")
logging.warning("this is warn")
logging.error("this is error")
logging.critical("this is critical")