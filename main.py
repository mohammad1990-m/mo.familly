import flet as ft

def main(page: ft.Page):
    page.title = "عيلة محمد"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 0  # صفرناها عشان الخلفية المتدرجة تغطي الشاشة كاملة

    # بيانات أفراد عائلة محمد الكريمة
    family_members = [
        {
            "name": "محمد",
            "full_name": "محمد ابراهيم صالح محمد",
            "role": "الأب",
            "gender": "ذكر",
            "age": "36 سنة",
            "study": "هندسة ميكانيك",
            "work": "فيلادلفيا للطاقة الشمسية",
            "image": "https://cdn-icons-png.flaticon.com/512/145/145867.png"
        },
        {
            "name": "الاء",
            "full_name": "الاء احمد عبد المجيد مصلح",
            "role": "الام",
            "gender": "أنثى",
            "age": "32 سنة",
            "study": "إدارة أعمال",
            "work": "ربة منزل",
            "image": "https://cdn-icons-png.flaticon.com/512/145/145866.png"
        },
        {
            "name": "لارين",
            "full_name": "لارين محمد ابراهيم محمد",
            "role": "ابنه",
            "gender": "أنثى",
            "age": "6 سنوات",
            "study": "اول ابتدائي",
            "work": "لا يوجد",
            "image": "https://cdn-icons-png.flaticon.com/512/2922/2922561.png"
        },
        {
            "name": "نايا",
            "full_name": "نايا محمد ابراهيم محمد",
            "role": "أنثى",
            "age": "4 سنوات",
            "study": "KG1",
            "work": "لا يوجد",
            "image": "https://cdn-icons-png.flaticon.com/512/2922/2922566.png"
        }
    ]

    # حاوية المحتوى الرئيسي المتغيرة
    content_area = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO
    )

    current_selected_member = None

    def on_file_picked(e: ft.FilePickerResultEvent):
        if e.files and current_selected_member:
            current_selected_member["image"] = e.files[0].path
            show_details(current_selected_member)

    file_picker = ft.FilePicker(on_result=on_file_picked)
    page.overlay.append(file_picker)

    def show_home(e=None):
        content_area.controls.clear()
        
        content_area.controls.append(ft.Container(height=10))
        content_area.controls.append(
            ft.Text("عيلة محمد", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.PINK_800)
        )
        content_area.controls.append(
            ft.Text("اختر فرداً لعرض وتعديل تفاصيله:", size=15, color=ft.colors.PINK_900)
        )
        content_area.controls.append(ft.Divider(height=20, color=ft.colors.PINK_200))

        grid = ft.GridView(
            expand=False,
            runs_count=2,
            max_extent=160,
            child_aspect_ratio=0.9,
            spacing=15,
            run_spacing=15,
        )

        for member in family_members:
            card = ft.GestureDetector(
                on_tap=lambda m=member: show_details(m),
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.CircleAvatar(
                                backgroundImage=ft.NetworkImage(member["image"]) if member["image"].startswith("http") else None,
                                radius=35,
                            ),
                            ft.Text(member["name"], weight=ft.FontWeight.BOLD, size=16, color=ft.colors.BLACK87),
                            ft.Text(member["role"], size=13, color=ft.colors.PINK_700),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=ft.colors.WHITE,
                    border_radius=15,
                    padding=10,
                    shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.colors.PINK_100),
                )
            )
            grid.controls.append(card)

        content_area.controls.append(grid)
        page.update()

    def show_details(member):
        nonlocal current_selected_member
        current_selected_member = member
        
        content_area.controls.clear()

        content_area.controls.append(ft.Container(height=10))
        content_area.controls.append(
            ft.CircleAvatar(
                backgroundImage=ft.NetworkImage(member["image"]) if member["image"].startswith("http") else None,
                radius=50,
            )
        )
        content_area.controls.append(
            ft.Text(member["name"], size=24, weight=ft.FontWeight.BOLD, color=ft.colors.PINK_900)
        )
        content_area.controls.append(
            ft.Text(f"الصفة: {member['role']}", size=16, italic=True, color=ft.colors.PINK_700)
        )
        
        change_img_btn = ft.TextButton(
            text="تغيير الصورة الشخصية",
            icon=ft.icons.PHOTO_CAMERA,
            icon_color=ft.colors.PINK_600,
            on_click=lambda _: file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.IMAGE),
        )
        content_area.controls.append(change_img_btn)
        content_area.controls.append(ft.Divider(height=10, color=ft.colors.PINK_200))
        
        details_text = (
            f"الاسم الكامل: {member['full_name']}\n"
            f"الجنس: {member['gender']}\n"
            f"العمر: {member['age']}\n"
            f"الدراسة: {member['study']}\n"
            f"العمل: {member['work']}"
        )
        
        content_area.controls.append(
            ft.Container(
                content=ft.Text(details_text, size=15, text_align=ft.TextAlign.START, color=ft.colors.BLACK87),
                padding=15,
                bgcolor=ft.colors.WHITE,
                border_radius=10,
                width=320,
                shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=ft.colors.PINK_100),
            )
        )
        
        content_area.controls.append(ft.Container(height=15))

        back_btn = ft.ElevatedButton(
            text="الرجوع لقائمة العائلة",
            icon=ft.icons.ARROW_BACK,
            on_click=show_home,
            bgcolor=ft.colors.PINK_600,
            color=ft.colors.WHITE,
        )
        content_area.controls.append(back_btn)
        page.update()

    show_home()

    # الخلفية المتداخلة المتدرجة (Gradient) من الزهري الفاتح إلى الأبيض
    background_container = ft.Container(
        content=content_area,
        expand=True,
        alignment=ft.alignment.center,
        padding=20,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.colors.PINK_100, ft.colors.WHITE, ft.colors.PINK_50],
        ),
    )

    page.add(background_container)
