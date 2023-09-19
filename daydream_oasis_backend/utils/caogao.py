aa = '''{ "blog/sider_a": {
      "text": "blog/sider_a",
      "collapsible": true,
      "collapsed": false,
      "items": [
        {
          "text": "api-examples.md",
          "link": "blog/sider_a/api-examples.md"
        },
        {
          "text": "markdown-examples.md",
          "link": "blog/sider_a/markdown-examples.md"
        },
        {
          "text": "初识机器学习.md",
          "link": "blog/sider_a/初识机器学习.md"
        },
        {
          "text": "b.md",
          "link": "blog/sider_a/b.md"
        },
        {
          "text": "team_members.md",
          "link": "blog/sider_a/team_members.md"
        },
        {
          "text": "a.md",
          "link": "blog/sider_a/a.md"
        },
        {
          "text": "index.md",
          "link": "blog/sider_a/index.md"
        }
      ],
      "blog/sider_a/section_a": {
        "text": "blog/sider_a/section_a",
        "collapsible": true,
        "collapsed": false,
        "items": [
          {
            "text": "demo.md",
            "link": "blog/sider_a/section_a/demo.md"
          }
        ]
      }
    },
    "blog/sider_b": {
      "text": "blog/sider_b",
      "collapsible": true,
      "collapsed": false,
      "items": [
        {
          "text": "demo.md",
          "link": "blog/sider_b/demo.md"
        },
        {
          "text": "a.md",
          "link": "blog/sider_b/a.md"
        },
        {
          "text": "index.md",
          "link": "blog/sider_b/index.md"
        }
      ]
    }
  }'''

import json
print(json.loads(aa))