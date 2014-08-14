# -*- coding: utf-8 -*-

import codecs


def queue_file_write(queue, file_path, file_contents):
    queue.append({"path": file_path, "contents": file_contents})
    return queue

def write_files(file_queue):
    for file_details in file_queue:
        file_path = file_details["path"]
        file_contents = file_details["contents"]
        with codecs.open(file_path, "w", "utf-8") as f:
            f.write(file_contents)
            print("Wrote '%s'." % file_path)
