#!/bin/bash
cd "$(dirname "$0")"
pip3 install -r requirements.txt
clear
python3 -m code_tester
exit $?
