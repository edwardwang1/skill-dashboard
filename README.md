## skill-dashboard
Skill to interact with [Pi-Dashboard](https://github.com/edwardwang1/Pi-Dashboard).

## Requirements
This skill and Pi-Dashboard has been confirmed to work on a Raspberry Pi 3B+, running Raspbian Strech.

## Installation
Follow the [instructions](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/linux) to install Mycroft on Linux. Once Mycroft is installed, copy this folder into /opt/mycroft/skills.

Additionally, [Pyro4](https://pypi.org/project/Pyro4/) must be installed into the Mycroft virtual environment so that Mycroft can communicate with Pi-Dashboard. 

Navigate to the mycroft-core directrory: `cd mycroft-core`

Enable the virtual environment: `mycroft-core$ source .venv/bin/activate`

Install Pyro4 via pip: `(.venv) pi@raspberrypi:~/mycroft-core$ pip install Pyro4`

## Description 
This skill allows users to interact with Pi-Dashboard through voice commands. 

## Examples 
* "Hide calendar"
* "Show clock"
* "Note add five eggs"
* "Note remove one"

## Credits 
Edward Wang
