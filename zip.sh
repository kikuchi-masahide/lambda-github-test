#!/bin/bash
cd $(dirname $0)
while read wk
do
    ZIP_FILE=${wk}.zip
    if [ -e $ZIP_FILE ]; then
        rm ./${ZIP_FILE}
    fi
    cd $wk
    zip -r ../${ZIP_FILE} * -x '*.git*'
    cd ..
done << END
app
END
