# packages import
import gui,json
# creating variable for application confing using app_confing.json
app_config=json.load(open("app_settings.json"))
# starting application
gui.gui.config(background=("white" if app_config["theme"]=="white" else "#323232"))
gui.update_gui_structure(gui.app_gui_structures["presentation"],gui.gui,app_config)
gui.gui.mainloop()