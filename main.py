# Created by Vaughn and Alex

print('''                                                          
         _               _                  _       _         
 ___ ___| |_ _ _ ___ ___| |   ___ ___ _____|_|___ _| |___ ___ 
|   | .'|  _| | |  _| .'| |  |  _| -_|     | |   | . | -_|  _|
|_|_|__,|_| |___|_| |__,|_|  |_| |___|_|_|_|_|_|_|___|___|_|  
                                                              
''')
import re
from collections import defaultdict
class TaskManager:
    def __init__(self):
        self.tasks = defaultdict(list)
    def add_task(self, task, category="General"):
        self.tasks[category].append(task)
        return f"Task '{task}' added to category '{category}'."
    def remove_task(self, task, category="General"):
        if task in self.tasks[category]:
            self.tasks[category].remove(task)
            return f"Task '{task}' removed from category '{category}'."
        return f"Task '{task}' not found in category '{category}'."
    def list_tasks(self, category=None):
        if category:
            return f"Tasks in '{category}': " + '; '.join(self.tasks[category])
        else:
            all_tasks = []
            for cat, tasks in self.tasks.items():
                all_tasks.append(f"Tasks in '{cat}': " + '; '.join(tasks))
            return '\n'.join(all_tasks)
    def nl_process_command(self, command):
        # Basic natural language patterns
        # Enhanced natural language patterns with memory for last action
        self.last_added_task = None
        add_patterns = [
            r'remind (?:me )?to (.+)',
            r'add (.+) to my (?:todo list|tasks)',
            r'schedule (.+)',
            r"don't forget to (.+)",
            r'can you (?:please )?add (.+) to (?:the )?(?:todo list|tasks)',
            r'please remind me about (.+)',
            r'put (.+) on my (?:agenda|schedule|list)'
        ]
        remove_patterns = [
            r'remove (.+) from my (?:todo list|tasks)',
            r'delete (.+) from (?:todo list|tasks)',
            r'cancel (.+)',
            r'forget about (.+)',
            r"don't add that",
            r'cancel that'
        ]
        list_patterns = [
            r'what\'s on my (?:todo list|tasks)',
            r'(?:show|list) (?:me )?(?:all )?(?:my )?(?:todo list|tasks)',
            r'what do I (?:have to do|need to do)?',
            r'give me an overview of (?:my )?(?:tasks|todo list)'
        ]
        task_extraction_patterns = [
            r'go shopping for (.+)',
            r'buy (.+) from the store',
            r'pick up (.+)'
        ]

        # Method to extract task from command
        def extract_task(self, command):
            for pattern in self.task_extraction_patterns:
                if match := re.match(pattern, command, re.I):
                    return match.group(1).strip()
            return None
        # Combine patterns and check for matches
        for pattern in add_patterns:
            if match := re.match(pattern, command, re.I):
                task = match.group(1).strip()
                return self.add_task(task)
        for pattern in remove_patterns:
            if match := re.match(pattern, command, re.I):
                task = match.group(1).strip()
                return self.remove_task(task)
        for pattern in list_patterns:
            if re.match(pattern, command, re.I):
                return self.list_tasks()
        return "Sorry, I didn't understand that. Could you rephrase it?"
# Example of using the TaskManager class:
# Creating a TaskManager instance
task_manager = TaskManager()
while True:
    command = input("Please enter a command: ")
    if command.lower() == 'exit':
        break
    print(task_manager.nl_process_command(command))