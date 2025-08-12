class VexDef:
    def __init__(self):
        self.vex_cat = 0
        self.vex_status = False
        self.vex_notes = ""
        self.vex_impact = 0.0

    def define_vex(self, vex_cat, vex_status, vex_notes, vex_impact):
        self.vex_cat = vex_cat
        self.vex_notes = vex_notes
        self.vex_impact = vex_impact
        self.vex_status = vex_status

    def print_vex(self, id):
        print(f" associated vex info for cve#:{id}")
        print(f" the vex category is:{self.vex_cat}")
        print(f" the exploitability status is: {self.vex_status}")
        print(f" the vex impact score is: {self.vex_impact}")
        print(f" here are some additional notes: {self.vex_notes}")


class CveDef(VexDef):
    def __init__(self):
        super().__init__()
        self.id = 0
        self.sev = 0
        self.desc = ""
        self.package = ""
        self.status = False

    def define_cve(self, id, sev, desc, package, status):
        self.id = id
        self.sev = sev
        self.desc = desc
        self.package = package
        if status is True:
            self.status = True
        self.add_vex(desc)

    def print_cve(self, id):
        print(f" cve info for cve#: {id}")
        print(f"severity = {self.sev} with status as {self.status}")
        print(f"package info: {self.package}")
        print(f"remediation status: {self.status}")
        print(" the associated vex info is below")
        super().print_vex(self.id)

    def add_vex(self, vex_notes):
        vex_cat = 0
        vex_status = False
        vex_impact = 0.0
        if 2 < self.sev < 4:
            vex_cat = 0
            vex_status = True
            vex_impact = 3.0
        elif self.sev > 4:
            vex_cat = 1
            vex_impact = 5.0
            vex_status = True
        else:
            vex_cat = 0
            vex_status = False
            vex_impact = 1.0
        super().define_vex(vex_cat, vex_status, vex_notes, vex_impact)

    def __del__(self):
        print("do nothing destructor")


if __name__ == "__main__":
    cid = 100
    sev = 6
    desc = "npe in keycloak client credentials grant handler"
    package = "keycloak 17.x"
    status = True
    cve_instance = CveDef()
    cve_instance.define_cve(cid, sev, desc, package, status)
    cve_instance.print_cve(cid)
    cve_instance = 10  # try to invoke the destructor as object has no refs now
    for _ in range(0, 10000):
        pass  # no-op statement
