# Flash Helper

Tool to help the process to get the files from a git workspace and
bazel into a specific USB drive.

- `pydev`
- `zenity`
- `gitpython`

Put the script in a locatio where only root can access. The command needs to
be run as sudo, then if the regular user account is compromised the script
contents could be changed and run as su.

## zenity




## udev

Create a rule for the USB here are the guidelines for rules in `/etc/udev/rules.d`

* Files should be named `xx-descriptive-name.rules` where the `xx` part can be
  * `<60`: most user rules; to prevent override by default rules use `:=`
  * The last one cannot access persistent information such as `vol_id`
  * `<70`: rules that run helpers such as `vol_id` to populate udev db
  * `<90`: Rules that run other programs probably using information from udeb db
  * `>=90`: Rules that should run last

In this case: `88-flash-helper.rules`



https://hackaday.com/2009/09/18/how-to-write-udev-rules/