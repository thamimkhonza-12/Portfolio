from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "portfolio" / "resume" / "Thamsanqa_Dlamini_CV.pdf"


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#64748b"))
    canvas.drawRightString(200 * mm, 10 * mm, f"Page {doc.page}")
    canvas.restoreState()


def p(text, style):
    return Paragraph(text, style)


def section(title, styles):
    return [
        Spacer(1, 8),
        p(title.upper(), styles["CVSection"]),
        Spacer(1, 4),
    ]


def bullets(items, styles):
    flow = []
    for item in items:
        flow.append(p(f"- {item}", styles["CVBullet"]))
    return flow


def build():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CVName",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=25,
            textColor=colors.HexColor("#0f172a"),
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVTitle",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            textColor=colors.HexColor("#0f766e"),
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVContact",
            parent=styles["Normal"],
            fontSize=8.6,
            leading=11,
            textColor=colors.HexColor("#334155"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVBody",
            parent=styles["Normal"],
            fontSize=9.3,
            leading=12.7,
            textColor=colors.HexColor("#1f2937"),
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVSection",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=12,
            textColor=colors.HexColor("#0f172a"),
            borderColor=colors.HexColor("#14b8a6"),
            borderWidth=0,
            borderPadding=0,
            spaceBefore=4,
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVRole",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.6,
            leading=12,
            textColor=colors.HexColor("#0f172a"),
            spaceBefore=4,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVMeta",
            parent=styles["Normal"],
            fontSize=8.6,
            leading=10.5,
            textColor=colors.HexColor("#64748b"),
            spaceAfter=3,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CVBullet",
            parent=styles["CVBody"],
            leftIndent=8,
            firstLineIndent=-8,
            spaceAfter=2,
        )
    )

    doc = BaseDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=11 * mm,
        bottomMargin=11 * mm,
        title="Thamsanqa Dlamini - Full-Stack Developer CV",
        author="Thamsanqa Dlamini",
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=add_page_number)])

    story = []
    story.append(p("THAMSANQA PROFESSOR DLAMINI", styles["CVName"]))
    story.append(p("Junior Full-Stack Developer | Python | Django | REST APIs | JavaScript", styles["CVTitle"]))
    story.append(
        p(
            "KwaNdengezi, South Africa | 061 452 5714 / 079 067 8829 | "
            "thamidlamini544@gmail.com<br/>"
            "GitHub: github.com/thamimkhonza-12 | LinkedIn: linkedin.com/in/thami-dlamini | "
            "Portfolio: thamimkhonza-12.github.io/Portfolio/",
            styles["CVContact"],
        )
    )

    story += section("Professional Summary", styles)
    story.append(
        p(
            "Junior Full-Stack Developer with hands-on experience building RESTful APIs, database-backed "
            "applications, and responsive web interfaces using Python, Django, Django REST Framework, "
            "JavaScript, HTML, CSS, and PostgreSQL. Recently completed ALX backend development training, "
            "with a strong foundation in API design, authentication, deployment, and clean application "
            "structure. Currently contributing as a contract-based developer for BuildForge/KasiDash. "
            "Combines technical growth with more than 10 years of professional experience "
            "showing discipline, reliability, customer focus, and problem-solving. Actively seeking a "
            "junior full-stack developer role.",
            styles["CVBody"],
        )
    )

    story += section("Technical Skills", styles)
    skill_data = [
        [p("Languages", styles["CVRole"]), p("Python, JavaScript, HTML5, CSS3", styles["CVBody"])],
        [
            p("Frameworks", styles["CVRole"]),
            p("Django, Django REST Framework, Node.js, Tailwind CSS", styles["CVBody"]),
        ],
        [p("Databases", styles["CVRole"]), p("PostgreSQL, MySQL, SQLite", styles["CVBody"])],
        [
            p("Tools & Platforms", styles["CVRole"]),
            p("VS Code, PyCharm, Git, GitHub, Postman, Render, Linux", styles["CVBody"]),
        ],
        [
            p("Core Concepts", styles["CVRole"]),
            p(
                "RESTful API development, CRUD operations, JWT authentication, MVC architecture, "
                "responsive UI, debugging, deployment, version control",
                styles["CVBody"],
            ),
        ],
    ]
    table = Table(skill_data, colWidths=[35 * mm, 130 * mm], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 8.6),
                ("LEADING", (0, 0), (-1, -1), 11),
                ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#0f172a")),
                ("TEXTCOLOR", (1, 0), (1, -1), colors.HexColor("#334155")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    story.append(table)

    story += section("Projects", styles)
    projects = [
        (
            "Task Management API",
            "Django, Django REST Framework, PostgreSQL, JWT",
            [
                "Built a RESTful API for secure user registration, login, task creation, updates, deletion, and retrieval.",
                "Implemented JWT-based authentication, user authorization, filtering, search, and user-specific data access.",
                "Tested API endpoints with Postman and followed RESTful principles and clean architecture practices.",
                "GitHub: github.com/thamimkhonza-12/Alx_BE_Capstone",
            ],
        ),
        (
            "Community Resource Finder",
            "Django, REST API, PostgreSQL, responsive web application concepts",
            [
                "Designed an application to help users locate nearby community services such as clinics, shelters, and food banks.",
                "Built database models, CRUD endpoints, filtering capabilities, and geolocation-based search logic.",
                "Focused on efficient data retrieval, practical user workflows, and deployment using Render.",
                "GitHub: github.com/thamimkhonza-12/Comunity_resource_finder",
            ],
        ),
        (
            "Frontend and JavaScript Projects",
            "JavaScript, HTML5, CSS3",
            [
                "Created practical browser-based projects including a Kanban Board, Form Validation Library, Dark Mode Toggle, Image Carousel, and CSV Data Parser.",
                "Applied DOM manipulation, state handling, validation logic, responsive layout, and reusable JavaScript patterns.",
                "GitHub: github.com/thamimkhonza-12",
            ],
        ),
    ]
    for name, meta, items in projects:
        story.append(p(name, styles["CVRole"]))
        story.append(p(meta, styles["CVMeta"]))
        story += bullets(items, styles)

    story += section("Education", styles)
    education = [
        ("ALX Africa (Remote)", "Back-End Web Development - Completed March 2026"),
        ("PC Training & Business College", "Certificate in Information Technology - 2007"),
        ("Rosebank College", "Diploma in Information Technology - 2008 to 2010"),
        ("Kwa Santi Secondary School", "Grade 12 - 2006"),
    ]
    for school, detail in education:
        story.append(p(school, styles["CVRole"]))
        story.append(p(detail, styles["CVMeta"]))

    story += section("Professional Experience", styles)
    experience = [
        (
            "Developer, Contract Based - BuildForge/KasiDash",
            "Contract Based",
            [
                "Contribute to development tasks across practical full-stack product work.",
                "Apply Python, JavaScript, GitHub, and implementation-focused problem-solving to support delivery.",
                "Work with project requirements, technical improvements, and collaborative development workflows.",
                "Reference: facebook.com/share/1EbNHvDFwp/",
            ],
        ),
        (
            "Customer Service - Kempston Truck Hire",
            "Jan 2023 - Present",
            [
                "Managed time-sensitive delivery operations with high accuracy.",
                "Maintained operational efficiency and reliability in a fast-paced environment.",
                "Strengthened problem-solving, communication, and attention to detail.",
            ],
        ),
        (
            "Driver - Kempston Employment Solutions",
            "Feb 2021 - Jan 2023",
            [
                "Maintained accurate delivery records and followed strict operational procedures.",
                "Demonstrated discipline, accountability, consistency, and route planning.",
            ],
        ),
        (
            "Sales & Stock Assistant - Incheon Korea Motor Spares",
            "Jan 2011 - Apr 2020",
            [
                "Managed inventory, supported daily sales operations, and maintained accurate stock records.",
                "Provided customer service, coordinated logistics, and worked with data-focused stock control processes.",
            ],
        ),
    ]
    for role, dates, items in experience:
        story.append(p(role, styles["CVRole"]))
        story.append(p(dates, styles["CVMeta"]))
        story += bullets(items, styles)

    story += section("Additional Information", styles)
    story += bullets(
        [
            "Open to junior full-stack developer roles.",
            "Actively expanding skills in Node.js, frontend development, and C# (.NET).",
            "Strong work ethic, fast learner, adaptable, and passionate about building useful applications.",
        ],
        styles,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story)


if __name__ == "__main__":
    build()
