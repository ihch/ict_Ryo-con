#! /usr/bin/python3
# -*- coding:utf-8 -*-
import open_csv
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

filename = open_csv.filename
user_data = ['user_name', 'major', 'minor', 'notice', 'atnd']

def user_init(user_info=None, fa=None):
    """
    :type user_info: [str, str, str, str, str]
                    ['user_name', 'major', 'minor', 'notice', 'atnd']
    :type fa: fileobject
    :rtype: None
    """
    if None in user_info:
        logger.debug("user_init error: user_info not enough {}"
            .format([user_data[i] for i, x in enumerate(user_info) if x is None]))
        return False
    elif fa == None:
        logger.debug("user_init error: file is None")
        return False
    else:
        writer = open_csv.csv.writer(fa, lineterminator='\n')
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
        return False
    elif fr is None:
        logger.debug("update_info error: None file")
        return False
    elif change_list is None:
        logger.debug("update_info error: None change_list")
        return False
    else:
        reader = open_csv.csv.reader(fr)
        res = list()

        for i, row in enumerate(reader):
            insert = row
            if user_info[0] in row:
                for j, change in enumerate(change_list):
                    insert[change] = user_info[j + 1]
            else:
                logger.debug("update_info error: None user")
                return False
            res.append(insert)

        fr.close()
        fw = open_csv.open_csv(filename, 'w')
        writer = open_csv.csv.writer(fw, lineterminator='\n')
        writer.writerows(res)
        fw.close()
        return True

def get_data(fr=None):
    if fr is None:
        logger.debug("get_data error: None file")
        return None
    else:
        reader = open_csv.csv.reader(fr)
        res = list()
        for row in reader:
            res.append(row)
        return res

