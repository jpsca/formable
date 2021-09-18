![HyperForm](header.png)

HyperForm is a library to make far easier to create beautiful, semantically rich, syntactically awesome, readily stylable and wonderfully accessible HTML forms in your Python web application.

**Documentation**: https://jpsca.github.io/hyperform/


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
