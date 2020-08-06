#!/bin/python

import fitz
import re

def format_chapter_name(chapter, name, page):
    return chapter + " " + name


def parse_toc(toc_file, pageoffset: int):
    matching = re.compile("^(\d+(?:.\d+)*)\s(.+) (\d+)$")
    toc = []
    for (line_i, line) in enumerate(toc_file):
        line.strip()
        g = matching.match(line)
        if g is None:
            print("Formatting error on line {}:\n\"{}\"".format(line_i, line))
            print("Skipping Chapter")
            continue
        chapter = g.group(1)
        chapter_name = g.group(2)
        page_no = g.group(3)

        # print("Chapter: {} name: {} page: {}".format(
        #    chapter, chapter_name, page_no))

        intend = 1+chapter.count(".")
        name = format_chapter_name(chapter, chapter_name, page_no)
        page_no = int(page_no) + pageoffset

        toc.append([intend, name, page_no])
    return toc


def main():
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description='Adds "table of contents" to pdf files.')

    parser.add_argument("--offset", type=int, default=0,
                        help="site offset when the first chapter starts.")

    parser.add_argument("input")

    parser.add_argument("toc", type=argparse.FileType("r"))

    parser.add_argument("output")

    args = parser.parse_args()

    toc = parse_toc(args.toc, args.offset)
    # write toc
    doc = fitz.Document(args.input)
    inserted = doc.setToC(toc)
    doc.save(args.output)
    # done
    print("Done setting {} chapters".format(inserted))


if __name__ == "__main__":
    main()
