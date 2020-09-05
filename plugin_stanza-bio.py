#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implementation of the Stanza-Bio plugin for DeepNLPF

This file is a modified version from the stanza plugin.
"""
import json
import stanza

from deepnlpf.core.iplugin import IPlugin


class Plugin(IPlugin):
    def __init__(self, document, pipeline):
        self._document = document
        self._processors = pipeline["tools"]["stanza-bio"]["processors"]
        self._lang = pipeline["lang"]
        self._package = pipeline['tools']['stanza-bio']['package']

    def run(self):
        doc = self.wrapper()
        doc_annotation = self.out_format(doc)
        return doc_annotation

    def wrapper(self) -> list:
        nlp = stanza.Pipeline(
            lang=self._lang,
            processors=", ".join(self._processors),
            use_gpu=False,
            package=self._package
        )

        object_stanza = nlp(" ".join(self._document))
        return json.loads(str(object_stanza))  # convert object stanza to object json.

    def out_format(self, doc: list) -> list:
        doc_formated = list()

        for index, sentence in enumerate(doc):
            text = list()
            token_annotation = list()

            for token in sentence:
                text.append(token["text"])
                token_annotation.append(token)

            data = {}
            data["_id"] = index + 1
            data["text"] = " ".join(text)
            data["annotation"] = token_annotation
            doc_formated.append(data)

        return doc_formated
