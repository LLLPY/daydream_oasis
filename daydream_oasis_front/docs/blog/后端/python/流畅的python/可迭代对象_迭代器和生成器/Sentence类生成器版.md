---

next: false

---



<BlogInfo id="828"/>

```python
import re
import reprlib


class Sentence:
    RE_WORD = re.compile('\w+')

    def __init__(self, text):
        self.text = text
        self.words = self.RE_WORD.findall(self.text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    # reprlib.repr用于生成大型数据结构的简略字符串表示形式
    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        pass
```



<ActionBox />
