from scene import World
import time


if __name__ == "__main__":
    world = World()
    start = time.ctime()
    image = world.render_scene_single()
    image.save('1tune.jpg')
    end = time.ctime()
    print(start, end)
