# Adds "Table of Content" to pdf files

Pdf files a great for reading and there are a lot of tools out there, which creates those files.
Unluckily, some pdf files have no Table of Content, which makes it hard to navigate in those. Bookmarks help, but they can be tedious.

This Python script adds user defined "Table of Content"(ToC) to a specific pdf file.
The ToC has to be defined in a [simple text file](#define-toc-file).

## Basic Usage

Install the dependencies ([PyMuPDF](https://pypi.org/project/PyMuPDF/)).
A [Poetry](https://python-poetry.org/) project file is provided.

Define your ToC ([see below](#define-toc-file)) and call the script, either by using poetry

```bash
poetry run pdf_toc input_file.pdf my_:_toc.toc output_file.pdf
```

or by executing the script:

```bash
python pdf_toc/pdf_toc.py input_file.pdf my_toc.toc output_file.pdf
```

You can also define a page offset i.e. if your first chapter starts at "Page 1" but
the actual page of "Page 1" in the pdf is i.e. page 11.

```bash
python pdf_toc/pdf_toc.py --offset 10 ...
```

## Define ToC file

For each chapter, write a line with:

```text
chapter-number name page
```

Example toc file:

```text
1 Introduction 1
1.1 History 2
1.2 Motivation 3
2 Content 4
2.1 Figures 6
3 Conclusion 8
```

The program will recognize the intend of the chapters and group them together.
The resulting ToC in the pdf would be:

```text
+ -- 1 Introduction
|    + -- 1.1 History
|    + -- 1.2 Motivation
| -- 2 Content
|    + -- 2.1 Figures
| -- 3 Conclusion
```

## License

[MIT License](./LICENSE) © Matthias Möller. Made with ♥ in Germany.
