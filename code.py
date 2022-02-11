from hashlib import shake_256
import json
from fpdf import FPDF

# call the json file

with open ("Info.json") as f:
    data = json.load(f)

# declare a variable in each json data
Fname = data["FName"]
Mail = data["Email"]
Pnumber = data["CNumber"]
Add = data["Address"]
Obj = data["Objective1"]
Educ1 = data["Ed1"]
Educ2 = data["Ed2"]
Exp1 = data["Extra1"]
Exp2 = data["Extra2"]
Exp3 = data["Extra3"]
Pro = data ["Exp"]
Sk1 = data["Skill1"]
Sk2 = data["Skill2"]
Sk3 = data["Skill3"]
Sk4 = data["Skill4"]
Sk5 = data["Skill5"]
Sk6 = data["Skill6"]
Aw1 = data["Award1"]
Aw2 = data["Award2"]
Aw3 = data["Award3"]
Aw4 = data["Award4"]


# create a pdf
pdf = FPDF("P", "mm", "Letter")

pdf.add_page()

# personal info
pdf.image("image.jpg", x=160, y=9, w=38, h=38, type="", link="")

pdf.set_font("Helvetica","B", size = 35)
pdf.cell(500, 10, Fname, ln = 1, align = "L")

pdf.set_font("Helvetica", size = 12)
pdf.cell(50, 10,  "Email: " + Mail, ln = 1)
pdf.cell(0, 5,  "Contact Number: " + Pnumber, ln = 1)
pdf.cell(0, 10,  "Address: " + Add, ln = 1)

pdf.line(x1 = 200, x2 = 12, y1 = 47, y2 = 47)

pdf.set_font("Helvetica","B", size = 13)
pdf.cell(100, 15,  "CAREER OBJECTIVE", ln = 1)

pdf.set_font("Helvetica", size = 11)
pdf.cell(0, 1,  Obj, ln = 1)

pdf.line(x1 = 200, x2 = 12, y1 = 65, y2 = 65)

pdf.set_font("Helvetica","B", size = 14)
pdf.cell(100, 20,  "EDUCATIONAL BACKGROUND", ln = 1)

pdf.set_font("Helvetica", size = 13)
pdf.cell(0, 1,  Educ1  + "                                                              (2013 - 2017)", ln = 1)
pdf.cell(0, 15,  Educ2  + "                                         (2017 - 2020)", ln = 1)

pdf.line(x1 = 200, x2 = 12, y1 = 98, y2 = 98)

pdf.set_font("Helvetica","B", size = 14)
pdf.cell(100, 20,  "PRE-PROFESSIONAL EXPERIENCE", ln = 1)

pdf.set_font("Helvetica", size = 13)
pdf.cell(0, 1,  Pro  + "                                                                 (2020 - 2021)", ln = 1)

pdf.line(x1 = 200, x2 = 12, y1 = 123, y2 = 123)

pdf.set_font("Helvetica","B", size = 14)
pdf.cell(100, 20,  "EXTRA CURRICULAR ACTIVITIES", ln = 1)

pdf.set_font("Helvetica", size = 13)
pdf.cell(0, 1,  Exp1  + "                                                                                     (2017 - 2020)", ln = 1)
pdf.cell(0, 15, Exp2  + "                                                                                               (2017 - 2020)", ln = 1)
pdf.cell(0, 1,  Exp3  + "                                                                                                       (2020)", ln = 1)

pdf.line(x1 = 200, x2 = 12, y1 = 160, y2 = 160)

pdf.set_font("Helvetica","B", size = 14)
pdf.cell(100, 20,  "SKILLS", ln = 1)

pdf.set_font("Helvetica", size = 13)
pdf.cell(0, 1,   Sk1 , ln = 1)
pdf.cell(0, 15,  Sk2 , ln = 1)
pdf.cell(0, 1,   Sk3 , ln = 1)
pdf.cell(0, 15,  Sk4 , ln = 1)
pdf.cell(0, 1,   Sk5 , ln = 1)
pdf.cell(0, 15,  Sk6 , ln = 1)

pdf.line(x1 = 200, x2 = 12, y1 = 220, y2 = 220)

pdf.set_font("Helvetica","B", size = 14)
pdf.cell(100, 15,  "AWARDS", ln = 1)

pdf.set_font("Helvetica", size = 13)
pdf.cell(0, 1,   Aw1 + "                                                                                            (2013 - 2019)" , ln = 1)
pdf.cell(0, 15,  Aw2 + "                                                                                                   (2020)",  ln = 1)
pdf.cell(0, 1,   Aw3 + "                                                                                                  (2013 - 2021)", ln = 1)


pdf.output("BERNALES_VIENANGELO.pdf")