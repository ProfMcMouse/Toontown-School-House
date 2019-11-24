from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE13a',
        'wantDoors': 1},
 1001: {'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None},
 0: {'type': 'zone',
     'name': 'UberZone',
     'comment': '',
     'parentEntId': 0,
     'scale': 1,
     'description': '',
     'visibility': []},
 100001: {'type': 'goon',
          'name': '',
          'comment': '',
          'parentEntId': 100000,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': .5,
          'attackRadius': 5,
          'crushCellId': None,
          'goonType': 'pg',
          'gridId': None,
          'hFov': 100,
          'strength': 5,
          'velocity': 4},
 100002: {'type': 'nodepath',
          'name': 'pathmasta1',
          'comment': '',
          'parentEntId': 100000,
          'pos': Point3(32.0525, 0.204516, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100003: {'type': 'nodepath',
          'name': 'copy of pathmasta1',
          'comment': '',
          'parentEntId': 100000,
          'pos': Point3(-28.2492, 5.56589, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100004: {'type': 'nodepath',
          'name': 'copy of pathmasta1',
          'comment': '',
          'parentEntId': 100000,
          'pos': Point3(-10.8179, 14.6481, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100005: {'type': 'nodepath',
          'name': 'pathmastachild',
          'comment': '',
          'parentEntId': 100000,
          'pos': Point3(-59.4987, 29.1448, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1)},
 100000: {'type': 'pathMaster',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-17.2957, -37.5269, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'pathIndex': 0,
          'pathScale': 1.0,
          'pathTarget0': 100002,
          'pathTarget1': 100003,
          'pathTarget2': 100004,
          'pathTarget3': 100005,
          'pathTarget4': 0,
          'pathTarget5': 0,
          'pathTarget6': 0,
          'pathTarget7': 0}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}
