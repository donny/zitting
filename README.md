# zitting

Zitting is a small AWS Lambda using [Gordon](https://github.com/jorgebastida/gordon) that displays top 10 stories from [Hacker News](https://news.ycombinator.com).

### Background

This project is part of [52projects](https://donny.github.io/52projects/) and the new stuff that I learn through this project: [Gordon](https://github.com/jorgebastida/gordon) and [Haxor](https://github.com/avinassh/haxor).

### Project

Zitting is a small AWS Lambda using [Gordon](https://github.com/jorgebastida/gordon) that displays top 10 stories from [Hacker News](https://news.ycombinator.com). We use [Haxor](https://github.com/avinassh/haxor) that provides the Python API to Hacker News. Zitting is accessible from HTTP via API Gateway. The screenshot of the app can be seen below:

![Screenshot](https://raw.githubusercontent.com/donny/zitting/master/screenshot.png)

### Implementation

We create a Gordon project by using the command: `gordon startproject zitting`. Followed by the command: `gordon startapp app` to create a new app. We build and deploy the project by running the following command: `gordon build && gordon apply`.

### Conclusion

...
