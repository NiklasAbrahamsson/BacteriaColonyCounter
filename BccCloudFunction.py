import os
import tempfile
from werkzeug.utils import secure_filename
from cv2 import cv2
def get_file_path(filename):
    # Note: tempfile.gettempdir() points to an in-memory file system
    # on GCF. Thus, any files in it must fit in the instance's memory.
    print('filename', filename)
    file_name = secure_filename(filename)
    return os.path.join(tempfile.gettempdir(), file_name)

def bcc(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
     # This code will process each non-file field in the form
    fields = {}
    data = request.form.to_dict()
    for field in data:
        fields[field] = data[field]
        print('Processed field: %s' % field)

    # This code will process each file uploaded
    files = request.files.to_dict()
    print('files', files)
    for file_name, file in files.items():
        # Note: GCF may not keep files saved locally between invocations.
        # If you want to preserve the uploaded files, you should save them
        # to another location (such as a Cloud Storage bucket).
        file.save(get_file_path(file_name))
        print('Processed file: %s' % file_name)

    
    gray = cv2.imread(files[0], 0)

    ## threshold
    th, threshed = cv2.threshold(gray, 100, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

    ## findcontours
    cnts = cv2.findContours(threshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]


    ## filter by area
    s1= 3
    s2 = 20
    xcnts = []
    for cnt in cnts:
        if s1<cv2.contourArea(cnt) <s2:
            xcnts.append(cnt)

    # Clear temporary directory
    for file_name in files:
        file_path = get_file_path(file_name)
        os.remove(file_path)

    return "Dots number: {}".format(len(xcnts))