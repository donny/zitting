# zitting

Zitting is a small AWS Lambda using [Gordon](https://github.com/jorgebastida/gordon) that displays top 10 stories from [Hacker News](https://news.ycombinator.com).

### Background

This project is part of [52projects](https://donny.github.io/52projects/) and the new stuff that I learn through this project: [Gordon](https://github.com/jorgebastida/gordon) and [Haxor](https://github.com/avinassh/haxor).

### Project

Zitting is a small AWS Lambda using [Gordon](https://github.com/jorgebastida/gordon) that displays top 10 stories from [Hacker News](https://news.ycombinator.com). We use [Haxor](https://github.com/avinassh/haxor) that provides the Python API to Hacker News. Zitting is accessible from HTTP via API Gateway. The screenshot of the app can be seen below:

![Screenshot](https://raw.githubusercontent.com/donny/zitting/master/screenshot.png)

### Implementation

We create a Gordon project by using the command: `gordon startproject zitting`. Followed by the command: `gordon startapp app` to create a new app. We build and deploy the project by running the following command: `gordon build && gordon apply`.

We then specify the API Gateway integration as can be seen in the following `settings.yml`:

```yml
---
project: zitting
default-region: us-east-1
code-bucket: gordon-fiftytwo-zitting
apps:
  - gordon.contrib.lambdas
  - app

apigateway:
    zittingapi:
        description: Zitting API
        resources:
            /:
                methods: GET
                integration:
                    lambda: app.zitting
```

The main Python code itself is very small and straight forward:

```python
import json
from hackernews import HackerNews

def handler(event, context):
    hn = HackerNews()
    results = []
    for story_id in hn.top_stories(limit=10):
        results.append(hn.get_item(story_id).title)

    return json.dumps(results)
```

### Conclusion

[Gordon](https://github.com/jorgebastida/gordon) is kind of similar to [Serverless](https://serverless.com) that I learnt from [Quail](https://github.com/donny/quail) a few weeks ago. They are basically a framework to simplify AWS Lambda development and deployment. As we can see from the list of [features](https://github.com/jorgebastida/gordon), Gordon aims to be more transparent (i.e. _less magic_) through simple YAML configuration and the generated CloudFormation templates. This is really great and we can actually deploy using the CloudFormation templates directly.

There is a [bug](https://github.com/jorgebastida/gordon/issues/8) in Gordon related to the query parameters and API Gateway. Nevertheless, Gordon is a great tool and I can see using it in the future.
