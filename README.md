# Wordpress rest api with Python

This is a short script that enables to use wordpress rest api with Python. It is meant mainly for posting.

This is a first version, hugily inspired by this video: https://www.youtube.com/watch?v=AS6EPzDyjhA

Unfortunately, some things suggested in the video had to be changed in order to make this work.


### How to use it?

Since the script is very simple, you just need to have all libraries and change these constants:

* url - url of your web made in wordpress, change only a hostname (the part before first single forward slash)
* cred - insert your username and password (not hardcoded credentials are recommended)
* url2 - url of your web, again change only a hostname
* post - this constant contain what you want to post with other useful informations


### Weak sposts

The regex used to capture the token is unsophisticated and may not work for every token combination. Be aware of this, maybe it will have to be changed.


### Prerequisites

It was written and successfully used in Python 3.7.4.


### Next versions

Because I am going to use it regularly, this is definately not a last version. But I did not want to wait, maybe it will be helpfull to someone even in this early state. 


