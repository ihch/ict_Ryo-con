#! /usr/bin/python3
import csv
from logging import getLogger, StreamHandler, DEBUG
import open_csv

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

FILENAME = open_csv.FILENAME
USER_DATA = ['user_name', 'major', 'minor', 'notice', 'atnd']


def user_init(user_info=None, fa=None):
    """
    :type user_info: [str, str, str, str, str]
                    ['user_name', 'major', 'minor', 'notice', 'atnd']
    :type fa: fileobject
    :rtype: None
    """
    if None in user_info:
        logger.debug("user_init error: user_info not enough {}".format(
                [USER_DATA[i] for i, x in enumerate(user_info) if x is None]))
        return False
    elif fa is None:
        logger.debug("user_init error: file is None")
        return False
    else:
        writer = csv.writer(fa, lineterminator='\n')
        writer.writerow(user_info)
        return True


def update_info(user_info=None, fr=None, change_list=None):
    """
    :type user_info: [str, str]
                    ['user_name', 'major', 'minor']
                    ['user_name', 'notice']
                    ['user_name', 'atnd']
    :type fr: fileobject
    :rtype: None
    """
    if None in user_info:
        logger.debug("update_info error: user_info not enough")
        logger.debug(user_info)
        return False
    elif fr is None:
        logger.debug("update_info error: None file")
        return False
    elif change_list is None:
        logger.debug("update_info error: None change_list")
        return False
    else:
        reader = csv.reader(fr)
        res = list()

        isSuccess = False
        for i, row in enumerate(reader):
            insert = row
            if user_info[0] in row:
                isSuccess = True
                for j, change in enumerate(change_list):
                    insert[change] = user_info[j + 1]
            res.append(insert)
        if not isSuccess:
            logger.debug("update_info error: None user")
            return False

        fr.close()
        fw = open_csv.open_csv(FILENAME, 'w')
        writer = csv.writer(fw, lineterminator='\n')
        writer.writerows(res)
        fw.close()
        return True


def get_data(fr=None):
    if fr is None:
        logger.debug("get_data error: None file")
        return None
    else:
        reader = csv.reader(fr)
        res = list()
        for row in reader:
            res.append(row)
        return res
