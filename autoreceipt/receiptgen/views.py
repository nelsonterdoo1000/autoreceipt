from django.shortcuts import render

from .models import ClientDetail
from .forms import ClientDetailForm


#imports for report ReportLab
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors



def generate_pdf(client):
    # Create a response object for the PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt_{client.fname}_{client.lname}.pdf"'
    
    # Create a PDF canvas
    pdf_canvas = canvas.Canvas(response, pagesize=A4)

    # Add business logo and name at the top right
    logo_path = "C:/Users/New User/Documents/Golden Touch Technologies/GT_HUB Logo.png"  # Ensure the correct path to your logo file
    pdf_canvas.drawImage(logo_path, 5.5 * inch, 10.5 * inch, width=2 * inch, height=1 * inch)

    # Add business name and address
    pdf_canvas.setFont("Helvetica-Bold", 14)
    pdf_canvas.drawString(5.5 * inch, 10 * inch, "Golden Touch Technologies")

    pdf_canvas.setFont("Helvetica", 10)
    pdf_canvas.drawString(5.5 * inch, 9.7 * inch, "No.19 Niger Drive,")
    pdf_canvas.drawString(5.5 * inch, 9.5 * inch, "Onitsha, Anambra State.")
    pdf_canvas.drawString(5.5 * inch, 9.3 * inch, "Phone: 08146058017")
    pdf_canvas.drawString(5.5 * inch, 9.1 * inch, "Email: nelson@nelsonterdoo.online")

    # Add title centered below the header
    pdf_canvas.setFont("Helvetica-Bold", 16)
    pdf_canvas.drawCentredString(4.14 * inch, 8.5 * inch, "Client Receipt")

    # Set the font and color for normal text
    pdf_canvas.setFont("Helvetica", 12)
    pdf_canvas.setFillColor(colors.black)

    # Add client details in a stylized way
    pdf_canvas.drawString(1 * inch, 7.8 * inch, f"FIRST NAME: {client.fname}")
    pdf_canvas.drawString(1 * inch, 7.5 * inch, f"LAST NAME: {client.lname}")
    pdf_canvas.drawString(1 * inch, 7.2 * inch, f"EMAIL: {client.email}")
    pdf_canvas.drawString(1 * inch, 6.9 * inch, f"SERIAL NUMBER: {client.serialnumber}")
    pdf_canvas.drawString(1 * inch, 6.6 * inch, f"ADDRESS: {client.address}")
    pdf_canvas.drawString(1 * inch, 6.3 * inch, f"PC MODEL: {client.pcmodel}")
    pdf_canvas.drawString(1 * inch, 6.0 * inch, f"PROCESSOR: {client.processor}")

    # Stylize RAM and ROM in bold and uppercase
    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(1 * inch, 5.7 * inch, f"RAM: {client.ram}")
    pdf_canvas.drawString(1 * inch, 5.4 * inch, f"ROM: {client.rom}")

    # Go back to normal font for the remaining details
    pdf_canvas.setFont("Helvetica", 12)
    pdf_canvas.drawString(1 * inch, 5.1 * inch, f"AMOUNT: {client.amount}")
    pdf_canvas.drawString(1 * inch, 4.8 * inch, f"DATE: {client.date}")

    # Optionally, add a footer or thank you note
    pdf_canvas.setFont("Helvetica-Oblique", 10)
    pdf_canvas.setFillColor(colors.gray)
    pdf_canvas.drawCentredString(4.14 * inch, 1 * inch, "Thank you for your partronage!")

    # Finish the PDF document
    pdf_canvas.showPage()
    pdf_canvas.save()

    return response


# def home(request):
#     if request.method == "POST":
#         form = ClientDetailForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             return render(request,'home.html',{})
#     else:
#         return render(request,'home.html',{})

def home(request):
    if request.method == "POST":
        form = ClientDetailForm(request.POST)
        if form.is_valid():
            client = form.save()
            # Generate PDF and return as response
            return generate_pdf(client)
    else:
        form = ClientDetailForm()
    
    return render(request, 'home.html', {'form': form})