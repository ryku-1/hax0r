#!/bin/bash

sudo echo "nameserver 8.8.8.8" >> /etc/resolv.conf

sudo service networking restart
