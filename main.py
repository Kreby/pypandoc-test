#!/usr/bin/env python3

import os
from pathlib import Path
import pypandoc


input = Path('documents/doc1/doc/test.md')
output = Path('output/result.docx')

pypandoc.convert_file(
    input,
    format='markdown+rebase_relative_paths',
    to="docx",
    encoding="utf-8",
    outputfile=output,
    extra_args=[],
    filters=None)

# pandoc documents/doc1/doc/test.md --from=markdown+rebase_relative_Paths --to=docx -o test.docx 