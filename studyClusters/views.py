from django.shortcuts import render
import os
import subprocess
from .forms import PDFNameForm

def showAllPDFs(request):
    pdfList = subprocess.check_output(["ls","/home/nahian/StudyClusters/studyClusters/static/studyClusters/pdfs/"]).decode("utf-8").split()
    context = {"list" : pdfList}
    if request.method == 'POST':
        print(request.POST["pdf"])
        pdfName = request.POST["pdf"]
        print(pdfName)
        return render(request,'studyClusters/display_pdf.html',{"pdfName" : pdfName})
    else:
        return render(request,'studyClusters/show_all_pdfs.html',context)
