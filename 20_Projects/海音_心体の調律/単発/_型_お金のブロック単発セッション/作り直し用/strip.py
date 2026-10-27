import sys
from pptx import Presentation
p=Presentation(sys.argv[1]); n=h=0
for s in p.slides:
    for sh in list(s.placeholders):
        if not sh.has_text_frame or not sh.text_frame.text.strip():
            sh._element.getparent().remove(sh._element); n+=1
    if any(sh.has_text_frame and sh.text_frame.text.startswith('【由香さん用】') for sh in s.shapes):
        h+=1
p.save(sys.argv[1]); print('removed',n,'hidden',h)
