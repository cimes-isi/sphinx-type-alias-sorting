# Sphinx groupwise sorting of primitive type aliases

In Sphinx v4.3.1 and Python 3.8.2, type aliases are not all sorted correctly when using `autodoc_member_order = 'groupwise'`.

To produce, install Sphinx into your Python environment (e.g., `pip install sphinx`), then:

```sh
cd docs
make html
```

Then view the generated html for the module at: `docs/build/html/testmod.html`.
Type aliases for primitive classes and Unions are not sorted together.
