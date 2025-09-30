import QuickUI

information:str = "Hello World!"

QuickUI.create_window(20, "Cool Program", [720, 640])
QuickUI.create_label(information, 0, 0)
QuickUI.create_button("Button", 1, 0)
QuickUI.refresh_ui()