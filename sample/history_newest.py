#!/bin/env python
#-*- coding: utf-8 -*-

from history_all import *
                   
if __name__ == "__main__":
    accounts = get_accounts()
    
    for account in accounts :
        history_list = history(account)

        newest_cnt = min(5, len(history_list))
        print "acc : %sLast Use Commands : % d개" % (account, newest_cnt)
        if newest_cnt == 0:
            print "\tNothing use"
            
        i = 0
        while i < newest_cnt:
            print "\t%s\t%s" % history_list[i]
            i = i + 1
        print "-" * 70
