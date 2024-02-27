import subprocess


def execute_command(cmd, parameters=[]):
    feedback = {"success": False, "output": ""}
    full_command = [cmd] + parameters

    print(f"Executing: {' '.join(full_command)}")  # Debugging line to see the command

    try:
        result = subprocess.run(full_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        feedback["success"] = True
        feedback["output"] = result.stdout
    except subprocess.CalledProcessError as e:
        feedback["success"] = False
        feedback["output"] = e.stderr
    finally:
        print(f"Command Output: {feedback['output']}")
        return feedback


# Example usage
cmd = "ls"  # Command to execute
parameters = ["-l", "/some/safe/directory"]  # Parameters for the command
execute_command(cmd, parameters)
