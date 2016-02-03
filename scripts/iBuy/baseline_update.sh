#!/bin/sh
#
# Copyright (c) 2006 Endeca Technologies Inc. All rights reserved.
# COMPANY CONFIDENTIAL
#

WORKING_DIR=`dirname ${0} 2>/dev/null`

. "${WORKING_DIR}/../config/script/set_environment.sh"

mv $ENDECA_PROJECT_DIR/logs/baseline_update.out $ENDECA_PROJECT_DIR/logs/baseline 2>/dev/null

"${WORKING_DIR}/runcommand.sh" BaselineUpdate run 2>&1 | tee -a "${ENDECA_PROJECT_DIR}/logs/baseline_update.out"

##########################email notifications#####################################
/home/tmi/bin/emailGenHTML.sh $ENDECA_PROJECT_DIR/logs/baseline_update.out $ENDECA_PROJECT_NAME "Baseline update" "iBuy" $ENDECA_PROJECT_DIR/logs/email.txt $ENDECA_PROJECT_DIR/logs/status.txt
if [ -f $ENDECA_PROJECT_DIR/logs/status.txt ];
then
/home/tmi/bin/sendMailAlertFileMessageHTML.sh "FAILURE [iBuy-Production] EOD Baseline Update Notification" $ENDECA_PROJECT_DIR/logs/email.txt $ENDECA_PROJECT_DIR/logs/baseline_update.out "notify@thanxmedia.com"
else
/home/tmi/bin/sendMailAlertFileMessageHTML.sh "SUCCESS [iBuy-Production] EOD Baseline Update Notification" $ENDECA_PROJECT_DIR/logs/email.txt $ENDECA_PROJECT_DIR/logs/baseline_update.out "notify@thanxmedia.com"
fi
# client notifications without logs
/home/tmi/bin/sendMailAlertMessageHTML.sh "EOD Baseline Update Notification" $ENDECA_PROJECT_DIR/logs/email.txt "msias@thanxmedia.com"

rm -f $ENDECA_PROJECT_DIR/logs/email.txt
if [ -f $ENDECA_PROJECT_DIR/logs/status.txt ];
then
   rm -f $ENDECA_PROJECT_DIR/logs/status.txt
fi
###################################################################################