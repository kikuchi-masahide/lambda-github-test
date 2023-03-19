#!/bin/bash
cd $(dirname $0)
cd app/$1
while read wk
do
    ZIP_FILE=$1.zip
    if [ -e $ZIP_FILE ]; then
        rm ./${ZIP_FILE}
    fi
    zip -r ../${ZIP_FILE} * -x '*.git*'
done << END
app
END
