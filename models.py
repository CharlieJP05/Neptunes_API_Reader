from copy import deepcopy


class Star:
    _stars_by_id = {}

    @classmethod
    def register(cls, star):
        cls._stars_by_id[star.id] = star

    @classmethod
    def get(cls, star_id):
        return cls._stars_by_id.get(star_id)

    @classmethod
    def get_all(cls):
        return deepcopy(cls._stars_by_id)

    def __init__(self, data, register=True):
        self.id = data['uid']
        self.visible = bool(data['v'])

        # TODO: Set to player object instead of PUID
        self.owning_player = data['puid']

        self.name = data['n']
        self.x = data['x']
        self.y = data['y']

        self.ships_stationed = data.get('st')
        self.experience = data.get('exp')
        self.resources = data.get('r')

        self.economy = data.get('s')
        self.industry = data.get('i')
        self.science = data.get('s')

        self.ship_build_progress = data.get('yard')

        #TODO: nr (resources based off terraforming?), ga

        if register:
            self.__class__.register(self)

class Player:
    _players_by_id = {}

    @classmethod
    def register(cls, player):
        cls._players_by_id[player.id] = player

    @classmethod
    def get(cls, player_id):
        return cls._players_by_id.get(player_id)

    @classmethod
    def get_all(cls):
        return deepcopy(cls._players_by_id)

    def __init__(self, data, register=True):
        self.id = data['']
        self.name = data['alias']
        self.avatar = data['avatar']
        self.colour = data['color']
        self.shape = data['shape']
        self.home = Star.get(data['home']) #TODO: Coupling?

        self.total_stars = data['totalStars']
        self.total_fleets = data['totalFleets']
        self.total_ships = data['totalStrength']
        self.total_economy = data['totalEconomy']
        self.total_industry = data['totalIndustry']
        self.total_science = data['totalScience']

        self.conceded = bool(data['conceded'])
        self.ai = bool(data['ai'])
        self.regard = data['regard']
        self.tech = data['tech'] #TODO: Tech class?

        #TODO: race, acceptedVassal, offersOfFealty, vassals, karmaToGive, ready, missedTurns

        if register:
            self.__class__.register(self)