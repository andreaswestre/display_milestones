#! /bin/sh
{
git pull
} 1>/dev/null 2>&1

python3 display_milestones.py
#python3 display_milestones.py

./display.sh
