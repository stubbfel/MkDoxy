TEMPLATE = """
<div style="border: 4px dotted red">
<h3 class="doxy-error">Error: {{title }}</h3>
{%- if message %}
```{{language}}
{{message}}
```
{%- endif %}
</div>
"""