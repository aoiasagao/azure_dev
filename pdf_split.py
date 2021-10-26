from io import FileIO
from pdf2image import convert_from_path
from pathlib import Path
import PyPDF2,pathlib,os
 

# パスをセット。
DIR_IN = ""
DIR_OUT = ""

# pdfファイルのリスト
pdffiles = list(pathlib.Path(DIR_IN).glob('*.pdf'))
 
# 本体処理
for pdffile in pdffiles:
 
    # 拡張子pdfなしのファイル名取得
    filename = pdffile.name
    # pdfファイルを読み込み
    pdffile_reader = PyPDF2.PdfFileReader(FileIO(pdffile,"rb"))
    
    # PDFファイルを分割
    for page in range(pdffile_reader.numPages):
        pdf_new = PyPDF2.PdfFileWriter()
        pdf_new.addPage(pdffile_reader.getPage(page))
 
        pageNo = format(page+1, '0>2')
        filename_new = os.path.join(DIR_OUT, f'{filename}_{pageNo}.pdf')
        
        with open(filename_new, 'wb') as f:
            pdf_new.write(f)

            