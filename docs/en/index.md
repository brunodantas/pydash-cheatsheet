# pydash-cheatsheet

A simplified reference for [pydash](https://pydash.readthedocs.io/en/latest/index.html).

<div class="grid" markdown>

{% for function in functions %}

### {{ function[0] }}

{{ function[1] }}

=== "Example"

    ```py
    >>> {{function[2] }}
    {{function[3]}}
    ```

=== "Docstring"

    ```{{ function[4] }}```

{% endfor %}

</div>
