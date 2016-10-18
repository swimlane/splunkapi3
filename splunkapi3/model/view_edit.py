from splunkapi3.model.model import Model


class ViewEdit(Model):
    name_map = {'action_email_to': 'action.email.to',
                'action_email': 'action.email*'}

    def __init__(self, action_email_to: str = None, cron_schedule: str = None,
                 is_scheduled: bool = None, action_email: str = None,
                 description: str = None, disabled: bool = None,
                 next_scheduled_time: str = None):
        """
        c-tor View model for updating.
        :param action_email_to: Comma or semicolon separated list of email
        addresses to send the view to.
        :param cron_schedule: The cron schedule to use for delivering the view.
        Scheduled views are dummy/noop scheduled saved searches that
        email a pdf version of a view. For example: */5 * * * * causes the search to
        execute every 5 minute
        :param is_scheduled: Whether this pdf delivery should be scheduled.
        :param action_email: Wildcard argument that accepts any email action.
        :param description: User readable description of this scheduled view object.
        :param disabled: Whether this object is enabled or disabled.
        :param next_scheduled_time: Ignored on edit.
        """
        self.action_email_to = action_email_to
        self.cron_schedule = cron_schedule
        self.is_scheduled = is_scheduled
        self.action_email = action_email
        self.description = description
        self.disabled = disabled
        self.next_scheduled_time = next_scheduled_time