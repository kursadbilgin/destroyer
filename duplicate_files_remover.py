import os
import logging


def destroyer(path):
    """
    This function finds duplicate files in the directory
    you entered and deletes the most newly created
    """
    filelist = []
    logging.basicConfig(filename='logging.log',
                        format='%(asctime)s %(message)s',
                        datefmt='%d/%m/%Y %I:%M:%S %p', filemode='w',
                        level=logging.DEBUG)

    if os.path.exists(path) and os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for filename in files:
                file_patch = os.path.join(root, filename)
                if filename not in filelist:
                    filelist.append(filename)
                else:
                    try:
                        os.remove("{}/{}".format(root, filename))
                        log_remove = file_patch + " file removed"
                        logging.info(log_remove)
                    except OSError:
                        logging.error("{} can't removed".format(filename))
    else:
        log_error = path + " not found"
        logging.getLogger().addHandler(logging.StreamHandler())
        logging.error(log_error)


path = input("Please enter path -> ")
destroyer(os.path.expanduser(path))
