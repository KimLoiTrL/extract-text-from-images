import kivy
#kivy.require('1.9.1')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from test2 import func
import time
Window.size = (680, 960)
class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class GalleryWindow(Screen):
    pass
class CameraWindow(Screen):
    pass
    path = StringProperty()
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        self.path = "IMG_"+str(timestr)+".png"
        camera.export_to_png(self.path)
        print("captured")
class ConfirmWindow(Screen):
    pass
class ResultWindow(Screen):
    pass
class WindowManager(ScreenManager):
    image_source = StringProperty()
    def selected(self,filename):
        try:
            if len(filename[0])==1:
                self.image_source = filename
            else:
                self.image_source = filename[0]
        except:
            pass
    result = StringProperty()
    def spliting(self,image):
        try:
            self.result = func(image)
        except:
            pass
class DemoApp(App):
    pass

if __name__ == '__main__':
    DemoApp().run()