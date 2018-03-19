_blips = {}


def setup():
    from .schema import Quadrant, Position, Blip, Ring

    def _store_blip(name, info, position, new):
        id = str(len(_blips.values()))
        blip = Blip(
            id = id,
            name = name,
            info = info,
            position = position,
            new = new
        )
        _blips[id] = blip
        blips = []
    
    _store_blip('Spurious code examples',
                'hello',
                Position(
                  quadrant = Quadrant.TECHNIQUES,
                  distance = 5,
                  ring = Ring.ADOPT),
                True)

    _store_blip('Friday pub',
                'Beverage-Ops as a practice not a role',
                Position(
                  quadrant = Quadrant.TECHNIQUES,
                  ring = Ring.ADOPT,
                  distance = 3),
                  True)

    _store_blip('Tautology and repetition',
                'some info goes here, also explain the thing',
                Position(
                  quadrant = Quadrant.LANGUAGES_AND_FRAMEWORKS,
                  distance = 3,
                  ring = Ring.HOLD),
                False)

    _store_blip('Enterprise scale fizzbuzz',
                'Fizz... ESB... buzz... ESB... fizz... ESB... buzz...',
                Position(
                  quadrant = Quadrant.PLATFORMS,
                  ring = Ring.ASSESS,
                  distance = 9),
                True)

    _store_blip('VR IDE',
                '360 Degree wrap around coding environments',
                Position(
                  quadrant = Quadrant.TOOLS,
                  ring = Ring.ASSESS,
                  distance = 1),
                False)

    _store_blip('USB Based Deployment Pipelines',
                'Switch to SD cards for massive storage gains',
                Position(
                  quadrant = Quadrant.TECHNIQUES,
                  ring = Ring.HOLD,
                  distance = 9),
                True)

    _store_blip('Subtly trolling doppler with fake tech radar blips',
                'Needs more real world evidence',
                Position(
                  quadrant = Quadrant.LANGUAGES_AND_FRAMEWORKS,
                  ring = Ring.TRIAL,
                  distance = 2),
                True)


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

