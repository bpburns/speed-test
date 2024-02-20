#!/bin/bash

OUTPUT_DIR=test_results

if [ -z ${SERVER} ]; then echo "Must specify SERVER"; exit 1; fi

echo Will connect to $SERVER

mkdir -p $OUTPUT_DIR

TS=$(date +%s)

# TCP tests
echo Running TCP send test
iperf3 -c $SERVER -J > $OUTPUT_DIR/$TS\_tcp_send.json

echo Running TCP receive test
iperf3 -c $SERVER -J --reverse > $OUTPUT_DIR/$TS\_tcp_receive.json

# UDP tests
echo Running UDP send test
iperf3 -c $SERVER -J -u > $OUTPUT_DIR/$TS\_udp_send.json

echo Running UDP receive test
iperf3 -c $SERVER -J -u --reverse > $OUTPUT_DIR/$TS\_udp_receive.json
