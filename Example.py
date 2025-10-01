import QuickUI

agreed = None

def check_age(age: int) -> str:
    global agreed
    if not agreed.get():
        return "Agree to T&C"

    if age >= 18:
        return "Can drive"
    else:
        return "Can't drive"


QuickUI.create_window(user_padding=10, title="QuickUI - drive test")
QuickUI.create_label(info="Can you drive?", y=0)
user_age = QuickUI.create_entry(default="Age", y=1)
agreed = QuickUI.create_checkbox(info="Agree to T&C", y=2)
QuickUI.create_button(info="Check", y=3, command=lambda: QuickUI.show_message("QuickUI", check_age(age=int(user_age.get()))))
QuickUI.refresh_ui()