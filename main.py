# -*- coding: utf-8 -*-
import hashlib
import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.utils import platform
from kivy.core.text import LabelBase

# ========== 中文字体 ==========
def register_fonts():
    try:
        if platform == 'android':
            for font_path in [
                '/system/fonts/NotoSansCJK-Regular.ttc',
                '/system/fonts/NotoSansSC-Regular.otf',
                '/system/fonts/DroidSansFallback.ttf',
                '/system/fonts/Roboto-Regular.ttf'
            ]:
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
            for font_path in [
                '/usr/share/fonts/truetype/droid/DroidSansFallback.ttf',
                '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
                '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc'
            ]:
                try:
                    LabelBase.register(name='Roboto', fn_regular=font_path)
                    return
                except:
                    continue
    except:
        pass

register_fonts()

# ========== 口令哈希（与 C# 版一致） ==========
PASSWORD_HASH = "dc2ec75ff1bfcd8208738fe9014cbb2f8db458a73fed4cd68f8e118cd8199137"

def validate_password(input_password):
    if not input_password:
        return False
    return hashlib.sha256(input_password.encode()).hexdigest() == PASSWORD_HASH

# ========== 工具箱清单（与 C# 版一致） ==========
_toolbox_list = [
    {"code": "ForestProcessor",  "name": "自动处理平台"},
    {"code": "ForestAutomator",  "name": "小班属性处理"},
    {"code": "RasterGeneration", "name": "专题栅格生成"}
]

def get_toolbox_code(display_name):
    for item in _toolbox_list:
        if item["name"] == display_name:
            return item["code"]

def get_display_names():
    return [item["name"] for item in _toolbox_list]

# ========== 天数编码（与 C# 版一致） ==========
def encode_days(days, signature_prefix):
    try:
        days_bytes = days.to_bytes(2, byteorder='big')
        key_bytes = bytes.fromhex(signature_prefix)[:2]
        encoded = bytes(a ^ b for a, b in zip(days_bytes, key_bytes * 2))
        return encoded.hex().upper()
    except:
        return "0000"

def generate_regcode(toolbox_code, machine_code, days):
    clean_machine = machine_code.replace('-', '')
    today = datetime.datetime.now().strftime("%Y%m%d")
    raw = f"{toolbox_code}|{clean_machine}|{days}|{today}"
    full_hash = hashlib.sha256(toolbox_code.encode() + raw.encode()).hexdigest().upper()
    signature = full_hash[:28]
    days_code = encode_days(days, signature[:8])
    return signature + days_code

# ========== 路径规则（与 C# ToolboxPathInfo 一致） ==========
_LEGACY_CODES = ("ForestAutomator", "RasterGeneration")

def _md5_fake_uuid(code):
    h = hashlib.md5(code.encode()).hexdigest().upper()
    return f"{h[0:8]}-{h[8:12]}-{h[12:16]}-{h[16:20]}-{h[20:32]}"

def get_path_info(toolbox_code):
    if toolbox_code in _LEGACY_CODES:
        return {
            "file1": f"%LOCALAPPDATA%\\ESRI_Licensing\\ProLicensing\\{toolbox_code}.lic",
            "file2": f"%APPDATA%\\ESRI\\ArcGISPro\\Licenses\\{toolbox_code}.lic",
            "reg_path": r"HKEY_CURRENT_USER\Software\ESRI\ArcGISPro\Licenses",
            "reg_key": _md5_fake_uuid(toolbox_code)
        }
    return {
        "file1": f"%PROGRAMDATA%\\{toolbox_code}\\license.lic",
        "file2": f"%APPDATA%\\{toolbox_code}\\license.lic",
        "reg_path": f"HKEY_CURRENT_USER\\Software\\{toolbox_code}",
        "reg_key": "LicenseHash / Timestamp"
    }

# ========== 主界面 ==========
class LicenseGeneratorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(10)
        self.spacing = dp(4)

        self.add_widget(Label(
            text="注册码生成工具_sxh", size_hint_y=0.07,
            font_size=sp(20), color=(0.2, 0.6, 1, 1), bold=True
        ))

        # 第1行：工具 + 天数
        row1 = BoxLayout(orientation='horizontal', size_hint_y=0.06, spacing=dp(8))
        row1.add_widget(Label(text="授权工具:", size_hint_x=0.18, font_size=sp(12)))
        self.toolbox_spinner = Spinner(
            text='请选择', values=get_display_names(),
            size_hint_x=0.48, font_size=sp(12),
            background_color=(0.8, 0.8, 0.8, 1)
        )
        row1.add_widget(self.toolbox_spinner)
        row1.add_widget(Label(text="天数:", size_hint_x=0.12, font_size=sp(12)))
        self.days_input = TextInput(
            hint_text='1-3650', size_hint_x=0.22, font_size=sp(12),
            multiline=False, input_filter='int', padding=(dp(8), dp(8))
        )
        self.days_input.text = '365'
        row1.add_widget(self.days_input)
        self.add_widget(row1)

        # 第2行：机器码
        row2 = BoxLayout(orientation='horizontal', size_hint_y=0.06, spacing=dp(8))
        row2.add_widget(Label(text="机器码:", size_hint_x=0.18, font_size=sp(12)))
        self.machine_input = TextInput(
            size_hint_x=0.82, font_size=sp(12), multiline=False,
            hint_text='ABCD-EFGH-IJKL-MNOP', padding=(dp(8), dp(8))
        )
        row2.add_widget(self.machine_input)
        self.add_widget(row2)

        # 第3行：口令 + 按钮
        row3 = BoxLayout(orientation='horizontal', size_hint_y=0.06, spacing=dp(8))
        row3.add_widget(Label(text="口令:", size_hint_x=0.18, font_size=sp(12)))
        self.password_input = TextInput(
            size_hint_x=0.42, font_size=sp(12), multiline=False,
            password=True, hint_text='请输入...', padding=(dp(8), dp(8))
        )
        row3.add_widget(self.password_input)
        self.generate_btn = Button(
            text="生成注册码", size_hint_x=0.40, font_size=sp(14),
            background_color=(0.2, 0.6, 1, 1), color=(1, 1, 1, 1)
        )
        self.generate_btn.bind(on_press=self.generate_license)
        row3.add_widget(self.generate_btn)
        self.add_widget(row3)

        # 输出区（最大空间）
        self.output_text = TextInput(
            size_hint_y=0.72, font_size=sp(12), readonly=True, multiline=True,
            background_color=(0.95, 0.95, 0.95, 1), foreground_color=(0, 0, 0, 1),
            padding=(8, 8)
        )
        self.add_widget(self.output_text)

        self.status_label = Label(
            text="就绪", size_hint_y=0.03, font_size=sp(10),
            color=(0.5, 0.5, 0.5, 1), halign='left'
        )
        self.add_widget(self.status_label)

    def validate_machine_code(self, code):
        if not code:
            return False, "机器码不能为空"
        parts = code.split('-')
        if len(parts) != 4:
            return False, "格式应为 ABCD-EFGH-IJKL-MNOP"
        for p in parts:
            if len(p) != 4:
                return False, f"每段必须为4位: {p}"
        return True, "格式正确"

    def generate_license(self, instance):
        self.output_text.text = ''
        toolbox_name = self.toolbox_spinner.text
        machine_code = self.machine_input.text.strip().upper()
        days_str = self.days_input.text.strip()
        password = self.password_input.text

        if toolbox_name == '请选择':
            return self.set_status("错误: 请选择授权工具", True)

        ok, msg = self.validate_machine_code(machine_code)
        if not ok:
            return self.set_status(f"错误: {msg}", True)

        try:
            days = int(days_str)
            if days < 1 or days > 3650:
                return self.set_status("错误: 天数必须在1-3650之间", True)
        except ValueError:
            return self.set_status("错误: 请输入有效的天数", True)

        if not validate_password(password):
            return self.set_status("错误: 口令错误!", True)

        try:
            toolbox_code = get_toolbox_code(toolbox_name)
            reg_code = generate_regcode(toolbox_code, machine_code, days)
            info = get_path_info(toolbox_code)
            date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            lines = [
                "=============================================",
                "注册码生成工具",
                "=============================================",
                f"工具名：{toolbox_name}",
                f"机器码：{machine_code}",
                f"授权天数：{days}",
                "---------------------------------------------",
                "",
                "【注册码】",
                reg_code,
                "",
                "---------------------------------------------",
                "【授权文件信息】",
                f"主路径：{info['file1']}",
                f"备路径：{info['file2']}",
                "",
                "【注册表信息】",
                f"路径：{info['reg_path']}",
                f"键名：{info['reg_key']}",
                "---------------------------------------------",
                "",
                "          shuxinghua , 93535012@qq.com",
                f"             {date_str}",
                "============================================="
            ]
            self.output_text.text = "\n".join(lines)
            self.set_status("注册码生成成功!", False)
        except Exception as e:
            self.set_status(f"错误: 生成失败 - {e}", True)

    def set_status(self, msg, is_error):
        self.status_label.text = msg
        self.status_label.color = (1, 0, 0, 1) if is_error else (0, 0.7, 0, 1)


class LicenseGeneratorApp(App):
    def build(self):
        self.title = "注册码生成工具"
        if platform == 'win':
            Window.size = (400, 800)
        return LicenseGeneratorLayout()


if __name__ == '__main__':
    LicenseGeneratorApp().run()
