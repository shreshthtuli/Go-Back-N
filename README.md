# Go-Back-N
A simple implementation of Go Back N protocol on Mininet network simulator


# Instructions for running go-back-N protocol on mininet:
```
1) sudo apt-get install tmux
2) tmux
3) python3 receiver.py <name_of_receiving_file>
4) ctrl+b then d = exits the tmux session
5) tmux
6) python3 sender.py <name_of_file_to_be_sent>
```

to exit both tmux session:
```
7) ctrl+d
8) tmux attach-session -t 0
9) ctrl+d
```

to view active tmux sessions:
```
10) tmux list-sessions
(should not show any session after closing all)
```
