import QuickUI

# Logic -- Can be ignored --
def check_age(age: int) -> str:
    if not agreed.get():
        return "Agree to T&C"

    if age >= 18:
        return "Can drive"
    else:
        return "Can't drive"

# Creates window
QuickUI.create_window(user_padding=10, title="QuickUI - drive test")

# Creates text
QuickUI.create_label(info="Can you drive?", y=0)

# Takes Input
user_age = QuickUI.create_entry(default="Age", y=1)

# Takes Checkbox Input
agreed = QuickUI.create_checkbox(info="Agree to T&C", y=2)

# Creates button
QuickUI.create_button(info="Check", y=3, command=lambda: QuickUI.show_message("QuickUI", check_age(age=int(user_age.get()))))

# Refresh UI screen
QuickUI.refresh_ui()