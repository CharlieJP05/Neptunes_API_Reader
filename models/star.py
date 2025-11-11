class Star:
    def __init__(self, data):
        self.id = data['uid']
        self.visible = bool(data['v'])

        # TODO: Set to player object instead of PUID
        self.owning_player = data['puid']

        self.name = data['n']
        self.x = data['x']
        self.y = data['y']

        self.ships_stationed = data['st']
        self.experience = data['exp']
        self.resources = data['r']

        self.economy = data['e']
        self.industry = data['i']
        self.science = data['s']

        self.ship_build_progress = data['yard']


        #TODO: nr (resources based off terraforming?), ga

