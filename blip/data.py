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


def _filter_by_quadrant(blips, quadrant):
  return [b for b in blips if b.position.quadrant == quadrant]


def _filter_by_ring(blips, ring):
  return [b for b in blips if b.position.ring == ring]


def get_blips(quadrant=None, ring=None):
    if quadrant is not None and ring is not None:
        return _filter_by_quadrant(_filter_by_ring(_blips.values(), ring), quadrant)
    if quadrant is not None:
        return _filter_by_quadrant(_blips.values(), quadrant)
    if ring is not None:
        return _filter_by_ring(_blips.values(), ring)
    else:
        return _blips.values()


def get_blip(id):
    return _blips.get(id)

