#!/bin/bash

# Deploy websites from buildbot

chmod -R ag+rX rendered/
DEPLOY_USER="www"
if [ $(git rev-parse --abbrev-ref HEAD) == 'stable' ]; then
  rsync -a --delete rendered/ $DEPLOY_USER@firefly.gnunet.org:~/stable/
else
  rsync -a --delete rendered/ $DEPLOY_USER@firefly.gnunet.org:~/stage/
fi
