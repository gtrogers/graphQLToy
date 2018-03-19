import graphene

from .data import get_blips, get_blip, setup

class Quadrant(graphene.Enum):
    TECHNIQUES = 0
    TOOLS = 1
    PLATFORMS = 2
    LANGUAGES_AND_FRAMEWORKS = 3


class Ring(graphene.Enum):
    ADOPT = 0
    TRIAL = 1
    ASSESS = 2
    HOLD = 3


class Position(graphene.ObjectType):
    quadrant = graphene.Field(Quadrant)
    ring = graphene.Field(Ring)
    distance = graphene.Int()
    blips = graphene.List(lambda: Blip)

    def resolve_blips(root, *args, **kwargs):
        blips = get_blips(root.quadrant, root.ring)
        return sorted(blips, key=lambda b: b.position.distance)

    def resolve_ring(root, *args, **kwargs):
        return root.ring.value

    def resolve_quadrant(root, *args, **kwargs):
        return root.quadrant.value


class Blip(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    info = graphene.String()
    position = graphene.Field(Position)
    new = graphene.Boolean()


class Query(graphene.ObjectType):
    """ this is the entry point for the graphQL API"""
    blips = graphene.List(Blip, quadrant=Quadrant(), ring=Ring())
    blip = graphene.Field(Blip, id=graphene.ID(required=True))

    def resolve_blips(self, info, quadrant=None, ring=None):
        return get_blips(quadrant, ring)

    def resolve_blip(self, info, id):
        return get_blip(id)

schema = graphene.Schema(query=Query)
