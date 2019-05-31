import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

if len(sys.argv) == 1:
    print 'Usage: python pdfbooklet.py <input_file.pdf>'
    print 'Output: output_<input_file.pdf>'
    exit()


for i in xrange(1, len(sys.argv)):
    try:
        with open(r'%s' %sys.argv[i], 'rb') as readfile:
            output_pdf = PdfFileWriter()
            input_pdf = PdfFileReader(readfile)
            total_pages = input_pdf.getNumPages()
            sum_of_pages_on_paper =( (total_pages - 1) / 4) * 4 + 3
            count = 0
            for page in xrange(0, sum_of_pages_on_paper/2+1):
                output_pdf.addPage(input_pdf.getPage(page))
                if page % 2 == 0:
                    if total_pages > sum_of_pages_on_paper - page: 
                        output_pdf.insertPage(input_pdf.getPage(sum_of_pages_on_paper - page), count-1)
                    else:
                        output_pdf.insertBlankPage(None,None,count -1)
                else:
                    if total_pages > sum_of_pages_on_paper - page: 
                        output_pdf.addPage(input_pdf.getPage(sum_of_pages_on_paper - page))
                    else:
                        output_pdf.addBlankPage()
                    

            output_file = 'output_%s' %sys.argv[i]
            with open(r'%s' %output_file, "wb") as writefile:
                output_pdf.write(writefile)
            print 'Created', total_pages,  'pages %s' %output_file
    except:
        print 'File %s does not exist' %sys.argv[i]
