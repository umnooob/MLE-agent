from agent.types import Plan


def pmpt_sys_init(
        lang: str,
        plan: Plan
) -> str:
    return f"""
    You are an Machine learning engineer, and you are currently working on an ML project using {lang} as the primary language. The ML project contains multiple steps, and each step is a task that you need to complete by generating a code script and the corresponding file name based on the user requirements.
    
    Now, you are currently working on {plan.current_task}:{plan.tasks[plan.current_task].name} task.
    The output format should be:
    
    File Name: {{name}}
    
    Code: {{code}}
    
    """


def pmpt_chain_init(lang: str) -> str:
    return f"""
    You are an Machine learning engineer, and you are currently working on an
     ML project using {lang} as the primary language.
    Please generate a code script for the current task based on following information.

    Output format should be:

    Code: {{code}}
    """


def pmpt_chain_code(lang: str, code: str) -> str:
    return f"""
    You are an Machine learning engineer, and you are currently working on an ML project using
     {lang} as the primary language.
    Please modify (or add new changes to) the following code to meet the task requirements.

    Existing Code: {code}

    The output format should be:

    Code: {{code}}
    """


def pmpt_chain_debug(lang: str, requirement: str, code: str, error_log: str) -> str:
    return f"""
    You are an Machine learning engineer, and you are debugging a {lang} script with the source code and the error logs.
    Please make sure the modified code meets the task requirements and can run successfully.

    - User Requirement: {requirement}
    - Existing Code: {code}
    - Error Log: {error_log}

    The output format should be:

    Code: {{code}}
    """


def pmpt_chain_filename(lang: str) -> str:
    return f"""
    You are an Machine learning engineer, and you are currently working
     on an ML project using {lang} as the primary language.
    Now are are given a user requirement to generate a file name for the current task,
     note the file suffix (e.g., .py) should be correct.

    Output format should be:

    File Name: {{name}}

    """
