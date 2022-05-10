
from reportlab.lib.pagesizes import letter, A4
PAGE_WIDTH, PAGE_HEIGHT = A4

# print(A4)


from reportlab.lib.units import inch, mm
# PAGE_WIDTH, PAGE_HEIGHT = 140*mm, 215*mm
page_size = (PAGE_WIDTH, PAGE_HEIGHT)
TOP_MARGIN, BOTTOM_MARGIN = 0.5*inch, 0.5*inch
LEFT_MARGIN, RIGHT_MARGIN = 0.5*inch, 0.5*inch

export_name_url = 'resume.pdf'
# page_info = "======================== RESUME =============================="

# Title = "Santo K Thomas - Resume 2021"

PAGE_FRAME_WIDTH = PAGE_WIDTH - (LEFT_MARGIN + RIGHT_MARGIN)
# print(PAGE_FRAME_WIDTH)
PAGE_FRAME_HEIGHT = PAGE_HEIGHT - (TOP_MARGIN + BOTTOM_MARGIN)
