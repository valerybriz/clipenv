import os
from .. import exceptions, filesystem_utilities


def get_env_vars_context(profile_file_path):
    """
    receives a profile file path and a variable already added in the file and
    then modifies the value the containing venvs previously stored in the file.
    """
    try:
        # Check if the profile file exists
        exists = os.path.isfile(profile_file_path)
        if exists:
            with open(profile_file_path, "r") as profile_file:
                all_vars = profile_file.read().splitlines()
            return all_vars
        else:
            raise exceptions.ClipenvFileNotFoundError("File not Found")

    except (exceptions.ClipenvIOError, Exception) as e:
        raise exceptions.ClipenvFileNotFoundError(e)



def add_env_var(variable_name, variable_value, profile_file_path):
    """
    receives a variable name and a value and stores it on the
    previously selected profile file.
    """
    successfully_added = False
    try:
        # The profile file most exists
        exists = os.path.isfile(profile_file_path)
        if exists:
            with open(profile_file_path, "a") as profile_file:
                env_var = F"export {variable_name}='{variable_value}'"
                profile_file.write(env_var)
                profile_file.write("\n")
            successfully_added = True
        else:
            raise exceptions.ClipenvFileNotFoundError("File not Found")

    except (exceptions.ClipenvIOError, Exception) as e:
        raise exceptions.ClipenvFileNotFoundError(e)

    return successfully_added


def list_all_env_vars(profile_file_path):
    """
    receives a profile file path and lists all the containing venvs
    previously stored in the file.
    """
    var_list = get_env_vars_context(profile_file_path)
    return "\n".join(var_list)


def edit_env_var(variable_name, new_variable_value, profile_file_path):
    """
    receives a profile file path and a variable already added in the file and
    then modifies the value the containing venvs previously stored in the file.
    """
    success = False
    try:
        all_vars = get_env_vars_context(profile_file_path)
        found_string, index = filesystem_utilities.check_if_string_in_text(
                variable_name, all_vars
        )
        if found_string:
            edited_var = all_vars[index].split("=")
            #double check if the edited var is the same of the found var
            if edited_var[0] == variable_name:
                new_var = F"export {variable_name}='{new_variable_value}'"
                all_vars[index] = ""
                with open(profile_file_path, "a") as profile_file:
                    profile_file.write(new_var)
                    profile_file.write("\n")

        else:
            raise exceptions.ClipenvVarNotFoundError()


    except (exceptions.ClipenvIOError, Exception) as e:
        raise exceptions.ClipenvFileNotFoundError(e)

    return success


def remove_env_var(variable_name, variable_value, profile_file_path):
    """
    receives a profile file path and a variable already added in the file and
    then modifies the value the containing venvs previously stored in the file.
    """
    all_vars = ""
    try:
        # Check if the profile file exists
        exists = os.path.isfile(profile_file_path)
        if exists:
            with open(profile_file_path, "r") as profile_file:
                all_vars = profile_file.read()
        else:
            raise exceptions.ClipenvFileNotFoundError("File not Found")

        if filesystem_utilities.check_if_string_in_text(
                variable_name, all_vars
        ):
            print("exists")
        else:
            raise exceptions.ClipenvVarNotFoundError()


    except (exceptions.ClipenvIOError, Exception) as e:
        raise exceptions.ClipenvFileNotFoundError(e)

    return all_vars