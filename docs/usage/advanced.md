# Advanced usage





## Disabling the plugin
You can use the `enabled` option to optionally disable this plugin. A possible use case is local development where you might want faster build times.

```yaml
plugins:
  - mkdoxy:
      enabled: !ENV [ENABLE_MKDOXY, True]
      ...
```

This will disable the plugin if the `ENABLE_MKDOXY` environment variable is not set or is set to `False`.
Inspirated by [mkdocs-simple-hooks](https://github.com/aklajnert/mkdocs-simple-hooks)

```bash
export ENABLE_MKDOXY=False
mkdocs serve
```