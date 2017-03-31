#! /usr/bin/python3
# -*- coding:utf-8 -*-
import open_csv

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
        print("user_init error: user_info not enough {}" \
            .format([user_data[i] for i, x in enumerate(user_info) if x is None]))
        return False
        # logger.debug("user_init error: user_info not enough {}".format([user_data[i] for i, x in enumerate(user_info)]))
    elif fa == None:
        print("user_init error: file is None")
        return False
        # logger.debug("user_init error: file is None")
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
        print("update_info error: user_info not enough")
        return False
        # logger.debug("update_info error: user_info not enough {}".format([user_data[i] for i, x in enumerate(user_info)]))
    elif fr is None:
        print("update_info error: None file")
        return False
        # logger.debug("update_info error: None file")
    elif change_list is None:
        print("update_info error: None change_list")
        return False
        # logger.debug("update_info error: None change_list")
    else:
        reader = open_csv.csv.reader(fr)
        res = list()

        for i, row in enumerate(reader):
            insert = row
            if user_info[0] in row:
                for j, change in enumerate(change_list):
                    insert[change] = user_info[j + 1]
            else:
                print("update_info error: None user")
                return False
                # logger.debug("update_info error: None user")
            res.append(insert)

        fr.close()
        fw = open_csv.open_csv(filename, 'w')
        writer = open_csv.csv.writer(fw, lineterminator='\n')
        writer.writerows(res)
        fw.close()
        return True

def get_data(fr=None):
    if fr is None:
        print("get_data error: None file")
        # logger.debug("get_data error: None file")
        return None
    else:
        reader = open_csv.csv.reader(fr)
        res = list()
        for row in reader:
            res.append(row)
        return res

