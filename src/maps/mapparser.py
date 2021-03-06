import json
import urllib.request

import maps.map
import maps.territory

class MapParser():
    @staticmethod
    def fromURL(url):
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        return MapParser.fromJSON(response.read().decode('utf-8'))

    @staticmethod
    def fromJSON(s):
        obj = json.loads(s)

        mapObj = maps.map.Map(obj['map_id'], obj['name'], obj['width'], obj['height'], obj['url'])

        for i, v in enumerate(obj['territories']):
            t = maps.territory.Territory(v['id'], v['name'], v['x'], v['y'])
            mapObj.addTerritory(t)

        for i, v in enumerate(obj['connections']):
            tFrom = mapObj.getTerritoryByID(v['from'])
            tTo = mapObj.getTerritoryByID(v['to'])
            tFrom.addConnection(tTo)

        return mapObj