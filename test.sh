#!/bin/bash

echo "starting test"
tmux new-session -s my_session
echo "inside new session"
touch a.txt
echo "executed commands"
tmux detach -s my_session
echo "detached from session"
# tmux kill-session -s my_session
# tmux list-sessions
echo "hello"

tmux list-sessions

sudo mn --custom topo.py --topo linear --controller=remote,ip=127.0.0.1 --link tc,bw=1,delay=3,loss=1
