p = document.add_paragraph('')
p.add_run('').bold = True
p.add_run('')
#document.add_heading('Heading, level 1', level=1)
#document.add_paragraph('Intense quote', style='IntenseQuote')


#document.add_paragraph(
    #'first item in unordered list', style='ListBullet'
#)
document.add_paragraph(
    'first item in ordered list', style='ListNumber'
)
document.add_paragraph(
    'first item in ordered list', style='ListNumber'
)
document.add_picture('C:/Users/Daniel/Pictures/mantis.png', width=Inches(1.25))

table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Qty'
hdr_cells[1].text = 'Id'
hdr_cells[2].text = 'Desc'
row_cells = table.add_row().cells
row_cells[0].text = 'fifty'
row_cells[1].text = '4523525'
row_cells[2].text = 'Best in the West'