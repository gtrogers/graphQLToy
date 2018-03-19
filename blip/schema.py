import graphene

from data import get_blips, setup

class Quadrant(graphene.Enum):
    TECHNIQUES = 0
    TOOLS = 1
    PLATFORMS = 2
    LANGUAGES_AND_FRAMEWORKS = 3


class Position(graphene.ObjectType):
    quadrant = graphene.Field(Quadrant)
    distance = graphene.Int()


class Blip(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    info = graphene.String()
    position = graphene.Field(Position)
    new = graphene.Boolean()


class Query(graphene.ObjectType):
    blips = graphene.List(Blip)

    def resolve_blips(self, info):
        return get_blips()

schema = graphene.Schema(query=Query)

if __name__ == '__main__':
    setup()
    result = schema.execute('query blips{ blips { name, info, position { quadrant } } }')
    print(result.data)

