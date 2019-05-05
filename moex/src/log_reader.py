import datetime
import re

def reader():
    #path to logfile with statistics test
    file_name = "medium.log"
    var = []

    with open(file_name, "r",encoding='utf-8', errors='ignore') as f:
        f = f.readlines()
    return(f)
