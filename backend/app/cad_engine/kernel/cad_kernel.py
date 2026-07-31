class CADKernel:


    def box(
        self,
        width,
        height,
        depth
    ):

        volume = width * height * depth

        return {

            "type": "box",

            "dimensions": {

                "width": width,
                "height": height,
                "depth": depth

            },

            "volume_mm3": volume

        }



    def cylinder(
        self,
        radius,
        height
    ):

        volume = 3.14159 * radius * radius * height

        return {

            "type": "cylinder",

            "dimensions": {

                "radius": radius,
                "height": height

            },

            "volume_mm3": round(
                volume,
                2
            )

        }



    def sphere(
        self,
        radius
    ):

        volume = (
            4 / 3
        ) * 3.14159 * radius ** 3


        return {

            "type": "sphere",

            "dimensions": {

                "radius": radius

            },

            "volume_mm3": round(
                volume,
                2
            )

        }



    def estimate_mass(
        self,
        volume_mm3,
        density
    ):

        volume_cm3 = volume_mm3 / 1000

        return round(
            volume_cm3 * density,
            2
        )
