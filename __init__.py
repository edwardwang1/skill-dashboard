# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import os
import Pyro4

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class DashboardSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(DashboardSkill, self).__init__(name="Dashboard")
        

    @intent_handler(IntentBuilder("").require("Open").require("Dashboard"))
    def handle_dashboard_control_intent(self, message):
        with open("uri.txt", 'r') as myfile:
            uri = myfile.read()
        if uri.strip():
            pass
            #self.speak_dialog("dashboard.already.active")
        else:
            #self.speak_dialog("opening.dashboard")
            os.system('lxterminal -e /usr/bin/python3 ~/Desktop/RPiDashboard/main.py')
            #os.system('/usr/bin/python3 ~/Desktop/RPiDashboard/main.py')

    @intent_handler(IntentBuilder("").require("Visibility").require("Widget"))
    def handle_show_hide_intent(self, message):
        with open("uri.txt", 'r') as myfile:
            uri = myfile.read()
        try:
            app = Pyro4.Proxy(uri)
            if message.data["Visibility"] == "show":
                vis = 1
            else:
                vis = 0
            if message.data["Widget"] == "all":
                app.showHideAllWidgets(vis)
            elif message.data["Widget"] == "calendar":
                app.showHideCalendar(vis)
            elif message.data["Widget"] == "clock":
                app.showHideClock(vis)
            elif message.data["Widget"] == "weather":
                app.showHideWeather(vis)
            elif message.data["Widget"] == "command":
                app.showHideCommandDisplay(vis)
            elif message.data["Widget"] == "notes":
                app.showHideNotes(vis)
        except:
            print("Pyro could not create connection")
    
    @intent_handler(IntentBuilder("").require("Close").require("Dashboard"))        
    def close_dashboard_intent(self, message):
        with open("uri.txt", 'r') as myfile:
            uri = myfile.read()
        app = Pyro4.Proxy(uri)
        app.shutdown()
        app._pyroRelease()

    @intent_handler(IntentBuilder("").require("Reset").require("Dashboard"))        
    def reset_intent(self, message):
        text_file = open("uri.txt", "w")
        text_file.write("")
        text_file.close()
    
    @intent_handler(IntentBuilder("").require("Note").require("Modify"))        
    def modify_note_intent(self, message):
        if message.data["Modify"] == "add":
            with open("uri.txt", 'r') as myfile:
                uri = myfile.read()
            try:
                utterance = message.data.get('utterance')
                app = Pyro4.Proxy(uri)
                app.addNote(utterance)
            except:
                print("Pyro could not create connection")
        else:
            with open("uri.txt", 'r') as myfile:
                uri = myfile.read()
            try:
                utterance = message.data.get('utterance')
                app = Pyro4.Proxy(uri)
                app.removeNote(utterance)
            except:
                print("Pyro could not create connection")
        
        
        
    @intent_handler(IntentBuilder("").require("Clear").require("Note"))        
    def clear_note_intent(self, message):
        with open("uri.txt", 'r') as myfile:
            uri = myfile.read()
        try:
            app = Pyro4.Proxy(uri)
            app.clearNote()
        except:
            print("Pyro could not create connection")

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return DashboardSkill()
