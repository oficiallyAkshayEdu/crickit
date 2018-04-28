import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(levelname)-8s %(filename)-20s %(funcName)-20s %(lineno)-3d  %(message)s',
#                     )
#
# critical = logging.critical
# error = logging.error
# warning = logging.warning
# info = logging.info
# debug = logging.debug


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

LOGS = [matchlog, serieslog, scriptlog, tosslog]

for each in LOGS:
    each.setLevel(logging.DEBUG)
    each.addHandler(ch)

