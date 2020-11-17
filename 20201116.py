skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
answer = 0

skillList = list(skill)
skillLen = len(skillList)
skillTreesLen = len(skill_trees)
newSkillTree = []
wholeNewSkillTree = []

for i in range(0, skillTreesLen):
    skillTreesArr = list(skill_trees[i])
    skillTreesArrLen = len(skillTreesArr)

    for j in range(0, skillTreesArrLen):
        for k in range(0, skillLen):
            if (skillTreesArr[j] == skill[k]):
                newSkillTree.append(skill[k])
    wholeNewSkillTree.append(newSkillTree)
    newSkillTree = []

print(wholeNewSkillTree)