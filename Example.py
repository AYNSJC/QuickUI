import QuickUI

QuickUI.create_window()
QuickUI.create_label("QuickUI's Important question:", y=0, x=0)
entry = QuickUI.create_entry(y=0, x=1)
QuickUI.create_checkbox("True?", y=1, x=0)
QuickUI.create_button("Cool!", y=2, x=0)
QuickUI.refresh_ui()