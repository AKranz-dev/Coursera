#Using the reportlab Python library, define the method generate_report to build the PDF reports. Create a PDF report named processed.pdf

#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    
    report_title = Paragraph(title, styles["h1"])
    report_para = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1,20)
    
    report.build([report_title, empty_line, report_para])

    
#Attachment is the name/location of the file
#Title is the title
#paragraph is the all the text for the body