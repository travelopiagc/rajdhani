from . import config


def get_smtp_credentials(testing=False):
    """Returns SMTP credentials as a 4-tuple of (hostname, port, username, password).

    hostname and port will never be None. username or password may be None when
    authentication is not needed.
    """
    if testing is True:
        creds_dict = config.smtp_test
    else:
        creds_dict = config.smtp

    return (creds_dict["hostname"], creds_dict["port"],
            creds_dict["username"], creds_dict["password"])
