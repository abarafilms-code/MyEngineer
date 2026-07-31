from backend.app.cad_engine.kernel.cad_kernel import CADKernel


class CADKernelAgent:

    name = "cad_kernel_agent"


    def run(self, context):

        print("\nCAD Kernel Agent:")


        kernel = CADKernel()


        model = kernel.box(
            100,
            50,
            20
        )


        validation = kernel.validate(
            model
        )


        context["cad_kernel"] = {

            "model": model,

            "valid":

                validation

        }


        print(
            "Solid generated:",
            model
        )


        return context
