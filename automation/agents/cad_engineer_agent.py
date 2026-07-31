class CADEngineerAgent:

    name = "cad_engineer_agent"

    def run(self, context):

        print("\nCAD Engineer Agent:")

        files = context.get(
            "analysis",
            {}
        ).get(
            "files",
            []
        )

        cad_files = []

        for file in files:
            if "cad" in file.lower():
                cad_files.append(file)

        analysis = {
            "cad_files": cad_files,
            "issues": [],
            "recommendations": []
        }

        if cad_files:
            analysis["recommendations"].extend([
                "Check geometry constraints",
                "Validate parametric dimensions",
                "Improve manufacturing compatibility"
            ])

        else:
            analysis["recommendations"].append(
                "Create CAD architecture layer"
            )

        context["cad_analysis"] = analysis

        print(
            "CAD files found:",
            len(cad_files)
        )

        return context
