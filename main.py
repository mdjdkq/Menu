from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, RoundedRectangle
from kivy.core.window import Window

class GameMenu(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_minimized = False
        
        # Thiết lập kích thước menu ban đầu (Ví dụ: 300x250)
        self.menu_width = 600
        self.menu_height = 500
        
        # Nền của Menu chính
        with self.canvas.before:
            Color(0.17, 0.24, 0.31, 1) # Màu xám xanh đen
            self.bg_rect = RoundedRectangle(size=(self.menu_width, self.menu_height), pos=(100, 500), radius=[20])
        
        # Tiêu đề
        self.title = Label(text="FPS HELPER MENU", font_size='20sp', bold=True,
                           size_hint=(None, None), size=(self.menu_width, 50),
                           pos=(100, 500 + self.menu_height - 60))
        self.add_widget(self.title)
        
        # Các nút tính năng (Checkbox/Toggle)
        self.btn_aim = ToggleButton(text="Bật Aim Assist", size_hint=(None, None), size=(400, 60), pos=(200, 800))
        self.btn_esp_bone = ToggleButton(text="Bật ESP Khung Xương", size_hint=(None, None), size=(400, 60), pos=(200, 700))
        self.btn_esp_hp = ToggleButton(text="Bật ESP Thanh Máu", size_hint=(None, None), size=(400, 60), pos=(200, 600))
        
        self.add_widget(self.btn_aim)
        self.add_widget(self.btn_esp_bone)
        self.add_widget(self.btn_esp_hp)
        
        # Nút thu nhỏ
        self.btn_toggle = Button(text="Thu nhỏ (M)", size_hint=(None, None), size=(400, 60), pos=(200, 520),
                                 background_color=(0.9, 0.3, 0.2, 1))
        self.btn_toggle.bind(on_press=self.toggle_menu)
        self.add_widget(self.btn_toggle)

    def toggle_menu(self, instance):
        if not self.is_minimized:
            # Chuyển sang chế độ thu nhỏ thành nút tròn chữ M
            self.is_minimized = True
            
            # Ẩn giao diện chính
            self.remove_widget(self.title)
            self.remove_widget(self.btn_aim)
            self.remove_widget(self.btn_esp_bone)
            self.remove_widget(self.btn_esp_hp)
            
            # Xóa nền cũ, vẽ nền tròn nhỏ cho nút M
            self.canvas.before.clear()
            with self.canvas.before:
                Color(0.1, 0.7, 0.6, 1) # Màu xanh ngọc
                self.bg_rect = Ellipse(size=(120, 120), pos=(100, 500))
            
            # Thay đổi nút toggle thành chữ M tròn
            self.btn_toggle.text = "M"
            self.btn_toggle.size = (120, 120)
            self.btn_toggle.pos = (100, 500)
            self.btn_toggle.background_color = (0, 0, 0, 0) # Làm trong suốt nút bấm để lộ hình tròn canvas
            
        else:
            # Phóng to lại Menu đầy đủ
            self.is_minimized = False
            
            self.canvas.before.clear()
            with self.canvas.before:
                Color(0.17, 0.24, 0.31, 1)
                self.bg_rect = RoundedRectangle(size=(self.menu_width, self.menu_height), pos=(100, 500), radius=[20])
            
            # Khôi phục nút toggle
            self.btn_toggle.text = "Thu nhỏ (M)"
            self.btn_toggle.size = (400, 60)
            self.btn_toggle.pos = (200, 520)
            self.btn_toggle.background_color = (0.9, 0.3, 0.2, 1)
            
            # Hiện lại các thành phần
            self.add_widget(self.title)
            self.add_widget(self.btn_aim)
            self.add_widget(self.btn_esp_bone)
            self.add_widget(self.btn_esp_hp)

class FPSApp(App):
    def build(self):
        return GameMenu()

if __name__ == '__main__':
    FPSApp().run()
  
