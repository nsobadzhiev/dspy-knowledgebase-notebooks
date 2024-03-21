from semantic_text_splitter import TextSplitter


def file_chunks(file_name: str, max_chars: int = 2000) -> list[str]:
    with open(file_name, 'r') as text_file:
        contents = text_file.read()
        splitter = TextSplitter()
        chunks = splitter.chunks(contents, max_chars)
        return chunks
    