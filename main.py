# -*- coding: utf-8 -*-
import hashlib
import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.utils import platform
from kivy.core.text import LabelBase

# ========== 设置中文字体 ==========
def register_fonts():
    try:
        if platform == 'android':
            android_fonts = [
                '/system/fonts/NotoSansCJK-Regular.ttc',
                '/system/fonts/NotoSansSC-Regular.otf',
                '/system/fonts/DroidSansFallback.ttf',
                '/system/fonts/Roboto-Regular.ttf'
            ]
            for font_path in android_fonts:
                try:
                    LabelBase.register(name='Roboto', fn_regular=font_path)
                    return
                except:
                    continue
        elif platform == 'win':
            LabelBase.register(name='Roboto', fn_regular='C:/Windows/Fonts/msyh.ttc')
        elif platform == 'macosx':
            try:
                LabelBase.register(name='Roboto', fn_regular='/System/Library/Fonts/PingFang.ttc')
            except:
                LabelBase.register(name='Roboto', fn_regular='/System/Library/Fonts/STHeiti Light.ttc')
        else:
            linux_fonts = [
                '/usr/share/fonts/truetype/droid/DroidSansFallback.ttf',
                '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
                '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc'
            ]
            for font_path in linux_fonts:
                try:
                    LabelBase.register(name='Roboto', fn_regular=font_path)
                    return
                except:
                    continue
    except:
        pass

register_fonts()

# ========== 安全验证 ==========
PASSWORD_HASH = "dc2ec75ff1bfcd8208738fe9014cbb2f8db458a73fed4cd68f8e118cd8199137"

def validate_password(input_password):
    if not input_password:
        return False
    input_hash = hashlib.sha256(input_password.encode()).hexdigest()
    return input_hash == PASSWORD_HASH

# ========== 全局工具箱信息 ==========
_toolbox_list = [
    {"code": "ForestAutomator", "name": "小班属性处理"},
    {"code": "RasterGeneration", "name": "专题栅格生成"}
]

def get_toolbox_code(display_name):
    for item in _toolbox_list:
        if item["name"] == display_name:
            return item["code"]

def get_display_names():
    return [item["name"] for item in _toolbox_list]

def encode_days(days, signature_prefix):
    try:
        days_bytes = days.to_bytes(2, byteorder='big')
        key_bytes = bytes.fromhex(signature_prefix)[:2]
        encoded_bytes = bytes(a ^ b for a, b in zip(days_bytes, key_bytes * 2))
        return encoded_bytes.hex().upper()
    except:
        return "0000"

def generate_regcode(toolbox_code, machine_code, days):
    clean_machine = machine_code.replace('-', '')
    today = datetime.datetime.now().strftime("%Y%m%d")
    raw = f"{toolbox_code}|{clean_machine}|{days}|{today}"
    
    full_hash = hashlib.sha256(toolbox_code.encode() + raw.encode()).hexdigest().upper()
    base_signature = full_hash[:28]
    days_code = encode_days(days, base_signature[:8])
    reg_code = base_signature + days_code
    return reg_code

# ========== 主界面 ==========
class LicenseGeneratorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(10)
        self.spacing = dp(5)
        
        # 标题
        title = Label(
            text="注册码生成工具 v2.3",
            size_hint_y=0.07,
            font_size=sp(20),
            color=(0.2, 0.6, 1, 1),
            bold=True
        )
        self.add_widget(title)
        
        # ========== 第1行：授权工具 + 天数 ==========
        row1 = BoxLayout(orientation='horizontal', size_hint_y=0.07, spacing=dp(10))
        row1.add_widget(Label(text="授权工具:", size_hint_x=0.25, font_size=sp(12)))
        self.toolbox_spinner = Spinner(
            text='请选择',
            values=get_display_names(),
            size_hint_x=0.45,
            font_size=sp(12),
            background_color=(0.8, 0.8, 0.8, 1)
        )
        row1.add_widget(self.toolbox_spinner)
        row1.add_widget(Label(text="天数:", size_hint_x=0.12, font_size=sp(12)))
        self.days_input = TextInput(
            text='365', 
            size_hint_x=0.18, 
            font_size=sp(12), 
            multiline=False, 
            input_filter='int'
        )
        row1.add_widget(self.days_input)
        self.add_widget(row1)
        
        # ========== 第2行：机器码 ==========
        row2 = BoxLayout(orientation='horizontal', size_hint_y=0.07, spacing=dp(10))
        row2.add_widget(Label(text="机器码:", size_hint_x=0.2, font_size=sp(12)))
        self.machine_input = TextInput(
            text='',
            size_hint_x=0.8,
            font_size=sp(12),
            multiline=False,
            hint_text='ABCD-EFGH-IJKL-MNOP'
        )
        row2.add_widget(self.machine_input)
        self.add_widget(row2)
        
        # ========== 第3行：口令 + 按钮 ==========
        row3 = BoxLayout(orientation='horizontal', size_hint_y=0.08, spacing=dp(10))
        row3.add_widget(Label(text="口令:", size_hint_x=0.2, font_size=sp(12)))
        self.password_input = TextInput(
            text='', 
            size_hint_x=0.45, 
            font_size=sp(12), 
            multiline=False, 
            password=True
        )
        row3.add_widget(self.password_input)
        
        self.generate_btn = Button(
            text="生成注册码",
            size_hint_x=0.35,
            font_size=sp(14),
            background_color=(0.2, 0.6, 1, 1),
            color=(1, 1, 1, 1)
        )
        self.generate_btn.bind(on_press=self.generate_license)
        row3.add_widget(self.generate_btn)
        self.add_widget(row3)
        
        # ========== 输出区域：ScrollView + TextInput（关键修改）==========
        # ScrollView 负责滚动
        output_scroll = ScrollView(
            do_scroll_x=False,
            do_scroll_y=True,
            size_hint_y=0.68
        )
        
        # TextInput 禁用内部滚动，只负责显示和复制
        self.output_text = TextInput(
            text='',
            size_hint_y=None,           # 高度自适应
            height=0,
            font_size=sp(12),
            readonly=True,
            multiline=True,
            do_scroll_y=False,           # 关键！禁用内部滚动
            background_color=(0.95, 0.95, 0.95, 1),
            foreground_color=(0, 0, 0, 1),
            selection_color=(0.3, 0.6, 1, 0.3),
            cursor_color=(0.2, 0.6, 1, 1),
            padding=(8, 8)
        )
        
        # 让文本框高度自适应内容
        self.output_text.bind(minimum_height=self.output_text.setter('height'))
        
        output_scroll.add_widget(self.output_text)
        self.add_widget(output_scroll)
        
        # ========== 状态栏 ==========
        self.status_label = Label(
            text="就绪", 
            size_hint_y=0.02, 
            font_size=sp(12), 
            color=(0.5, 0.5, 0.5, 1),
            halign='left'
        )
        self.add_widget(self.status_label)
    
    def validate_machine_code(self, code):
        if not code:
            return False, "机器码不能为空"
        parts = code.split('-')
        if len(parts) != 4:
            return False, "格式应为 ABCD-EFGH-IJKL-MNOP"
        for part in parts:
            if len(part) != 4:
                return False, f"每段必须为4位: {part}"
        return True, "格式正确"
    
    def generate_license(self, instance):
        self.output_text.text = ''
        toolbox_name = self.toolbox_spinner.text
        machine_code = self.machine_input.text.strip().upper()
        days_str = self.days_input.text.strip()
        password = self.password_input.text
        
        if toolbox_name == '请选择':
            self.status_label.text = "错误: 请选择授权工具"
            self.status_label.color = (1, 0, 0, 1)
            return
        
        is_valid, msg = self.validate_machine_code(machine_code)
        if not is_valid:
            self.status_label.text = f"错误: {msg}"
            self.status_label.color = (1, 0, 0, 1)
            return
        
        try:
            days = int(days_str)
            if days < 1 or days > 3650:
                self.status_label.text = "错误: 天数必须在1-3650之间"
                self.status_label.color = (1, 0, 0, 1)
                return
        except ValueError:
            self.status_label.text = "错误: 请输入有效的天数"
            self.status_label.color = (1, 0, 0, 1)
            return
        
        if not validate_password(password):
            self.status_label.text = "错误: 口令错误!"
            self.status_label.color = (1, 0, 0, 1)
            return
        
        try:
            toolbox_code = get_toolbox_code(toolbox_name)
            reg_code = generate_regcode(toolbox_code, machine_code, days)
            reg_key = hashlib.md5(toolbox_code.encode()).hexdigest().upper()
            
            output = []
            output.append("=" * 35)
            output.append("注册码生成工具")
            output.append("=" * 35)
            output.append(f"工具箱：{toolbox_name}")
            output.append(f"机器码：{machine_code}")
            output.append(f"授权天数：{days}")
            output.append("-" * 55)
            output.append("注册码生成成功！")
            output.append("")
            output.append("【注册码】")
            output.append(reg_code)
            output.append("")
            output.append("-" * 55)
            output.append("授权文件存放位置：")
            output.append(f"  1. %LOCALAPPDATA%\\ESRI_Licensing\\ProLicensing\\{toolbox_code}.lic")
            output.append(f"  2. %APPDATA%\\ESRI\\ArcGISPro\\Licenses\\{toolbox_code}.lic")
            output.append("")
            output.append("注册表信息：")
            output.append("  路径: HKEY_CURRENT_USER\\Software\\ESRI\\ArcGISPro\\Licenses")
            output.append(f"  键名: {reg_key[:8]}-{reg_key[8:12]}-{reg_key[12:16]}-{reg_key[16:20]}-{reg_key[20:32]}")
            output.append("")
            output.append("shuxinghua , 93535012@qq.com")
            output.append("=" * 35)
            
            self.output_text.text = "\n".join(output)
            self.status_label.text = "注册码生成成功!"
            self.status_label.color = (0, 0.7, 0, 1)
            
        except Exception as e:
            self.status_label.text = f"错误: 生成失败 - {str(e)}"
            self.status_label.color = (1, 0, 0, 1)


class LicenseGeneratorApp(App):
    def build(self):
        self.title = "注册码生成工具"
        if platform == 'win':
            Window.size = (400, 800)
        return LicenseGeneratorLayout()


if __name__ == '__main__':
    LicenseGeneratorApp().run()
