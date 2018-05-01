import logging


# create console handler (ch)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(name)-7s%(levelname)-8s %(filename)-20s %(funcName)-20s %(lineno)-3d  %(message)s')
ch.setFormatter(formatter)


# declare all different loggers
matchlog = logging.getLogger('MATCH')
serieslog = logging.getLogger('SERIES')
scriptlog = logging.getLogger('SCRIPT')
tosslog = logging.getLogger('TOSS')
inningslog = logging.getLogger('INNINGS')

LOGS = [matchlog, serieslog, scriptlog, tosslog, inningslog]

# default logging level = INFO
for each in LOGS:
    each.setLevel(logging.INFO)
    each.addHandler(ch)

def debug(object, classname):
    logger = getattr(object, ("_" + classname + "__logger"))
    for prop in object.__slots__:
        if prop.startswith("__"):
            prop = "_" + classname +prop
            logger.debug("{}: {}".format(prop.title(), getattr(object, prop)))
        else:
            logger.debug("{}_{}: {}".format(classname, prop.title(), getattr(object, prop)))