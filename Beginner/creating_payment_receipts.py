from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

DATA = [
    ['Date', 'Name', 'Suscription', 'Price (Rs.)'],
    ['16/11/2020', 'Full Stack Development with React & Node JS - Live',
     'Lifetime',
     '10,999/-'],
    ['17/11/2020', 'Python Programming - Live',
        'Lifetime',
        '5,999/-'],
        ['18/11/2020', 'Data Science with Python - Live',
        'Lifetime',
        '8,999/-'],
        ['19/11/2020', 'Machine Learning with Python - Live',
        'Lifetime',
        '7,999/-'],
        ['20/11/2020', 'Full Stack Development with React & Node JS - Live',
        'Lifetime',
        '10,999/-'],
        ['21/11/2020', 'Python Programming - Live',
        'Lifetime',
        '5,999/-'],
        ['22/11/2020', 'Data Science with Python - Live',
        'Lifetime',
        '8,999/-'],
        ['23/11/2020', 'Machine Learning with Python - Live',
        'Lifetime',
        '7,999/-'],
        ['24/11/2020', 'Full Stack Development with React & Node JS - Live',
        'Lifetime',
        '10,999/-'],
        ['25/11/2020', 'Python Programming - Live',
        'Lifetime',
        '5,999/-'],
        ['26/11/2020', 'Data Science with Python - Live',
        'Lifetime',
        '8,999/-'],
        ['27/11/2020', 'Machine Learning with Python - Live',
        'Lifetime',
        '7,999/-'],
        ['Subtotal', '', '', '1,00,000/-'],
        ['Discount', '', '', '20,000/-'],
        ['Total', '', '', '80,000/-']
]

pdf = SimpleDocTemplate('payment_receipt.pdf', pagesize=A4)

styles = getSampleStyleSheet()

title_style = styles['Heading1']

title_style.alignment = 1

title = Paragraph('Payment Receipt', title_style)

style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
])

table = Table(DATA, style=style)

pdf.build([title, table])
