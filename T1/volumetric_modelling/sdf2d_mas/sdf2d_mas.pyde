def setup():
    size(800,450)
    
    global pic
    w,h = 400,225
    pic = createImage(w,h,RGB)
    pic.loadPixels()
    
    # circle 1 params
    cx = 200
    cy = 100
    rd = 75
    
    # circle 2 params
    cx2, cy2 = 300,150
    rd2 = 100
    
    # rectangle parameters
    rx,ry,ra,rb = 120,150,180,130
    
    for x in range(w):
        for y in range(h):
            # distance functions for circles
            d = sqrt((x-cx)**2 + (y-cy)**2) - rd
            d2 = sqrt((x-cx2)**2 + (y-cy2)**2) - rd2
            
            # distance function for rectangle
            d3 = max(abs(x-rx)-ra/2.0, abs(y-ry)-rb/2.0)
                        
            # boolean union
            u = min(d,d2)
            # boolean intersection
            #u = max(d,d2)
            # boolean subtraction
            u = max(u,-d3)
            
            # shell of thickness t
            t = 65.0
            u = abs(u)-t/2
            #u = max(u,-d3)
            
            # microstructure = sin(x/8.0)*cos(y/8.0)*10
            # u = max(u,microstructure)
            
            # image representation    
            # greenish
            col = color(0,u*2,0)
            if u<0:
                # reddish
                col = color(u*-2,0,0)
            
            # perimeter
            if abs(u)<1:
                col = color(255)
                
            # binary coloring
            # col = color(255)
            # if u<0:
            #     col = color(0)
            
            ix = y*w+x
            pic.pixels[ix] = col
    
def draw():
    image(pic,0,0,width,height)
