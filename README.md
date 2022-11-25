# webssh.sh
Shell Helpers about WebSSH

## Installation
```pip install webssh-sh```

## Usage
### wshcopy
Helper wich allow you to write to your own terminal clipboard (on your computer) through your remote terminal connection.

```echo "WebSSH is awesome!" | wshcopy```

If you use tmux >= 3.3 you will need either :
* `set -g allow-passthrough on` **THEN** `echo "WebSSH is awesome!" | wshcopy -t tmux`
* **OR**
* `set -g set-clipboard on` **THEN** `echo "WebSSH is awesome!" | wshcopy -t default`