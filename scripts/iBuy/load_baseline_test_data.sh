#!/bin/sh
#
# Copyright (c) 2006 Endeca Technologies Inc. All rights reserved.
# COMPANY CONFIDENTIAL
#

WORKING_DIR=`dirname ${0} 2>/dev/null`

. "${WORKING_DIR}/../config/script/set_environment.sh"
cp /home/iBuy/Endeca.zip ${ENDECA_PROJECT_DIR}/test_data/baseline/
chmod 777 ${ENDECA_PROJECT_DIR}/test_data/baseline/Endeca.zip

####################ARCHIVE FILES#############################
TIMESTAMP=`date +%Y%m%d_%H%M_%S`
CLIENT="iBuy"
mkdir -p /home/archive/${CLIENT}/$TIMESTAMP
cp ${ENDECA_PROJECT_DIR}/test_data/baseline/*  /home/archive/${CLIENT}/$TIMESTAMP/
find /home/archive/${CLIENT}/ -mtime +7 -exec rm -r {} \;
##################################################################


#START FILE CHECK
#FIRST Checks if New Data files have been loaded to the FTP if so, then it checks all the files for a minimum # of lines.  If the file doesn't have the required number of lines, the baseline does not run and a failure notification is sent
itemLINES=$(awk 'END { print NR }' $ENDECA_PROJECT_DIR/test_data/baseline/items.txt)
attrNUMLINES=$(awk 'END { print NR }' $ENDECA_PROJECT_DIR/test_data/baseline/attributes.txt)
hierNUMLINES=$(awk 'END { print NR }' $ENDECA_PROJECT_DIR/test_data/baseline/hierarchy.txt)

unzip ${ENDECA_PROJECT_DIR}/test_data/baseline/Endeca.zip
if [[ $? == 0 ]] ;
then
echo "Unzip was Successfull"
	if [ $itemLINES -gt 50000 ] 
	then
		if [ $attrNUMLINES -gt 600000 ]
		then
			if [ $hierNUMLINES -gt 2000 ]
			then
				echo "Good Files"
				cp ${ENDECA_PROJECT_DIR}/test_data/baseline/* ${ENDECA_PROJECT_DIR}/data/incoming/
				"${WORKING_DIR}/set_baseline_data_ready_flag.sh"
				exit 0
			else
				echo "SEVERE FAILURE - Hierarchy File is too Small!"
				echo "SEVERE FAILURE - Hierarchy File is too Small!" > ${ENDECA_PROJECT_DIR}/logs/baseline_update.out
				exit 1
			fi
		else
			echo "SEVERE FAILURE - Attributes File is too Small!"
			echo "SEVERE FAILURE - Attributes File is too Small!" > ${ENDECA_PROJECT_DIR}/logs/baseline_update.out
			exit 1
		fi
	else
		echo "SEVERE FAILURE - Items file is too Small!"
		echo "SEVERE FAILURE - Items file is too Small!" > ${ENDECA_PROJECT_DIR}/logs/baseline_update.out
		exit 1
	fi
else
	echo "Corrupt Zip file" 
	echo "Corrupt Zip File" > ${ENDECA_PROJECT_DIR}/logs/baseline_update.out
	exit 1
fi
#END FILE CHECK

