#!/usr/bin/python
document = open('document.xml', 'w')
document.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
document.write('<w:p w:rsidR="005E41F3" w:rsidRDefault="0066025C" w:rsidP="00670B26"><w:pStyle w:val="normal0"/><w:numPr><w:ilvl w:val="0"/><w:numId w:val="15"/></w:numPr><w:spacing w:before="0" w:after="60"/><w:rPr><w:color w:val="auto"/></w:rPr></w:pPr><w:r><w:rPr><w:color w:val="auto"/></w:rPr><w:t>Test View</w:t></w:r></w:p>')
document.close()