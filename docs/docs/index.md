---
template: home.html
---
<blockquote style="max-width:480px; margin:0 auto;">
    <p>The main problem I used to have with it was the markup.
    <br>I wanted Bootstrap <em>classes</em>.
    <br>I wanted <em>complex layouts</em> like multiple columns.</p>
    <footer>— <cite>Random Redditor</cite></footer>
</blockquote>

## How HyperForm is different

- A field isn't tied to a specific HTML tag, so can be presentend in multiple ways. Even the same form can be used in different contexts and have different widgets and styles on each.

- Incredible easy to integrate with any ORM (object-relational mapper). Built-in adaptators for SQLAlchemy and Pony.

- Many commonly used built-in validators, and you can also write simple functions to use as custom ones.

- Any field can accept multiple values; as a list or as a comma-separated text.

- All error messages are editable. We are not robots, the tone of the messages must be able to change or to be translated.


## Just show me how it looks

```python
from hyperform  import Form, Email, Text


class CommentForm(Form):
    email = Email(required=True, check_dns=True)
    message = Text(
    	LongerThan(5, "Please write a longer message"),
    	required=True
    )


def comment():
    form = CommentForm(request.POST)
    if request.method == "POST" and form.validate():
    	data = form.save()
        ...
    return render_template("comment.html", form=form)

```

## Installation

Install the package using `pip`.

```bash
pip install hyperform
```

## Resources

- [Source code (MIT Licensed)](https://github.com/jpsca/hyperform)
- [PyPI](https://pypi.org/project/hyperform/)
- [Change log](https://github.com/jpsca/hyperform/releases)
