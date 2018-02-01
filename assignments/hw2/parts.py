suppliers = set()
# (create-relation s(sno sname status city))
suppliers.add(("s1","Smith",20,"London"))
suppliers.add(("s2","Jones",10,"Paris"))
suppliers.add(("s3","Blake",30,"Paris"))
suppliers.add(("s4","Clark",20,"London"))
suppliers.add(("s5","Adams",30,"Athens"))

parts = set()
# (create-relation p(pno pname color weight city))
parts.add(("p1","Nut","Red",12,"London"))
parts.add(("p2","Bolt","Green",17,"Paris"))
parts.add(("p3","Screw","Blue",17,"Rome"))
parts.add(("p4","Screw","Red",14,"London"))
parts.add(("p5","Cam","Blue",12,"Paris"))
parts.add(("p6","Cog","Red",19,"London"))

projects = set()
# (create-relation j(jno jname city))
projects.add(("j1","Sorter","Paris"))
projects.add(("j2","Punch","Rome"))
projects.add(("j3","Reader","Athens"))
projects.add(("j4","Console","Athens"))
projects.add(("j5","Collator","London"))
projects.add(("j6","Terminal","Oslo"))
projects.add(("j7","Tape","London"))

spj = set()
# (create-relation spj(sno pno jno qty))
spj.add(("s1","p1","j1",200))
spj.add(("s1","p1","j4",700))
spj.add(("s2","p3","j1",400))
spj.add(("s2","p3","j2",200))
spj.add(("s2","p3","j3",200))
spj.add(("s2","p3","j4",500))
spj.add(("s2","p3","j5",600))
spj.add(("s2","p3","j6",400))
spj.add(("s2","p3","j7",800))
spj.add(("s2","p5","j2",100))
spj.add(("s3","p3","j1",200))
spj.add(("s3","p4","j2",500))
spj.add(("s4","p6","j3",300))
spj.add(("s4","p6","j7",300))
spj.add(("s5","p2","j2",200))
spj.add(("s5","p2","j4",100))
spj.add(("s5","p5","j5",500))
spj.add(("s5","p5","j7",100))
spj.add(("s5","p6","j2",200))
spj.add(("s5","p1","j4",100))
spj.add(("s5","p3","j4",200))
spj.add(("s5","p4","j4",800))
spj.add(("s5","p5","j4",400))
spj.add(("s5","p6","j4",500))
