# pip install beautifulsoup4==4.13.4 markdown_pdf==1.7
from bs4 import BeautifulSoup
from bs4.element import Tag
import re
from markdown_pdf import MarkdownPdf, Section

note_data = open("notes.txt", "r", encoding="utf-8").read()
soup = BeautifulSoup(note_data, "html.parser")

def drill_into_tag(tag, ):
    texts = ""
    if isinstance(tag, Tag):
        if tag.name == "span":
            text = tag.text
            if "bold" in tag['class']:
                text = f" **{text}** "
            if "code" in tag['class']:
                text = f" `{text}` "
            return text
        elif tag.name == "div":
            if "heading3" in tag['class']:
                texts += "## "
            elif "paragraph" in tag['class']:
                texts += "\n"
            elif "bullet" in tag['class']:
                text = '- '
                return text 
        for child in tag.children:
            texts += drill_into_tag(child)
    return texts

texts = []
notes = []
parent = soup.find("labs-tailwind-doc-viewer")
for child in parent.children:
    if isinstance(child, Tag):
        for inner_child in child.children:
            if isinstance(inner_child, Tag):
                text = drill_into_tag(inner_child)
                text = text.strip()
                if text == "--------------------------------------------------------------------------------":
                    title = texts[0].strip()
                    title = title.strip("#")
                    notes.append({"title": title, "note":"\n".join(texts)})
                    texts = []
                else:
                    texts.append(text)
                    texts.append("\n")

notes.reverse()
import re

for i, item in enumerate(notes):
    pdf = MarkdownPdf(toc_level=1, optimize=True)
    clean_text = re.sub(r'-(\n+)', '- ', item["note"]) 
    clean_text = re.sub(r'\[\s*\d+(?:\s*[-,]\s*\d+)*\s*\]', '', clean_text)

    pdf.add_section(Section(clean_text))
    title = item["title"].strip().replace(" ", "_").replace(":", "_").replace("/", "_")
    pdf.save(f"{i}. {title}.pdf")