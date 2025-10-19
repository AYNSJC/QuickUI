import QuickUI

# State variables
age_entry = None
terms_checkbox = None
category_dropdown = None
experience_spinbox = None
notes_text = None
countries_listbox = None
progress_var = None
skill_slider = None
result_label = None
color_display = None


def show_file_browser():
    """Opens file dialog and shows result"""
    file_path = QuickUI.show_file_dialog(title="Select a file", file_types=[("Python", "*.py"), ("All Files", "*.*")])
    if file_path:
        QuickUI.show_message("File Selected", f"Path: {file_path}")


def show_folder_browser():
    """Opens folder dialog and shows result"""
    folder_path = QuickUI.show_folder_dialog(title="Select a folder")
    if folder_path:
        QuickUI.show_message("Folder Selected", f"Path: {folder_path}")


def pick_color():
    """Opens color picker"""
    global color_display
    color = QuickUI.show_color_picker(title="Choose your favorite color")
    if color:
        QuickUI.show_message("Color Selected", f"Color code: {color}")
        if color_display:
            QuickUI.remove_widget(color_display)
        color_display = QuickUI.create_label(info=f"Selected: {color}", y=17)


def validate_and_check():
    """Validates input and determines driving eligibility"""
    global result_label

    # Check if terms are accepted
    if not terms_checkbox.get():
        QuickUI.show_warning("Terms Required", "Please agree to the Terms & Conditions")
        return

    # Validate age input
    try:
        age = int(age_entry.get())
        if age < 0 or age > 150:
            raise ValueError
    except ValueError:
        QuickUI.show_error("Invalid Input", "Please enter a valid age (0-150)")
        return

    # Get other form data
    category = category_dropdown.get()
    experience = experience_spinbox.get()
    notes = notes_text.get("1.0", "end-1c")
    selected_countries = countries_listbox.curselection()
    skill_level = skill_slider.get()

    # Build message
    message = f"""
    Age: {age} years old
    License Category: {category}
    Years of Experience: {experience}
    Skill Level: {skill_level}/100
    Notes: {notes if notes else 'None'}
    Selected Countries: {', '.join([countries_listbox.get(i) for i in selected_countries]) if selected_countries else 'None'}
    """

    # Determine eligibility
    if age >= 18:
        eligibility = f"✓ At age {age}, you CAN drive!"
    else:
        eligibility = f"✗ At age {age}, you CANNOT drive yet.\nYou can drive in {18 - age} years."

    # Update result display
    if result_label:
        QuickUI.remove_widget(result_label)

    result_label = QuickUI.create_label(
        info=eligibility,
        y=18,
        font=("Arial", 12, "bold")
    )

    # Show confirmation dialog
    QuickUI.show_message("Eligibility Check", eligibility + message)


def update_progress():
    """Updates progress bar"""
    current = progress_var.get()
    if current < 100:
        progress_var.set(current + 10)
    else:
        progress_var.set(0)


def clear_all():
    """Clears all widgets and resets"""
    if QuickUI.show_question("Clear All", "Remove all widgets and reset form?"):
        QuickUI.remove_all_widgets()
        initialize_ui()


def initialize_ui():
    """Initialize/reinitialize the UI"""
    global age_entry, terms_checkbox, category_dropdown, experience_spinbox
    global notes_text, countries_listbox, progress_var, skill_slider, result_label

    # Header
    QuickUI.create_label(
        info="🚗 Advanced Driving License Checker",
        y=0,
        font=("Arial", 16, "bold")
    )
    QuickUI.create_separator(y=1, orient="horizontal")

    # Age input
    QuickUI.create_label(info="Enter your age:", y=2)
    age_entry = QuickUI.create_entry(y=3, default="18")

    # License category dropdown
    QuickUI.create_label(info="License Category:", y=4)
    category_dropdown = QuickUI.create_dropdown(
        options=["Class A (Motorcycle)", "Class B (Car)", "Class C (Truck)", "Class D (Bus)"],
        y=5,
        default=1
    )

    # Experience spinbox
    QuickUI.create_label(info="Years of Experience:", y=6)
    experience_spinbox = QuickUI.create_spinbox(y=7, from_=0, to=60, default=0)

    # Skills slider
    QuickUI.create_label(info="Skill Level:", y=8)
    skill_slider = QuickUI.create_slider(y=9, from_=0, to=100)

    # Notes text area
    QuickUI.create_label(info="Additional Notes:", y=10)
    notes_text = QuickUI.create_text(y=11, width=40, height=3)

    # Countries listbox
    QuickUI.create_label(info="Valid in Countries:", y=12)
    countries_listbox = QuickUI.create_listbox(
        items=["India", "USA", "Canada", "Germany", "France", "Japan"],
        y=13,
        height=4
    )

    # Progress bar
    QuickUI.create_label(info="Test Progress:", y=14)
    progress_var = QuickUI.create_progressbar(y=15, max_value=100)

    # Separator
    QuickUI.create_separator(y=16, orient="horizontal")

    # Terms checkbox
    terms_checkbox = QuickUI.create_checkbox(
        info="I agree to the Terms & Conditions",
        y=17
    )

    # Buttons (Horizontal layout using columns)
    QuickUI.create_button(info="📁 Open File", x=0, y=18, command=show_file_browser)
    QuickUI.create_button(info="📂 Open Folder", x=1, y=18, command=show_folder_browser)
    QuickUI.create_button(info="🎨 Pick Color", x=2, y=18, command=pick_color)

    QuickUI.create_button(info="📊 Progress +10%", x=0, y=19, command=update_progress)
    QuickUI.create_button(info="✅ Check Eligibility", x=1, y=19, command=validate_and_check)
    QuickUI.create_button(info="🔄 Clear All", x=2, y=19, command=clear_all)

    result_label = QuickUI.create_label(info="Results will appear here", y=20, font=("Arial", 10))


# Create window
QuickUI.create_window(
    user_padding=10,
    title="QuickUI - Advanced Driving License Checker",
    dimensions=(600, 900)
)

# Initialize UI
initialize_ui()

# Refresh UI
QuickUI.refresh_ui()