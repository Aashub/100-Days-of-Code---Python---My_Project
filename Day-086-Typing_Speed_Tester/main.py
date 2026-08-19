from userinterface import UserInterface

ui = UserInterface()
ui.add_typing_test_screen()
ui.display_typing_text()
ui.all_widget_button()
ui.bind("<KeyRelease>", ui.check_retrieved_text)

ui.mainloop()


