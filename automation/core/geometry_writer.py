class GeometryWriter:

    def write(self, context, geometry):

        if "engineering_context" in context:

            context["engineering_context"].update(
                "geometry",
                geometry
            )

        return context
