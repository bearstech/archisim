#!/bin/sh

apt-get update
apt-get install --yes openssh-server
mkdir -p /root/.ssh
