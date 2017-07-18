# botlet_a_v01

This repository contains a small python script that runs a twitter bot to 
reply to any messages it is tagged in.

## Setup

The script uses the twython package for streaming twitter data and sending 
tweets. This can be downloaded using the apt-get command line tool:

```
$ sudo apt-get twython
```

If you have issues with this you can try updating apt-get with:

```
$ suo apt-get upgrade
```

Once twython is installed the repository can be downloaded by running:

```
$ git clone git@github.com:quentinjcm/botlet_a_v01.git
```

## Usage

The script requires command line input that is the path to the file that 
contains the private data that script required for the bot to run and is 
in the following format:

```
api_key=ifsjnagghrthb43r9tu45g
api_secret=43t8frefnv894rmuguvtr9jg45jg9urt
access_token=8fbvtbb4w7834hpag.bner943fenrag45g30esfqazx
access_token_secret=vnrueaohvosiiok34945g9
screen_name=twitter_bot_handle
```

The script can be run by moving into the cloned repository and running:

```
$ python tweet_steamer.py path/to/data_file.txt
```
