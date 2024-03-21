# DSPy knowledgebase notebooks

This is a collection of utilities and notebooks for experimenting with DSPy and knowledgebases. It can be run in order to get chat completions based on external knowledge.

## Current setup

DSPy is very flexible and supports a number of LMs and knowledgebase storage models. Here, focus has been put on simplicity and the ability to get up and running quickly and "locally". Therefore, the following tools have been chosen:
* Ollama with Mistral as a model
* ChromaDB as a vector database, featuring a persistant file storage

## Adding knowledebase

Two options are provided here, as notebooks, for adding new knowedge to the ChromaDB and therefore, to the LLM agent.

### PDFs

`extract_pdf.py` extracts text from a PDF and the `create_knowledgebase` notebook ca nbe used to get these pages and feed them into a ChromaDB collection. Text is split into pages and focus has been given to textual data. If your PDF contains a lot of diagrams, tables or images, it might not result into a useful knowledgebase.

### Text files / man pages

The `create_knowledgebase` notebook can also open text files (via `extract_text.py`), split them into semantically relevant pieces and build a vector database from.

For demonstration purposes, I've added the man page contents of `curl` in `man_curl.txt`. It can be used to answer curl-related questions in the `llm_agent` notebook.

## Running an LLM agent

The `llm_agent` notebook uses DSPy in order to create a couple of LLM agents for answering questions while using knowledgebase, previously created with `create_knowledgebase`.

### Prerequisites

All dependencies needed for these notebooks is in `requirements.txt` and the notebooks begin with a step that installs them. However, prior to running the LLM agent, you need to make sure Ollama is installed AND running. Additionally, the Mistral model needs to be installed.

#### Running Ollama

```bash
ollama serve
```

#### Installing the Mistral model

```bash
ollama pull mistral
```
