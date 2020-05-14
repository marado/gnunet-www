#!/bin/bash

# Deploy websites from buildbot

chmod -R ag+rX rendered/
DEPLOY_USER="stage"
if [ $(git rev-parse --abbrev-ref HEAD) == 'stable' ]; then
  DEPLOY_USER="www"
fi
rsync -a --delete rendered/ $DEPLOY_USER@gnunet.org:~/www_deployment/
