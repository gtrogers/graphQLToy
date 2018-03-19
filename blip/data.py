_blips = {}


def setup():
    from .schema import Quadrant, Position, Blip, Ring
    blips = []
    
    blips.append(Blip(
        id = "0",
        name = 'Spurious code examples',
        info = 'hello',
        position = Position(
            quadrant = Quadrant.TECHNIQUES,
            distance = 5,
            ring = Ring.ADOPT),
        new = True
    ))

    blips.append(Blip(
        id = "1",
        name = 'Tautology and repetition',
        info = 'some info goes here, also explain the thing',
        position = Position(
            quadrant = Quadrant.LANGUAGES_AND_FRAMEWORKS,
            distance = 3,
            ring = Ring.HOLD),
        new = False
    ))

    for b in blips:
        _blips[b.id] = b


def get_blips(quadrant=None):
    if quadrant is not None:
        return [b for b in _blips.values() if b.position.quadrant == quadrant]
    else:
        return _blips.values()


def get_blip(id):
    return _blips.get(id)

