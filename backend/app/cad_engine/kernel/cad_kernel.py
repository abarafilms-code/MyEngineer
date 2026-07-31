class CADKernel:


    def box(
        self,
        width,
        height,
        depth
    ):

        return {
            "type": "box",
            "width": width,
            "height": height,
            "depth": depth
        }


    def cylinder(
        self,
        radius,
        height
    ):

        return {
            "type": "cylinder",
            "radius": radius,
            "height": height
        }


    def validate(
        self,
        solid
    ):

        if not solid:
            return False

        return True
