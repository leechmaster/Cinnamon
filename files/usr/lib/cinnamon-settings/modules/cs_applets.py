#!/usr/bin/env python
import sys
from ExtensionCore import ExtensionSidePage

class Module:
    def __init__(self, content_box):
        keywords = _("applet")
        self.name = "applets"       
        self.comment = _("Manage Cinnamon applets")
        sidePage = AppletsViewSidePage(_("Applets"), "cs-applets", keywords, content_box, "applet", self)
        self.sidePage = sidePage
        self.category = "prefs"

    def on_module_selected(self, switch_container):
        if not self.loaded:
            print "Loading Applets module"
            self.sidePage.load(switch_container)
        self.sidePage.stack_switcher.show()

    def _setParentRef(self, window):
        self.sidePage.window = window

class AppletsViewSidePage (ExtensionSidePage):
    def __init__(self, name, icon, keywords, content_box, collection_type, module):
        self.RemoveString = _("You can remove specific instances in panel edit mode via the context menu.")
        ExtensionSidePage.__init__(self, name, icon, keywords, content_box, collection_type, module)

    def toSettingString(self, uuid, instanceId):
        panelno = "panel1"
        if len(sys.argv) > 2:
            if sys.argv[1] == "applets" and sys.argv[2][0:5] == "panel":
                panelno = sys.argv[2]
        return (panelno + ":right:0:%s:%d") % (uuid, instanceId)

    def fromSettingString(self, string):
        panel, side, position, uuid, instanceId = string.split(":")
        return uuid

    def getAdditionalPage(self):
        return None
