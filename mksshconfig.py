#!/bin/python

import json

json_data = open('/home/dotcloud/environment.json')
data = json.load(json_data)

configfile = open('/home/dotcloud/.ssh/config', 'a+')

configfile.write("host rtfd.static\n")
configfile.write("  User dotcloud\n")
configfile.write("  Port {0}\n".format(data['DOTCLOUD_STATIC_SSH_PORT']))
configfile.write("  HostName {0}\n".format(data['DOTCLOUD_STATIC_SSH_HOST']))
configfile.write("  StrictHostKeyChecking no\n")
configfile.write("  IdentityFile ~/data/dockeruser.key\n")

configfile.close()