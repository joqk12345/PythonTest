# Created by joqk12345 on 4/3/17.
# www.github.com/joqk12345

#!/usr/bin/env python
# -*- conding:utf-8 -*-
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import  LAParams
from pdfminer.pdfdevice import PDFDevice
from urllib.request import urlopen

# Open a PDF file.
# fp = open('./sample/sampl1.pdf', 'rb')

fp = urlopen("https://www.tencent.com/zh-cn/articles/8003261479985013.pdf")

parser = PDFParser(fp)

doc = PDFDocument()

parser.set_document(doc)
doc.set_parser(parser)

doc.initialize("")

reource = PDFResourceManager()
laparam = LAParams()

device = PDFPageAggregator(reource,laparams=laparam)

interpreter = PDFPageInterpreter(reource,device)

for page in doc.get_pages():
    interpreter.process_page(page)
    layout = device.get_result()

    for out in  layout:
        if hasattr(out,"get_text"):
            print(out.get_text())

