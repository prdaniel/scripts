#!/bin/sh
#
# Copyright (c) 2006 Endeca Technologies Inc. All rights reserved.
# COMPANY CONFIDENTIAL
#

if grep "INFO: Applying index to dgraphs in restart group '1'." /usr/local/endeca/apps/tmi20130815/logs/test.out
then
	echo 'Run Top Output' > /usr/local/endeca/apps/tmi20130815/logs/topCheck.txt
	scp /usr/local/endeca/apps/tmi20130815/logs/topCheck.txt eodsvc@moonraker-mdex-a.endecaondemand.net:/usr/local/endeca/apps/tmi20130815/
  if grep "INFO: Applying index to dgraphs in restart group '2'." /usr/local/endeca/apps/tmi20130815/logs/test.out; then
    ssh eodsvc@moonraker-mdex-a.endecaondemand.net 'rm /usr/local/endeca/apps/tmi20130815/logs/topCheck.txt'
    exit 0
  else
    exit 0
  fi
else
exit 0
fi