# LightsCtrl_HA
Script to turn on all lights with HA

HA entiys must be defined into "lights.json" file

EXAMPLE:

{"hlights":[
  { "name":"LIGHT_BEDROOM", "entity_id":"entity_example_ha.1234" },
  { "name":"LIGHT_WARDROBE", "entity_id":"entity2_example_ha.45678" }
]}

The script print the output of POSTS request

REF:
https://developers.home-assistant.io/docs/api/rest/