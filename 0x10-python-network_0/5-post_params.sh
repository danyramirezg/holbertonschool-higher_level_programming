#!/bin/bash
# Takes in a URL, sends a POST request to the passed URL, and displays the body of the response. A variable email must be sent with the value hr@holbertonschool.com
curl -sX POST -d "email=hr@holbertonschool.com&&subject=I will always be here for PLD" "$1"