import QuickUI

def check_age(age: int) -> str:
    if age >= 18:
        return "Can drive"
    else:
        return "Can't drive"


QuickUI.create_window(user_padding=10, title="QuickUI - drive test")
QuickUI.create_label(info="Can you drive?", y=0)
user_age = QuickUI.create_entry(default="Age", y=1)
QuickUI.create_button(info="Check", y=2, command=lambda: QuickUI.show_message("QuickUI", check_age(age=int(user_age.get()))))
QuickUI.refresh_ui()