
_blips = {}

def setup():
    from schema import Quadrant, Position, Blip
    blip1 = Blip(
        id = 0,
        name = 'Spurious code examples',
        info = 'hello',
        position = Position(quadrant = 0, distance = 5),
        new = True
    )

    _blips[blip1.id] = blip1

def get_blips():
    return _blips.values()

