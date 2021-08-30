#!/bin/bash

# Deploy websites from buildbot

chmod -R ag+rX rendered/
DEPLOY_USER="www"
if [ $(git rev-parse --abbrev-ref HEAD) == 'stable' ]; then
  rsync -a --delete rendered/ $DEPLOY_USER@gnunet.org:~/www_deployment/
else
  rsync -a --delete rendered/ $DEPLOY_USER@firefly.gnunet.org:~/stage/
fi
