{
    "name": "CDN Mobile API Addon",
    "version": "1.0.0",
    "summary": "Backend API untuk aplikasi mobile IBS Al Hamra",
    "description": "Menyediakan endpoint autentikasi & CRUD perijinan, pelanggaran, absesnsi, nilai, dll.",
    "author": "Magang Backend",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/perijinan_view.xml",
        "views/perijinan_menu.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
