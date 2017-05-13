ps -ef | grep "/usr/bin/python ./fred-data.py" | grep -v "grep" |awk '{print $2}' | xargs kill -9
sleep 5
./start-fred-data.sh
