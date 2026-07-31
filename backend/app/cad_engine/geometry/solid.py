
class SolidGenerator:

    name="solid_generator"

    def run(self, geometry):

        return {
            "solid_model": True,
            "format":[
                "STEP",
                "STL"
            ],
            "geometry": geometry
        }
