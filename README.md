# plugin_stanza-bio
A [Stanza][stanza] plugin with [biomedical models][stanza-bio] for [DeepNLPF][deepnlpf].

## Installation
To install the stanza-bio plugin and its dependencies, do:

```zsh
deepnlpf --install_user_plugin 'https://github.com/daniloBlera/plugin_stanza-bio/archive/master.zip'
```

After installing the plugin's dependencies, download the biomedical models from python with:

```python
import stanza
stanza.download('en', package='craft')
```

The other available biomedical and clinical models can be found here:

[https://stanfordnlp.github.io/stanza/available_biomed_models.html][available-models]

[stanza]: https://stanfordnlp.github.io/stanza/
[stanza-bio]: https://stanfordnlp.github.io/stanza/biomed.html
[deepnlpf]: https://github.com/deepnlpf/deepnlpf
[available-models]: https://stanfordnlp.github.io/stanza/available_biomed_models.html
