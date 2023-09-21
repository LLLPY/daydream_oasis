aa = '''{ "blog/front": {
      "text": "blog/front",
      "collapsible": true,
      "collapsed": false,
      "items": [
        {
          "text": "api-examples.md",
          "link": "blog/front/api-examples.md"
        },
        {
          "text": "markdown-examples.md",
          "link": "blog/front/markdown-examples.md"
        },
        {
          "text": "初识机器学习.md",
          "link": "blog/front/初识机器学习.md"
        },
        {
          "text": "b.md",
          "link": "blog/front/b.md"
        },
        {
          "text": "team_members.md",
          "link": "blog/front/team_members.md"
        },
        {
          "text": "a.md",
          "link": "blog/front/a.md"
        },
        {
          "text": "index.md",
          "link": "blog/front/index.md"
        }
      ],
      "blog/front/section_a": {
        "text": "blog/front/section_a",
        "collapsible": true,
        "collapsed": false,
        "items": [
          {
            "text": "demo.md",
            "link": "blog/front/section_a/demo.md"
          }
        ]
      }
    },
    "blog/backend": {
      "text": "blog/backend",
      "collapsible": true,
      "collapsed": false,
      "items": [
        {
          "text": "demo.md",
          "link": "blog/backend/demo.md"
        },
        {
          "text": "a.md",
          "link": "blog/backend/a.md"
        },
        {
          "text": "index.md",
          "link": "blog/backend/index.md"
        }
      ]
    }
  }'''

import json
print(json.loads(aa))