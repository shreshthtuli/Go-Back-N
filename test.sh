#!/bin/bash

echo "starting test"
tmux new-session -d -s my_session
echo "inside new session"
touch a.txt
echo "executed commands"
# tmux detach
echo "detached from session"
# tmux kill-session -s my_session
# tmux list-sessions
echo "hello"

tmux list-sessions

