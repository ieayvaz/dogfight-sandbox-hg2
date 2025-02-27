from Machines import Radar
import harfang as hg

class RADARTYPE1(Radar):
    model_name = "RADARTYPE1"
    instance_scene_name = "machines/aircraft/aircraft_blend.scn"

    def __init__(self, name, scene, scene_physics, pipeline_ressource: hg.PipelineResources, nationality, start_pos, start_heading):
        parameters = {
            "max_range" : 2000,
            "azimuth_fov" : 360,
            "elevation_fov" : 360,
            "max_track" : 5,
            "scan_speed" : 360,
        }
        super().__init__(name, self.model_name, scene, scene_physics, pipeline_ressource, self.instance_scene_name,
                        nationality, start_pos, start_heading, **parameters)