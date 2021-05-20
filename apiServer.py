from flask import Flask, jsonify
import logging
from logging.config import fileConfig
from configparser import ConfigParser
import os
import sys
import csv


app = Flask(__name__)


def readConfig(configFile):
    try:
        if os.path.exists(os.path.join('./', configFile)):
            parserData = ConfigParser()
            parserData.read(os.path.join('./', configFile))
            return parserData
        else:
            logger.error('Config file {} not found. Ensure that it exists in the same directory'.format(configFile))
    except Exception as e:
        logger.error('Error occurred while trying to read the config file.'.format(str(e)))


def configureLogging(configFile):
    try:
        if os.path.exists(os.path.join('./', configFile)):
            fileConfig('logging_config.ini', disable_existing_loggers=True)
            loggerObj = logging.getLogger()
            return loggerObj
        else:
            print('Logging Config not found.')
            sys.exit(1)
    except Exception as e:
        print('Error occurred while trying to read logging config. {}'.format(str(e)))
        sys.exit(1)


@app.route('/<csvFile>')
def gerData(csvFile):
    if os.path.exists(os.path.join('./', csvFile)):
        with open(os.path.join(parser.get('Global', 'Output_path')), 'r') as infile:
            csvData = csv.reader(infile)
    else:
        return {'error': 'File not found'}, 404


if __name__ == '__main__':
    parser = readConfig('init.conf')
    logger = configureLogging('logging_config.ini')
    app.run(debug=True, port=5555, host='0.0.0.0')
