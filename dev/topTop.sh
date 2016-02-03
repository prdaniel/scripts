#!/bin/sh
#
# Copyright (c) 2006 Endeca Technologies Inc. All rights reserved.
# COMPANY CONFIDENTIAL
#

if [ -f /usr/local/endeca/apps/tmi20130815/topCheck.txt]
then
	 top -n 1 -b >> /usr/local/endeca/apps/tmi20130815/logLog.txt
	 exit 0
else
exit 0
fi