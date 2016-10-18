from enum import Enum


# noinspection SpellCheckingInspection
class ControlAction(Enum):
    """
    The control action to execute.

    pause: Suspends the execution of the current search.

    unpause: Resumes the execution of the current search, if paused.

    finalize: Stops the search, and provides intermediate results to the /results endpoint.

    cancel: Stops the current search and deletes the result cache.

    touch: Extends the expiration time of the search to now + ttl

    setttl: Change the ttl of the search. Arguments: ttl=<number>

    setpriority: Sets the priority of the search process. Arguments: priority=<0-10>

    enablepreview: Enable preview generation (may slow search considerably).

    disablepreview: Disable preview generation.

    save: saves the search job, storing search artifacts on disk for 7 days. Add or edit the
    default_save_ttl value in limits.conf to override the default value of 7 days.

    unsave: Disables any action performed by save.
    """
    pause = 1
    unpause = 2
    finalize = 3
    cancel = 4
    touch = 5
    setttl = 6
    setpriority = 7
    enablepreview = 8
    disablepreview = 9
