#!/bin/sh
#
# Copyright (c) 2006 Endeca Technologies Inc. All rights reserved.
# COMPANY CONFIDENTIAL
#

WORKING_DIR=`dirname ${0} 2>/dev/null`
. "${WORKING_DIR}/../config/script/set_environment.sh"

curl -X get http://admin:\!Thanx29@skyfall-indexer.endecaondemand.net:8006/ifcr/sites/${ENDECA_PROJECT_NAME} > ${ENDECA_PROJECT_DIR}/control/check_app_status.txt
if grep "pages" ${ENDECA_PROJECT_DIR}/control/check_app_status.txt
then
	echo 'Baseline process starting'
    "${WORKING_DIR}/load_baseline_test_data.sh"
	if [[ $? == 1 ]] ; then
		echo "Baseline Failed on data"
		exit 1
	else
    "${WORKING_DIR}/dimension_creation_py.sh"
    "${WORKING_DIR}/baseline_update.sh"
    "${WORKING_DIR}/promote_content.sh"
    "${WORKING_DIR}/experience_manager_backup.sh"
   # Below line deletes the files from the test_data/baseline and FTP to prevent the baseline from running if they have not uploaded new files --drk
    rm -f /usr/local/endeca/apps/tmi20130122/test_data/baseline/*.*
    rm -f /home/iBuy/*.*
	fi
else
	echo 'Workbench error, aborting mission'
	/home/tmi/bin/sendMailAlertMessage.sh "Workbench is down or the Workbench application directory in the repository is missing for ${ENDECA_PROJECT_NAME} " ${ENDECA_PROJECT_DIR}/control/check_app_status.txt "helpdesk@thanxmedia.com"
fi

rm ${ENDECA_PROJECT_DIR}/control/check_app_status.txt