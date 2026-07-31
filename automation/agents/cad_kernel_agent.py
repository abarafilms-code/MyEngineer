from backend.app.cad_engine.kernel.cad_kernel import CADKernel


class CADKernelAgent:


    name = "cad_kernel_agent"



    def run(
        self,
        context
    ):

        kernel = CADKernel()


        solid = kernel.box(
            100,
            50,
            20
        )


        mass = kernel.estimate_mass(
            solid["volume_mm3"],
            1.27
        )


        solid["material_density"] = 1.27
        solid["estimated_mass_grams"] = mass


        context["cad_kernel"] = solid


        print(
            "CAD Kernel:"
        )

        print(
            solid
        )


        return context
