# -*- coding: utf-8 -*-

import logging
import sys
import os

# return a logger with the passed in name (typicaly the file name by passing in __name__)


class Logger():

	def __init__(self):

		# set a format which is simpler for file use (this is the same as basic config but could be changed)
		self.basicConfig = logging.Formatter('[%(asctime)s] {Line:%(lineno)d} %(levelname)s - %(message)s',
											'%m-%d %H:%M:%S')

	def make_logger(self, name, log_level='debug', FileH=True,file_level = 'info', ConsoleH=True, console_level = 'debug', log_format='defualt',location="Public"):
		"""Creates an instance of a logger with the supplied configurations
		
		Arguments:
			name {str} -- name of instance
		
		Keyword Arguments:
			log_level {str} -- main logger level (default: {'debug'})
			FileH {bool} -- add file handler (default: {True})
			file_level {str} -- level of file handler (default: {'info'})
			ConsoleH {bool} -- add console handler (default: {True})
			console_level {str} -- level of console handler (default: {'debug'})
			log_format {str} -- logger format (default: {'defualt'})
			location {str} -- location of file handler output (default: {"Public"})
		
		Returns:
			object -- configured logging instance
		"""

		logger = logging.getLogger(name)

		if FileH == True:
			self.add_file_handler(logger,file_level=file_level,log_format=log_format,location=location)

		if ConsoleH == True:
			self.add_console_handler(logger,console_level=console_level)

		self.set_level(logger, log_level)

		return logger

	def add_file_handler(self, logger, file_level='info', log_format='defualt', location='Public'):

		if location == 'Public':
			filepath = os.path.join(
				r"\\dc01\atos_programs\MCXL\Templates\2018\gom_scripts\Logs", '{}.log'.format(logger.name))

		elif location == 'Testing':
			filepath = os.path.join(r'C:\Users\shainc\Desktop\Git Repositories\2018\gom_scripts\Logs','{}.log'.format(logger.name))

		else:
			filepath = os.path.join(location, '{}.log'.format(logger.name))

		filehandler = logging.FileHandler(filepath, 'w', 'utf8')

		self.set_level(filehandler, file_level)

		self.set_format(filehandler)

		logger.addHandler(filehandler)

	def add_console_handler(self, logger, console_level='debug'):

		consolehandler = logging.StreamHandler(sys.stdout)

		self.set_level(consolehandler, console_level)

		self.set_format(consolehandler)

		logger.addHandler(consolehandler)

	def set_format(self, handler, format='defualt'):

		if format == 'defualt':
			handler.setFormatter(self.basicConfig)
		else:
			handler.setFormatter(format)

	def set_level(self, logger, level):
		if level == 'debug':
			logger.setLevel(logging.DEBUG)
		elif level == 'info':
			logger.setLevel(logging.INFO)
		elif level == 'warning':
			logger.setLevel(logging.WARNING)
		elif level == 'critical':
			logger.setLevel(logging.CRITICAL)
		elif level == 'error':
			logger.setLevel(logging.ERROR)
		else:
			raise ValueError(
				"There is no logging level called {}".format(level))


if __name__ == '__main__':
	log = Logger().make_logger('Test')
	log.debug('this is debug test')
	log.error('this is error test')
