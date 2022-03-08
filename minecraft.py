from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController




app = Ursina()

punch_sound = Audio('assets_punch_sound.wav', loop = False, autoplay = False)
window.fps_counter.enabled = False
window.exit_button.visible  = False
window.fullscreen = True
window.title = 'Just craft'


gif = 'Just-Craft.gif'
a = Animation(gif, parent=camera.ui)
a.scale /= 5 # adjust right size to your needs
a.position = (0.01,0.0999) # lower right of the screen
txt = Text(text=("in python"),scale = 2,color = color.red,width = 3)


def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.pasive()
    



class Voxel(Button):
    def __init__(self,position = (0,0,0)):
       super().__init__(
           parent=scene,
           position = position,
           model = "cube",
           origin_y = 0.5,
           texture= 'brick',
           color =  color.color(0,0,random.uniform(1,0.9)),
           highlight_color = color.lime,
           
           
        ) 
       self.texture_choice = 0
       self.textures = ["download (4).jfif", "hi.jpg", "hwllo.jfif","photo-1588402912586-70706e7791d8.jfif","hi.png",'arrow_down',
'arrow_right',

'brick',

'circle',
'circle_outlined',
'cobblestone',
'cursor',
'file_icon',
'folder',
'grass',
'heightmap_1',
'horizontal_gradient',
'noise',
'radial_gradient',
'reflection_map_3',
'shore',
'sky_default',
'sky_sunset',
'ursina_logo',
'ursina_wink_0000',
'ursina_wink_0001',
'vertical_gradient',
'white_cube', ]


    def input(self,key):
        if self.hovered:
            
           if key == 'left mouse down':
              punch_sound.play()
              voxel = Voxel(position = self.position + mouse.normal)
           if key == 'right mouse down':
               punch_sound.play()
               destroy(self)
           if key == "c":
               self.texture_choice += 1
               self.texture_choice %= len(self.textures)
               self.texture = self.textures[self.texture_choice]
               

class Sky(Entity):




    def __init__(self):
        super(). __init__(
             parent = scene,
             model ="sphere",
             texture = "skybox.png",    
             scale = 150,
           
             double_sided =True)


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "cube",
            texture = "brick",
            scale = 0.2,
            rotation =  Vec3(150,-10,0),
            position= Vec2(0.4,-0.4)
            
        )
    def active(self):
        
        self.position = Vec2(0.4,-0.3)

    def pasive(self):
        self.position= Vec2(0.4,-0.4)




for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))
         


player = FirstPersonController()
sky = Sky() 
hand = Hand()
app.run()
