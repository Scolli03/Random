# -*- coding: utf-8 -*-

import logging
from logging import Logger, Handler
import sys
import os
from typing import Union

def make_logger(name: str, location: str = '', logger_level: str = "debug", FileH: bool = True,
                file_level: str = "info", file_mode: str = 'w', file_format: str = 'default',
                ConsoleH: bool = True, console_level: str = "debug", console_format: str = 'default') -> Logger:
    """
    Creates and returns an instance of a logger with supplied settings

    Args:

        \tname (str): Logger and log file name

        \tlocation (str=''): Where to write the log file if not in running script dir

        \tlogger_level (str="debug"): Logger instance level as a string

        \tFileH (bool=True): Should logger instance have a file handler

        \tfile_level (str="info"): File handler level as a string

        \tfile_mode (str='w'): File handler mode, write or append - {'w' or 'a'}

        \tfile_format (str='default'): File handler logging format

        \tConsoleH (bool=True): Should the logger have a console handler

        \tconsole_level (str="debug"): Console handler level as a string

        \tconsole_format (str='default'): Console handler logging format

    Returns:

        \tLogger - the logger instance

    """

    logger = logging.getLogger(name)

    if FileH == True:

        add_file_handler(logger, file_level=file_level, file_mode=file_mode,
                         file_format=file_format, location=location)

    if ConsoleH == True:
        add_console_handler(logger, console_level=console_level,
                            console_format=console_format)

    set_level(logger, logger_level)

    return logger


def add_file_handler(logger: Logger, file_level: str, file_mode: str, file_format: str, location: str):
    """
    Adds a File Handler to the logging instance

    Args:

        \tlogger (Logger): The logger instance

        \tfile_level (str): Log level for the file handler as a string

        \tfile_mode (str): File handler mode, write or append - {'w' or 'a'}

        \tfile_format (str): File handler logging format

        \tlocation (str): Where to write the log file if not in running script dir

    """

    if location != "":
        filepath = os.path.join(location, "{}.log".format(logger.name))
    else:
        filepath = "{}.log".format(logger.name)

    filehandler = logging.FileHandler(filepath, file_mode, "utf8")

    set_level(filehandler, file_level)

    set_handler_format(filehandler, file_format)

    logger.addHandler(filehandler)


def add_console_handler(logger: Logger, console_level: str, console_format: str):
    """
    Adds a Console Hanlder to the logging instance

    Args:

        \tlogger (Logger): Logging instance

        \tconsole_level (str): Log level for the console handler as a string

        \tconsole_format (str): Console handler logging format

    """

    consolehandler = logging.StreamHandler()

    set_level(consolehandler, console_level)

    set_handler_format(consolehandler, console_format)

    logger.addHandler(consolehandler)


def set_handler_format(handler: Handler, format_string: str = "default"):
    """
    Set the logging format for the supplied handler

    Args:

        \thandler (Handler): File or Console handler

        \tformat_string (str="default"): logging format string

    """
    # set a format which is simpler for file use (this is the same as basic config but could be changed)
    if format_string == "default":
        handler_format = logging.Formatter('[%(asctime)s] {Line:%(lineno)d} %(levelname)s - %(message)s',
                                           '%m-%d %H:%M:%S')
    else:
        handler_format = logging.Formatter(format)

    handler.setFormatter(handler_format)


def set_level(handlerOrLogger:Union[Logger,Handler], level:str):
    """
    Sets logging level for either a Handler or Logger instance 

    Args:
        handlerOrLogger (Union[Logger,Handler]): Logger instance or Handler object
        level (str): logging level as string

    """
    if level == "debug":
        handlerOrLogger.setLevel(logging.DEBUG)
    elif level == "info":
        handlerOrLogger.setLevel(logging.INFO)
    elif level == "warning":
        handlerOrLogger.setLevel(logging.WARNING)
    elif level == "critical":
        handlerOrLogger.setLevel(logging.CRITICAL)
    elif level == "error":
        handlerOrLogger.setLevel(logging.ERROR)
    else:
        raise ValueError("There is no logging level called {}".format(level))


if __name__ == "__main__":
    # makes a logger called test, therefor the log file will be called Test.log
    # Since no location or other settings were called, default settings will  be used
    log = make_logger("Test")

    # this will be logged to the console only
    log.debug("this is debug test")

    # this will get logged to the console and to the log file
    log.error("this is error test")

    # This logger will have a name of Test2
    # It will only ever log to the console info level or above
    # it will only ever log errors to the log file
    # the log file will be located on the desktop
    log2 = make_logger("Test2", logger_level="info",
                       file_level="error",file_mode='a', location=r"C:\Users\shainc\Desktop")

    # This will not do anything as the default level is info or above
    log2.debug("log something for debug")

    # this will log to the console but not the file because the file_level is set for error or above
    log2.info("Something for info")

    # this will log to both the console and the file
    log2.error("Bad stuff happened")
