TEMPLATE = """
# Modules

Here is a list of all modules:

{% for node in nodes recursive %}
{%- if node.is_group %}
* [**{{node.title}}**]({{node.url}}) {{node.brief}}
{%- if node.has_children %}
  {{- loop(node.children)|indent(2, true) }}
{%- endif %}
{%- endif -%}
{%- endfor %}
"""
