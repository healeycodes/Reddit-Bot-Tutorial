This repository contains the files that accompany [my tutorial](https://healeycodes.github.io/tutorial/python/beginners/webdev/2019/03/25/reddit-bot-tutorial.html) for writing a Reddit bot!

<br>

![](https://github.com/healeycodes/Reddit-Bot-Tutorial/blob/master/header.png)

<br>

These brief instructions should get you up and running. Refer to my tutorial for a complete walkthrough 😊

Remember to follow Reddit's [bottiquette](https://www.reddit.com/wiki/bottiquette) at all times!

### Setup

- Create your Reddit script app, and get your client id and client secret:

<br>

![](https://github.com/healeycodes/Reddit-Bot-Tutorial/blob/master/setup.png)

<br>

- Set the following environment variables:

```
$env:CLIENTID='id-here'
$env:CLIENTSECRET='secret-here'
$env:CLIENTUSER='reddit-user-name'
$env:CLIENTPASS='reddit-password'
```

- Pass in comma delimited search phrases, or a single string:
  - `python bot.py --search 'phrase one, two, and three' --reply 'found you!'`

<br>

### Contributing

You're very welcome to expand the bot or raise any issues.

<hr>

License: MIT
