from pathlib import Path
from weasyprint import HTML
import fitz
from PIL import Image, ImageDraw

OUT = Path('/tmp/pdf-book-factory-smoke')
OUT.mkdir(parents=True, exist_ok=True)

HTML_TEXT = '''<!doctype html>
<html lang="ar" dir="rtl">
<head><meta charset="utf-8">
<style>
@page {
  size: A4;
  margin: 16mm;
  background: #fffdf7;
  @bottom-center { content: counter(page); color: #6f5f43; font-size: 9pt; }
}
body {
  direction: rtl;
  font-family: "Noto Naskh Arabic", "Noto Sans Arabic", serif;
  color: #102a38;
  font-size: 11pt;
  line-height: 1.7;
}
h1 { font-family: "Noto Sans Arabic"; color: #0b3140; font-size: 24pt; margin: 0 0 8mm; }
h2 { color: #8a5a18; font-size: 15pt; margin: 8mm 0 3mm; }
.card { border: 1px solid #e0d2b0; background: #fff8e8; border-radius: 8px; padding: 10px 14px; margin: 6mm 0; }
table { width: 100%; border-collapse: collapse; margin-top: 6mm; }
th { background: #0a3040; color: white; padding: 8px; }
td { border: 1px solid #ddd3bd; padding: 8px; vertical-align: top; }
</style></head>
<body>
<h1>اختبار خط إنتاج كتاب احترافي</h1>
<p>في بيئة التصنيع، لا تظهر تكلفة المنتج فجأة داخل التقرير، بل تمر بسلسلة من الحركات تبدأ من الخامة وتنتهي بتقرير الإدارة.</p>
<div class="card"><strong>ملاحظة عملية:</strong> الصفحة الاحترافية لا تكون مزدحمة ولا فارغة؛ كل عنصر يجب أن يخدم فهم القارئ.</div>
<h2>جدول حركة القيمة</h2>
<table>
<tr><th>الحركة</th><th>الأثر المالي</th><th>سؤال المدير</th></tr>
<tr><td>شراء خامات</td><td>زيادة مخزون الخامات</td><td>هل الشراء مرتبط بخطة إنتاج؟</td></tr>
<tr><td>صرف للإنتاج</td><td>انتقال القيمة إلى الإنتاج تحت التشغيل</td><td>هل الصرف مطابق للمعيار؟</td></tr>
<tr><td>إتمام المنتج</td><td>تحويل التكلفة إلى مخزون منتج تام</td><td>هل الكمية المقبولة طبيعية؟</td></tr>
</table>
</body></html>'''

html_path = OUT / 'smoke.html'
pdf_path = OUT / 'smoke.pdf'
html_path.write_text(HTML_TEXT, encoding='utf-8')
HTML(filename=str(html_path)).write_pdf(str(pdf_path))

doc = fitz.open(str(pdf_path))
page_paths = []
for i, page in enumerate(doc, start=1):
    pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
    img_path = OUT / f'page-{i:03d}.png'
    pix.save(str(img_path))
    page_paths.append(img_path)

thumbs = []
for img_path in page_paths:
    img = Image.open(img_path).convert('RGB')
    img.thumbnail((260, 370))
    thumbs.append(img.copy())

sheet = Image.new('RGB', (max(1, len(thumbs)) * 300, 420), 'white')
draw = ImageDraw.Draw(sheet)
for idx, img in enumerate(thumbs, start=1):
    x = (idx - 1) * 300 + 20
    sheet.paste(img, (x, 20))
    draw.text((x, 395), f'page {idx}', fill=(0, 0, 0))

sheet_path = OUT / 'contact-sheet.png'
sheet.save(sheet_path)
print({'pdf': str(pdf_path), 'pages': doc.page_count, 'contact_sheet': str(sheet_path), 'size': pdf_path.stat().st_size})
