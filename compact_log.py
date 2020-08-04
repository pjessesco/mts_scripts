import os

def is_mitsuba_log(line):
    if line.find('[mitsuba') != -1:
        return True
    return False

def is_plugin_log(line):
    if line.find('[PluginManager]') != -1:
        return True
    return False

def is_film_log(line):
    if line.find('Film]') != -1:
        return True
    return False

def is_xml_log(line):
    if line.find('[xml') != -1:
        return True
    return False

def is_multifilm_print(line):
    if line.find('.exr') != -1:
        return True
    return False

if __name__ == '__main__':

    log_path = 'path/to/some/log'

    log_file = os.path.join(log_path, 'log.txt')
    compact_log_file = os.path.join(log_path, 'log_compact.txt')

    log = open(log_file, 'r')
    compact_log = open(compact_log_file, 'w')

    while True:
        line = log.readline()

        if not line:
            break

        if is_mitsuba_log(line):
            continue
        # if is_xml_log(line):
        #     continue
        if is_film_log(line):
            continue
        if is_plugin_log(line):
            continue
        if is_multifilm_print(line):
            continue

        compact_log.write(line)

    log.close()

    compact_log.close()
