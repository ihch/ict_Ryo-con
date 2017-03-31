#! /usr/bin/python3
# -*- coding:utf-8 -*-
import csv

filename = 'data'

def filename_check(filename=None):
    """
    :type filename: str
    :rtype: bool
    """
    if filename is None:
        print("None file")
        return False
    return True

def open_csv(filename=None, opentype='r'):
    """
    :type filename: str
    :type opentype: str
        read    -> 'r'
        write   -> 'w'
        append  -> 'a'
    :rtype: fileobject
    """
    if not filename_check(filename=filename):
        return
    return open(filename+'.csv', opentype)

