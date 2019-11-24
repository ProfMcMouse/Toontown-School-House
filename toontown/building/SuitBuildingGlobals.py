from ElevatorConstants import *
SuitBuildingInfo = (((1, 1),
  (1, 3),
  (4, 4),
  (8, 10),
  (1,)),
 ((1, 2),
  (2, 4),
  (5, 5),
  (8, 10),
  (1, 1.2)),
 ((1, 3),
  (3, 5),
  (6, 6),
  (8, 10),
  (1, 1.3, 1.6)),
 ((2, 3),
  (4, 6),
  (7, 7),
  (8, 10),
  (1, 1.4, 1.8)),
 ((2, 4),
  (5, 7),
  (8, 8),
  (8, 10),
  (1,
   1.6,
   1.8,
   2)),
 ((3, 4),
  (6, 8),
  (9, 9),
  (10, 12),
  (1,
   1.6,
   2,
   2.4)),
 ((3, 5),
  (7, 9),
  (10, 10),
  (10, 14),
  (1,
   1.6,
   1.8,
   2.2,
   2.4)),
 ((4, 5),
  (8, 10),
  (11, 11),
  (12, 16),
  (1,
   1.8,
   2.4,
   3,
   3.2)),
 ((5, 5),
  (9, 11),
  (12, 12),
  (14, 20),
  (1.4,
   1.8,
   2.6,
   3.4,
   4)),
 ((1, 1), #vp round 1
  (1, 12),
  (12, 12),
  (67, 67),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (8, 12), #vp round 2
  (12, 12),
  (100, 100),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1), #cfo
  (1, 12),
  (12, 12),
  (100, 100),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1), # what is this?
  (8, 12),
  (12, 12),
  (150, 150),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1), #cj (1,1) no idea what this tuple does
  (5, 12), #cog levels
  (12, 12), #random range?
  (275, 275), #cog amount
  (1, #all 1s #possible on off switch for above things? no clue
   1,
   1,
   1,
   1)),
 ((1, 1), #ceo
  (9, 12),
  (12, 12),
  (206, 206),
  (1,
   1,
   1,
   1,
   1),
  (1,)), #v2.0 revives
 ((1, 1), #vp storm round 1
  (1, 5),
  (5, 5),
  (33, 33),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),  #vp storm round 2
  (4, 5),
  (5, 5),
  (50, 50),
  (1,
   1,
   1,
   1,
   1)))
SUIT_BLDG_INFO_FLOORS = 0
SUIT_BLDG_INFO_SUIT_LVLS = 1
SUIT_BLDG_INFO_BOSS_LVLS = 2
SUIT_BLDG_INFO_LVL_POOL = 3
SUIT_BLDG_INFO_LVL_POOL_MULTS = 4
SUIT_BLDG_INFO_REVIVES = 5
VICTORY_RUN_TIME = ElevatorData[ELEVATOR_NORMAL]['openTime'] + TOON_VICTORY_EXIT_TIME
TO_TOON_BLDG_TIME = 8
VICTORY_SEQUENCE_TIME = VICTORY_RUN_TIME + TO_TOON_BLDG_TIME
CLEAR_OUT_TOON_BLDG_TIME = 4
TO_SUIT_BLDG_TIME = 8
