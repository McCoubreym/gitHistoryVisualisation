import subprocess
import matplotlib.pyplot as plt

startOfWeeks =[
    "2022-01-31",
    "2022-02-07",
    "2022-02-14",
    "2022-02-21",
    "2022-02-28",
    "2022-03-07",
    "2022-03-14",
    "2022-03-21",
    "2022-03-28",
    "2022-04-04",
    "2022-04-11",
    "2022-04-18",
    "2022-04-25",
    "2022-05-02",
    "2022-05-09",
]
def getNumberOfCommitsForDateRange(start, end, author):
    arguments = [
        "git",
        "rev-list",
        "--all",
        "--count",
        "--since",
        start,
        "--until",
        end
    ]
    if author != None:
        arguments.append("--author")
        arguments.append(author)
    
    return subprocess.check_output(arguments,shell=True)

def getNumberOfCommitsForProject(author):
    commitsForProject = []
    for i in [i for i in range(len(startOfWeeks)) if i != len(startOfWeeks)-1]:
        shellOutput = getNumberOfCommitsForDateRange(startOfWeeks[i], startOfWeeks[i+1], author)
        commitsForProject.append(int(shellOutput))
    return commitsForProject

developerData = getNumberOfCommitsForProject('Michael McCoubrey')
teamsData = getNumberOfCommitsForProject(None)
plt.bar(startOfWeeks[:-1], teamsData, label='Total commits by group')
plt.bar(startOfWeeks[:-1], developerData, label='Total commits by me')
plt.title("Number of commits over time", fontsize=16)
plt.xlabel("Week", fontsize=16)
plt.xticks(rotation=90)
plt.ylabel("Number of commits", fontsize=16)
plt.legend(loc='upper right', bbox_to_anchor=(1, 1), shadow=True, ncol=1)
plt.show()