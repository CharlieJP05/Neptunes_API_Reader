class Star:
    def __init__(self, data):
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
        self.industry = data('i')
        self.science = data('s')

        self.ship_build_progress = data.get('yard')


        #TODO: nr (resources based off terraforming?), ga

