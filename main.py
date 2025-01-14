import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler
from entity import Entity
from engine import Engine
from tiles.game_map import GameMap
def main():
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # 이벤트 헨들러 추가
    event_handler = EventHandler()
    # 엔티티 추가
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}
    
    game_map = GameMap(map_width, map_height)

    # 엔진 추가
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)
    
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)
            events = tcod.event.wait()
            engine.handle_events(events)

if __name__ == "__main__":
    main()