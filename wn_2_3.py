#pylint:disable=W0613
#pylint:disable=E0401
#pylint:disable=E0611
#pylint:disable=E1101
#pylint:disable=W0311
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Line
from kivy.uix.label import Label
#from kivy import *
import numpy as np
from kivy.properties import NumericProperty


class BoxLayoutExample(BoxLayout):
       
        def __init__(self, **kwargs):
        	super().__init__(**kwargs)
        	self.orientation='vertical'
        	d = DrawInput()
        	d.bind(numx=self.update_label)
        	
        	self.label = Label(text=f"{d.numx} ", size_hint= (1, 0.2), font_size= '80dp')
        	self.add_widget(self.label)
        	self.add_widget(d)
        	
        	HB= BoxLayout(orientation='horizontal')
        	self.add_widget(HB)

        	b1=Button(text='Submit', 
        			size_hint=(0.7, 0.2), 
        			font_size='30dp')
        	HB.add_widget(b1)
        	b1.bind(on_release=d.submit)
        	
        	b2=Button(text='Clear',
        			 size_hint=(0.3, 0.2), 
        			 font_size='20dp')
        	HB.add_widget(b2)
        	b2.bind(on_release=d.wipe)
        	
        def update_label(self, instance, value):
        	self.label.text = str(value)
        	
        
class DrawInput(Widget):
    numx = NumericProperty(9)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gen_num()
        print(f'initial x={self.numx}')
    
    def gen_num(self):
    	self.numx= np.random.randint(0,10)
    	self.rser = np.random.randint(
    										10000, 999999)
    	
    def wipe(self, instance):
    	self.canvas.clear()
    	
    def on_touch_down(self, touch):
    	with self.canvas:
    		touch.ud["line"]= Line(points=(touch.x, touch.y), width=10)
    		
    def on_touch_move(self, touch):
    	touch.ud["line"].points += (touch.x, touch.y)
    	
    def on_touch_up(self, touch):
        print(f"up x pre ={self.numx}")
        
    
    def submit(self, instance):
        self.export_to_png(f'images/{self.numx}/no_{self.numx}_s{self.rser}.png', dpi=50)
        self.canvas.clear()
        self.gen_num()
        print(f"up x post ={self.numx}")
        

		
class MyFirstApp(App):
    def build(self): 
        return BoxLayoutExample()
		
if __name__ == "__main__":
    MyFirstApp().run()
	