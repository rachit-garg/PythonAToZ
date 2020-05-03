import logging
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s : %(lineno)d] %(message)s',level=logging.WARN,filename='logs.txt')
logger = logging.getLogger('test_logger')
logger.info('This will not showed up')
logging.warning('This Will')
logging.debug('This is a debug message.')
logging.critical('A critical error occurred')

from datetime import datetime , timezone, timedelta
print(datetime.now())
print(datetime.now(timezone.utc))

today=datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)
print(tomorrow)


