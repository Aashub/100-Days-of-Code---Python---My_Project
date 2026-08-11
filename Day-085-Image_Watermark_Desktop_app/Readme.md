# Day 85 – Image Watermarking Desktop App with Tkinter

## Project Overview

This is a fully functional Image Watermarking Desktop App built with Python's Tkinter library. The application allows users to upload an image, add custom text watermarks with full control over font family, font size, font color, text alignment, rotation angle, and text styling (bold, italic, underline). Users can drag the watermark anywhere on the image using their mouse, save the watermarked image in PNG or JPEG format, and create presets to save their favorite watermark settings for future use. The app features a clean, professional interface with an image canvas on the left and all editing controls on the right panel.

The code is also designed with a future upgrade in mind, a Batch Watermark mode where users can add watermarks to multiple images at once, which can be added later by extending the existing application structure.

## What I Have Learned

* **Tkinter GUI Development**: Revised how to build a professional desktop application using Python's Tkinter library. Created windows, canvases, frames, buttons, labels, entry fields, comboboxes, listboxes, radiobuttons, scales, and spinboxes.

* **Object-Oriented Programming (OOP)**: Built the entire application using classes. The UserInterface class inherits from Tk and contains all the methods for creating UI elements, handling user interactions, and managing application state.

* **Pillow (PIL) for Image Processing**: Learned how to use Pillow library to open, manipulate, and save images. Used Image.open() to load images, ImageTk.PhotoImage() to display them on canvas.
    
* **Event Binding and Mouse Interactions**: Used Tkinter's event binding system to capture mouse drag events (<B1-Motion>) for moving the watermark text on the image. Also used mouse wheel events (<MouseWheel>) for zooming in and out.
 
* **Canvas and Coordinate Systems**: Learned how to use Tkinter's Canvas widget to display images and text, and how to manage coordinate systems to place watermark text at exact positions on both the canvas and the original image.

* **Font Management**: Learned how to work with fonts in Tkinter - getting available font families, searching and filtering fonts, applying font styles (bold, italic, underline), and using font_manager to locate actual font files (.ttf) for saving images.
 
* **Combobox and Listbox Widgets**: Used Combobox for dropdown selections (alignment options, preset management) and Listbox for displaying search results (font families, font colors) with real-time filtering.

* **JSON for Data Persistence**: Revised how to use JSON files to save and load preset data. Created a preset system where users can save their watermark settings (text, font properties, color, angle, position) and apply them later.
 
* **Scaling and Zooming**: Implemented image zoom functionality using mouse wheel events. The image scales up or down while the watermark text maintains its relative position on the image.

* **Real-Time Search and Filter**: Implemented search functionality for font families and font colors. As the user types in the search box, the listbox updates in real-time to show matching results.
 
* **Keyboard Shortcuts**: Added keyboard shortcuts for text styling - Ctrl+B for bold, Ctrl+I for italic, and Ctrl+U for underline.

## How It Works

### main.py

* **Imports and Global Variables**: The file imports Tkinter modules, Pillow for image processing, font_manager for font handling, json for presets. Global variables define window size, heading text color, and allowed image file types. The UserInterface class inherits from Tk and manages the entire application.

* **__init__ Method**: Sets up the main application window with a centered position on the screen, fixed size, and title. Initializes all variables including font family, font size, watermark mode, alignment, zoom scale, font designs, and watermark colors. Loads font families and watermark colors from the data.py file and calls add_home_screen_image() to display the home screen.
 
* **add_home_screen_image()**:  Displays the background image on the home screen using a Label widget with a PhotoImage. Then calls `home_screen_heading_text()` to add text on top of the background.

* **home_screen_heading_text()**: This method Creates a Canvas widget and adds the main heading "Make watermark quickly" and a subheading "add watermark to single & several images in a breeze" with custom font styling and colors.

* **home_screen_button()**: Creates two buttons - "Start Make Watermark" which calls `display_watermarking_screen()` to open the main editing screen, and "Start Batch Watermark" which is a placeholder for future batch processing functionality.

* **display_watermarking_screen()**: This method first Destroys all widgets from the home screen using list comprehension and creates the main editing interface with two canvases, a large canvas on the left (800x700) for displaying images and watermark text, and a smaller canvas on the right (280x700) for all editing controls. Then calls `all_edit_button()` to populate the controls.

* **all_edit_button()**: Creates all the editing widgets on the right panel. This includes the watermark text entry field, alignment combobox, font styling radiobuttons (Bold, Italic, Underline, Reset), font design search box and listbox, font color search box and listbox, font size scale, rotation spinbox, preset management combobox and "Create Preset" button, and action buttons (Select Image, Save Image, Delete Image). Each widget is placed at specific coordinates on the editing canvas.

* **display_watermark_text()**: This method First checks if an image is loaded on the canvas. If not, it shows a warning message. If an image exists, it calculates the center position of the image using the canvas bbox coordinates, creates the watermark text at the center with the current font settings, and binds the <B1-Motion> event to allow users to drag the text anywhere on the image using their mouse.

* **reposition_watermark_after_resize()**: This method called after image zooming to reposition the watermark text. If the user is in alignment mode, it calls on_alignment_selected() to apply the selected alignment. If the user is in free mode (dragged the text), it calculates the new position based on the saved relative position values (watermark_rel_x and watermark_rel_y) to maintain the same position on the image.

* **on_alignment_selected()**: Handles the alignment selection from the combobox. It first checks if an image and watermark text exist. If not, it shows a warning. If they exist, it calculates the new position based on the selected alignment option (Center, Top-Left, Top-Right, Bottom-Left, Bottom-Right, Top-Center Edge, Bottom-Center Edge, Left-Center Edge, Right-Center Edge) and moves the watermark text to that position using coords().

* **update_font_style()**: Applies font styling (bold, italic, underline) based on the selected radiobutton. If "reset" is selected, it sets the style back to normal. It gets the current font properties, updates the style, and applies it to the watermark text using itemconfig().

* **make_text_bold()**: Handles the Ctrl+B keyboard shortcut. Toggles the text weight between bold and normal while preserving italic and underline styles if they are active.

* **make_text_italic()**: Handles the Ctrl+I keyboard shortcut. Toggles the text slant between italic and roman while preserving bold and underline styles.

* **make_text_underline()**: Handles the Ctrl+U keyboard shortcut. Toggles underline on and off while preserving bold and italic styles.

* **search_font_design()**: This method Filters the font families list based on the user's search input. As the user types in the search box, it checks each font name against the search term using lower() for case-insensitive matching. When matches are found, it hides other widgets and displays the matching fonts in the listbox.

* **display_matched_font_design()**: Clears the listbox, inserts all matched font names, and adjusts the listbox height based on the number of matches. Binds the <<ListboxSelect>> event to apply_font_design().

* **apply_font_design()**: Gets the selected font from the listbox, inserts it into the search box, collapses the listbox, and applies the selected font to the watermark text using itemconfig()

* **search_font_color()**: This method Filters the watermark colors list based on the user's search input. As the user types, it checks each color name against the search term and displays matching colors in the listbox while hiding other widgets.

* **display_matched_font_colors()**: Clears the listbox, inserts matching colors, adjusts the listbox height, and binds the <<ListboxSelect>> event to `apply_font_color()`.

* **apply_font_color()**: This method Gets the selected color from the listbox, inserts it into the search box, collapses the listbox, and applies the selected color to the watermark text using itemconfig(fill=color).

* **increase_font_size()**: Updates the font size based on the scale widget value. Gets the current font properties, applies the new size while preserving the current style, and calls reposition_watermark_after_resize() to maintain the text position.

* **rotate_watermark_text()**: Gets the rotation value from the spinbox and applies it to the watermark text using itemconfig(angle=value), allowing the text to be rotated up to 360 degrees.

* **collect_preset_data()**: Collects all current watermark settings including text, font properties, color, rotation angle, and position coordinates. If the user is in free mode, it uses the relative position values. If in alignment mode, it uses the aligned coordinates. It then asks the user for a preset name and calls `save_preset_data()`.

* **save_preset_data()**: Reads the existing preset.json file or creates a new one if it doesn't exist. Checks if the preset name already exists and shows a warning if it does. If the name is unique, it adds the new preset data and saves it back to the JSON file.

* **add_preset_name_in_combobox()**: Reads the preset.json file, extracts all preset names, and updates the combobox values so users can see and select saved presets.

* **apply_preset_style()**: Gets the selected preset name from the combobox, reads the preset data from the JSON file, and applies all the saved settings to the current image including watermark text, font properties, color, rotation angle, and position coordinates. It also calculates the relative position for the new image size.

* **get_new_image_text_coordinates()**: This method Calculates new x and y coordinates for the watermark based on the current image size. It uses the saved ratio values from the preset to maintain the same relative position on images of different sizes.

* **get_font_path()**: Searches through all installed fonts on the system using font_manager to find the actual .ttf file path for a given font family, weight, and slant. This is needed for saving images because Pillow requires a font file path.

* **save_watermarked_image()**: Opens a file dialog for the user to choose the save location and format (PNG or JPEG). It creates a copy of the original image, gets the watermark text, position, font properties, color, and rotation angle. It finds the actual font file using get_font_path(), creates a transparent watermark layer, draws the text with proper styling and underline if enabled, rotates the watermark if needed, and composites it onto the original image. Finally, it saves the image and shows a success message.

* **delete_image()**:  Clears everything from the image canvas using delete("all"), removing the image and watermark text.

* **open_file_explorer()**: Opens a file dialog for the user to select an image file. It filters for common image formats (jpg, jpeg, png, bmp, gif). If a file is selected, it calls `display_image()`.

* **display_image()**: Opens the selected image using Pillow, stores the original dimensions, creates a PhotoImage for display on the canvas, and places it at the center of the image canvas. It also binds the <MouseWheel> event to `resize_image()` for zoom functionality.

* **resize_image()**: Handles mouse wheel events to zoom in and out. It increases the zoom scale on scroll up and decreases it on scroll down, with limits between 0.1 and 5.0. It resizes the image using Pillow's resize() method, updates the displayed image on the canvas, and calls reposition_watermark_after_resize() to maintain the watermark position.

### data.py

* **text_align_options**: A list containing all available alignment options for the watermark text including center positions, corners, and edge positions.

* **watermark_colors**: A comprehensive list of color names including basic colors, light variations, dark variations, and shades that users can choose for their watermark text.

### preset.json

* Stores saved presets with details including watermark text, font properties (family, size, weight, slant, underline), font color, rotation angle, and position coordinates relative to the original image. This allows users to save their favorite watermark styles and apply them quickly to new images.


## Project Highlights

* **Tkinter GUI**: Built a complete desktop application with a professional interface and custom styling.
* **Image Processing with Pillow**: Used Pillow to open, display, edit, and save images with watermarks.
* **Real-Time Text Styling**: Applied font family, size, color, bold, italic, underline, and rotation in real-time.
* **Drag-and-Drop Watermark Positioning**: Users can drag the watermark anywhere on the image using mouse.
* **Alignment Presets**: Predefined alignment options (Center, Top-Left, Bottom-Right, etc.) for quick positioning.
* **Font Family and Color Search**: Real-time search and filter for font families and colors.
* **Keyboard Shortcuts**: Ctrl+B for bold, Ctrl+I for italic, Ctrl+U for underline.
* **Preset Management**: Save and load custom watermark settings for future use.
* **Image Zoom**: Mouse wheel zoom in and out while maintaining watermark position.
