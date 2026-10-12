import flet as ft
import sys  # مكتبة النظام الأساسية لإغلاق التطبيق

# قاموس معلومات عيلة محمد (قاعدة البيانات المحدثة)
family_catalog = {
    "محمد": "الاسم الكامل: كامل محمد ابراهيم صالح محمد\nالجنس: ذكر\nالصفة: الأب\nالعمر: 36 سنة\nالدراسة: هندسة ميكانيك\nالعمل: فيلادلفيا للطاقة الشمسية",
    "الاء": "الاسم الكامل: آلاء أحمد عبد المجيد مصلح\nالجنس: أنثى\nالصفة: الأم\nالعمر: 32 سنة\nالدراسة: إدارة أعمال\nالعمل: ربة منزل",
    "لارين": "الاسم الكامل: لارين محمد ابراهيم محمد\nالجنس: أنثى\nالصفة: ابنة\nالعمر: 6 سنوات\nالدراسة: أول ابتدائي\nالعمل: لا يوجد",
    "نايا": "الاسم الكامل: نايا محمد ابراهيم محمد\nالجنس: أنثى\nالصفة: ابنة\nالعمر: 4 سنوات\nالدراسة: KG1\nالعمل: لا يوجد"
}

def main(page: ft.Page):
    page.title = "عيلة محمد"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    # دالة إغلاق التطبيق المضمونة 100%
    def close_app(e):
        sys.exit(0)

    # دالة الانتقال لشاشة البحث عن أفراد العائلة
    def go_to_family_system(e):
        page.clean()  # مسح واجهة الترحيب
        
        # عناصر واجهة البحث عن أفراد العائلة
        name_input = ft.TextField(label="اكتب اسم الشخص (مثال: محمد، الاء، لارين، نايا)")
        result_text = ft.Text(value="ستظهر معلومات الشخص هنا...", size=16)

        def search_family_member(e):
            entered_name = name_input.value.strip().lower()
            found = False
            for name, info in family_catalog.items():
                if name.lower() in entered_name:
                    result_text.value = f"📋 معلومات الشخص:\n{info}"
                    result_text.color = ft.Colors.GREEN
                    found = True
                    break
            
            if not found:
                result_text.value = "❌ عذراً، هذا الاسم غير متوفر في سجل عيلة محمد!"
                result_text.color = ft.Colors.RED
            page.update()

        search_button = ft.Container(
            content=ft.Text("بحث عن الشخص", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.BLUE,
            padding=10,
            border_radius=5,
            on_click=search_family_member
        )

        # زر خروج من التطبيق
        exit_button = ft.Container(
            content=ft.Text("خروج من التطبيق", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.RED,
            padding=10,
            border_radius=5,
            on_click=close_app
        )

        # إضافة عناصر واجهة العائلة للصفحة
        page.add(
            ft.Text("✨ دليل أفراد عيلة محمد ✨", size=22, weight=ft.FontWeight.BOLD),
            name_input,
            search_button,
            result_text,
            exit_button
        )
        page.update()

    # --- واجهة الترحيب الأولية ---
    start_button = ft.Container(
        content=ft.Text("دخول لعيلة محمد", size=18, color=ft.Colors.WHITE),
        bgcolor=ft.Colors.GREEN,
        padding=15,
        border_radius=8,
        on_click=go_to_family_system
    )

    # عرض واجهة الترحيب أول ما يفتح التطبيق
    page.add(
        ft.Text("أهلاً بك في تطبيق عيلة محمد", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
        start_button
    )
    page.update()

ft.run(main)