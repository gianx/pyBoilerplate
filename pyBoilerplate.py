#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ConfigParser
import datetime
import logging
import os
import signal
import socket
import sys
import traceback


def ctrlc_handler(signum,frame):
    msg = 'Sript interrotto manualmente dall''utente (CTRL-C)'
    try:
        logging.error(msg)
    except:
        print msg

def myencode(text):
    for charset in ['US-ASCII', 'ISO-8859-1', 'UTF-8']:
        try:
            out = text.encode(charset)
        except UnicodeError:
            pass
        else:
            return out

def exception_logger(ex, ex_traceback=None):
    if ex_traceback is None:
        ex_traceback = ex.__traceback__
    tb_lines = [line.strip().replace('\n','') for line in traceback.format_exception(ex.__class__, ex, ex_traceback)]
    return ': '.join(tb_lines[1:])

##############################################################
# MAIN
##############################################################

def main():
    # Initialization
    scriptname = os.path.basename(__file__).split('.')[:-1][0]
    conf_file = scriptname+".conf"
    log_file = datetime.datetime.today().strftime("%Y%m%d-"+scriptname+".log")
    hostname = socket.gethostname()
    conf = {}

    # Log initialization
    logging.basicConfig(filename=log_file, level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%Y/%m/%d %H:%M:%S')

    # CTRL+C management
    signal.signal(signal.SIGINT, ctrlc_handler)

    # Configuration parsing
    config = ConfigParser.ConfigParser()
    config.read(conf_file)
    for section in config.sections():
        for name,value in config.items(section):
            conf[name]=value

    # DEMO
    logging.debug('Debug message')
    logging.info('Info message')
    logging.warning('Warning message')
    logging.error('Erro message')
    logging.critical('Critical message')

    for x in conf:
        print "%s : %s"%(x, conf[x])

    try:
        x = 3/0
    except Exception as ex:
        _, _, ex_traceback = sys.exc_info()
        logging.error(exception_logger(ex, ex_traceback))
        sys.exit() # Only if critical

if __name__ == '__main__':
    main()
