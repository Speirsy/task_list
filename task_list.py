the_tasks = [
    { 
      "description": "Wash Dishes", 
      "completed": False,
      "time_taken": 10 
    },
    { 
      "description": "Clean Windows", 
      "completed": False, 
      "time_taken": 15 
    },
    { 
       
      "description": "Make Dinner", 
      "completed": True, 
      "time_taken": 30 
      
    },
    { 
      "description": "Feed Cat", 
      "completed": False, 
      "time_taken": 5 },
    { 
      "description": "Walk Dog", 
      "completed": True, 
      "time_taken": 60 
    },
]
def print_uncompleted_tasks(tasks): #tasks list above is renamed the_tasks

    for task in tasks:
        if task["completed"] == False:
            print(task)

print_uncompleted_tasks(the_tasks)

def print_completed_tasks(jobs):

    for job in jobs:
        if job["completed"] == True:
            print(job)

print_completed_tasks(the_tasks)


for task in the_tasks:
    print( task['description'])


def print_all_tasks(gigs):
    for gig in gigs:
        print_all_tasks(the_tasks)

# Robbed from Function notes (chickens eggs) for investigation
# def count_mins( list ):
#     total_mins = 0

#     for task in list:
#         total_mins += task["time_taken"]
#         task["time_taken"] = 0 

#     return f"{total_mins} minuts spent"

# print(count_mins(tasks))


